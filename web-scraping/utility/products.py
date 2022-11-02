import requests
from uuid import uuid4
from selenium.webdriver.common.by import By
from utility.base import BaseElement


class Product(BaseElement):
    def __init__(self, element, driver):
        super().__init__(element, driver)
        self._id = uuid4()
        self._price = None
        self._image = None

    def extract_data(self):
        link_element = self._element.find_element(By.TAG_NAME, 'a')

        self._driver.execute_script(f'window.open("{link_element.get_attribute("href")}")')
        self._driver.switch_to.window(self._driver.window_handles[-1])

        self._title = self._driver.find_element(By.XPATH, './/h1[@class="page-title"]').text

        self._price = float(
            self._driver.find_element(
                By.XPATH, './/div[contains(@class, "product-main-area")]//p[@class="product-new-price"]'
            ).text.replace(' Lei', '').replace('.', '').replace(',', '.')
        )

        image_element = self._driver.find_element(By.XPATH, './/div[@data-ph-id="image-0"]//img')
        image_data = requests.get(url=image_element.get_attribute('src')).content
        with open(f'./images/{self._id}.jpg', 'wb') as image_file:
            image_file.write(image_data)

        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[-1])
