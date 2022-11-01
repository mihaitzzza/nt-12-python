import tkinter as tk
from abc import ABC, abstractmethod


class Frame(ABC):
    @abstractmethod
    def draw(self):
        pass


class Table(tk.Frame):
    def __init__(self, master, *args, data=None, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._data = data or []

    def draw(self):
        for row_index, row_data in enumerate(self._data):
            for col_index, col_data in enumerate(row_data):
                # class_parameters = col_data['class_parameters'] if 'class_parameters' in col_data else {}
                class_parameters = col_data.get('class_parameters', {})

                element = col_data['class'](self, text=col_data['text'], **class_parameters)
                element.grid(row=row_index, column=col_index)
