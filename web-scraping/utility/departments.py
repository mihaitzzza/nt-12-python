from selenium.webdriver.common.by import By
from utility.base import BaseElement
from utility.categories import Category


class Department(BaseElement):
    def __init__(self, element, driver):
        super().__init__(element, driver)
        self._categories = []

    def extract_data(self):
        title_element = self._element.find_element(By.TAG_NAME, 'h3')
        self._title = title_element.text

        category_elements = self._element.find_elements(By.XPATH, './/div[contains(@class, "subdepartment-col")]')
        for category_element in category_elements:
            category = Category(category_element, self._driver)
            category.extract_data()

            self._categories.append(category)

            break
