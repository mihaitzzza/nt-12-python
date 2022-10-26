import tkinter as tk
from gui.base import Frame, MenuBar


class StudentMenu(MenuBar):
    def __init__(self, logout):
        super().__init__(logout)


class StudentFrame(tk.Frame, Frame):
    def draw(self):
        label = tk.Label(self, text='StudentFrame')
        label.pack()
