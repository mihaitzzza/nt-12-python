import tkinter as tk
from gui.base import Frame
from gui.menu import Menu


class TeacherFrame(tk.Frame, Frame):
    def __init__(self, master, logout, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._menu_bar = Menu(master, logout, menu_options=({
            'name': 'Courses',
            'command': lambda: print('view teacher courses frame'),
        }, {
            'name': 'Students',
            'command': lambda: print('view teacher students frame'),
        }))
        self._menu_bar.draw()
        master.config(menu=self._menu_bar)

    def draw(self):
        label = tk.Label(self, text='TeacherFrame')
        label.pack()
