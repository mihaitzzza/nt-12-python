import tkinter as tk
from gui.base import Frame, MenuBar


class TeacherMenu(MenuBar):
    def __init__(self, logout):
        super().__init__(logout)


class TeacherFrame(tk.Frame, Frame):
    def draw(self):
        label = tk.Label(self, text='TeacherFrame')
        label.pack()
