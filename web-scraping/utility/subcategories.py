from selenium.webdriver.common.by import By
from utility.base import BaseElement
from utility.products import Product


class Subcategory(BaseElement):
    def __init__(self, element, driver):
        super().__init__(element, driver)
        self._products = []

    def extract_data(self):
        link_element = self._element.find_element(By.TAG_NAME, 'a')
        self._title = link_element.text
        print('subcategory title:', self._title)

        self._driver.execute_script(f'window.open("{link_element.get_attribute("href")}")')
        self._driver.switch_to.window(self._driver.window_handles[-1])

        product_elements = self._driver.find_elements(
            By.XPATH,
            './/div[@id="card_grid"]//div[contains(@class, "card-item")]'
        )
        for product_element in product_elements:
            product = Product(product_element, self._driver)
            product.extract_data()
            self._products.append(product)

            break

        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[-1])
