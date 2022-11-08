from abc import ABC, abstractmethod


class BaseElement(ABC):
    def __init__(self, element, driver):
        self._element = element
        self._driver = driver
        self._title = None

    @abstractmethod
    def extract_data(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
