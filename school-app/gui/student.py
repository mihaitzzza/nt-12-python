import tkinter as tk
from gui.base import Frame, Table
from gui.menu import Menu


class StudentFrame(tk.Frame, Frame):
    def __init__(self, master, logout, *args, courses=None, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._menu_bar = Menu(master, logout)
        self._menu_bar.draw()
        master.config(menu=self._menu_bar)

        # if courses is None:
        #     self._courses = []
        # else:
        #     self._courses = courses
        self._courses = courses or []

    def draw(self):
        if len(self._courses) == 0:
            empty_course = tk.Label(self, text='You are not enrolled to any courses.')
            empty_course.pack()
        else:
            table_data = [
                (student_course.course.name, student_course.grade or 'N/A')
                for student_course in self._courses
            ]

            course_frame = Table(self, data=table_data)
            course_frame.pack()
            course_frame.draw()
