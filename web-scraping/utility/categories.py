from selenium.webdriver.common.by import By
from utility.base import BaseElement
from utility.subcategories import Subcategory


class Category(BaseElement):
    def __init__(self, element, driver):
        super().__init__(element, driver)
        self._subcategories = []

    def extract_data(self):
        title_element = self._element.find_element(By.TAG_NAME, 'h4')
        self._title = title_element.text

        subcategory_elements = self._element.find_elements(By.XPATH, './/ul/li')
        for subcategory_element in subcategory_elements:
            subcategory = Subcategory(subcategory_element, self._driver)
            subcategory.extract_data()

            self._subcategories.append(subcategory)

            break
