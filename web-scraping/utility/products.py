import requests
from time import sleep
from uuid import uuid4
from selenium.webdriver.common.by import By
from utility.base import BaseElement


class Product(BaseElement):
    def __init__(self, element, driver):
        super().__init__(element, driver)
        self._id = uuid4()
        self._price = None
        self._image_path = None
        self._specifications = {}

    def extract_data(self):
        link_element = self._element.find_element(By.TAG_NAME, 'a')

        self._driver.execute_script(f'window.open("{link_element.get_attribute("href")}")')
        self._driver.switch_to.window(self._driver.window_handles[-1])

        try:
            self._title = self._driver.find_element(By.XPATH, './/h1[@class="page-title"]').text

            self._price = float(
                self._driver.find_element(
                    By.XPATH, './/div[contains(@class, "product-main-area")]//p[contains(@class, "product-new-price")]'
                ).text.replace(' Lei', '').replace('.', '').replace(',', '.')
            )

            image_element = self._driver.find_element(By.XPATH, './/div[@data-ph-id="image-0"]//img')
            image_data = requests.get(url=image_element.get_attribute('src')).content
            self._image_path = f'./images/{self._id}.jpg'
            with open(self._image_path, 'wb') as image_file:
                image_file.write(image_data)

            # Extend specifications body
            button = self._driver.find_element(By.XPATH, './/button[@data-ph-target="#specifications-body"]')
            button.click()

            sleep(0.5)

            # Get product specifications
            specifications_body = self._driver.find_element(By.ID, 'specifications-body')
            title_elements = specifications_body.find_elements(By.TAG_NAME, 'p')
            table_elements = specifications_body.find_elements(By.TAG_NAME, 'table')

            for title_element, table_element in zip(title_elements, table_elements):
                specs_title = title_element.text
                self._specifications[specs_title] = {}

                row_elements = table_element.find_elements(By.TAG_NAME, 'tr')
                for row_element in row_elements:
                    cells = row_element.find_elements(By.TAG_NAME, 'td')
                    subcategory = cells[0].text
                    value = cells[1].text

                    self._specifications[specs_title][subcategory] = value
        except Exception as e:
            print(e)

        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def to_dict(self):
        return {
            'id': str(self._id),
            'title': self._title,
            'price': self._price,
            'image_path': self._image_path,
            'specifications': self._specifications
        }
