import tkinter as tk
from gui.base import Frame, MenuBar


class AdminMenu(MenuBar):
    def __init__(self, master, logout):
        super().__init__(master, logout)


class AdminFrame(tk.Frame, Frame):
    def __init__(self, master, logout, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        print('master', master, type(master))
        self._menu_bar = AdminMenu(master, logout)
        master.config(menu=self._menu_bar.menu)

    def draw(self):
        label = tk.Label(self, text='AdminFrame')
        label.pack()
