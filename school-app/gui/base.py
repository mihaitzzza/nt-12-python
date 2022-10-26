import tkinter as tk
from abc import ABC, abstractmethod


class Frame(ABC):
    @abstractmethod
    def draw(self):
        pass


class MenuBar:
    def __init__(self, master, logout):
        self.menu = tk.Menu(master, tearoff=0)
        self.menu.add_command(label='Logout', command=logout)
