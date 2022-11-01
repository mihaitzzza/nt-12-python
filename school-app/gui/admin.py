import tkinter as tk
import functools
from gui.base import Frame, Table
from gui.menu import Menu


class CoursesFrame(tk.Frame, Frame):
    def __init__(self, master, set_active_course, *args, courses=None, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._courses = courses or []
        self._set_active_course = set_active_course
        self._label = tk.Label(self, text='CourseFrame')
        self._table_frame = None

    def __set_active_course(self, course_id, course_index, value):
        # Internal logic for updating course is_active status
        self._courses[course_index].is_active = value

        # Call function to update into database
        self._set_active_course(course_id, value)

        # Re-draw data
        self.draw()
        # self._table_frame.update()

    def draw(self):
        self._label.pack_forget()
        self._label.pack()

        table_header = (
            ({
                 'text': 'ID', 'class': tk.Label
             }, {
                 'text': 'Name', 'class': tk.Label
             }, {
                'text': 'Hours', 'class': tk.Label
            }, {
                'text': 'Is Active', 'class': tk.Label
            }),
        )
        table_data = [
            (
                {'text': course.id, 'class': tk.Label},
                {'text': course.name, 'class': tk.Label},
                {'text': int(course.hours), 'class': tk.Label},
                {
                    'text': 'Deactivate' if course.is_active else 'Activate',
                    'class': tk.Button,
                    'class_parameters': {
                        'command': functools.partial(self.__set_active_course, course.id, course_index, not course.is_active)
                    }
                }
            )
            for course_index, course in enumerate(self._courses)
        ]

        if self._table_frame is not None:
            self._table_frame.pack_forget()

        self._table_frame = Table(self, data=[*table_header, *table_data])
        self._table_frame.pack()
        self._table_frame.draw()


class AddCourseFrame(tk.Frame, Frame):
    def draw(self):
        label = tk.Label(self, text='AddNewCourseFrame')
        label.pack()


class AdminFrame(tk.Frame, Frame):
    def __init__(self, master, logout, set_active_course, *args, courses=None, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._menu_bar = Menu(master, logout, menu_options=({
            'name': 'Courses',
            'children': ({
                'name': 'View all',
                'command': lambda: self._set_frame(CoursesFrame(self, set_active_course, courses=courses))
            }, {
                'name': 'Add new course',
                'command': lambda: self._set_frame(AddCourseFrame())
            })
        }, {
            'name': 'Accounts',
            'children': ({
                'name': 'Add new account',
                'command': lambda: print('admin frame add new account')
            }, {
                'name': 'View all',
                'command': lambda: print('admin frame view all accounts')
            })
        }))
        self._menu_bar.draw()
        master.config(menu=self._menu_bar)

        self._frame = CoursesFrame(self, set_active_course, courses=courses)

    def _set_frame(self, frame_instance):
        self._frame.pack_forget()

        self._frame = frame_instance
        self.draw()

    def draw(self):
        self._frame.draw()
        self._frame.pack()
