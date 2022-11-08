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
        print('self._title', self._title)

        category_elements = self._element.find_elements(By.XPATH, './/div[contains(@class, "subdepartment-col")]')
        for index, category_element in enumerate(category_elements):
            category = Category(category_element, self._driver)
            category.extract_data()

            self._categories.append(category)

            if index == 2:
                break

    def to_dict(self):
        return {
            'title': self._title,
            'categories': [
                category.to_dict()
                for category in self._categories
            ]
        }
