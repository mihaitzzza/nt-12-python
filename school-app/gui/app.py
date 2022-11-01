import tkinter as tk
from gui.login import LoginFrame
from gui.admin import AdminFrame
from gui.teacher import TeacherFrame
from gui.student import StudentFrame
from helpers.db import authenticate, get_student_courses, get_all_courses, set_active_course
from utility.enums import RoleTypes


class Application:
    def __init__(self):
        # self._logged_user = None
        self._logged_user = authenticate('mihai@gmail.com', 'python123')

        self._window = tk.Tk()
        self._window.geometry('800x600')  # set 800 x 400 size
        # self._window.attributes('-zoomed', True)
        self._window.winfo_toplevel().title('NT-12-PYTHON School App')

        self._frame = None

    def _authenticate(self, email, password):
        user = authenticate(email, password)

        if user is not None:
            self._logged_user = user
            self._draw()

        return user

    def _logout(self):
        self._logged_user = None
        self._draw()

    def _draw(self):
        if self._frame:
            self._frame.pack_forget()

        if self._logged_user:
            if self._logged_user.role.name == RoleTypes.admin:
                self._frame = AdminFrame(self._window, self._logout, set_active_course, courses=get_all_courses())
            elif self._logged_user.role.name == RoleTypes.teacher:
                self._frame = TeacherFrame(self._window, self._logout)
            else:
                courses = get_student_courses(self._logged_user)
                self._frame = StudentFrame(self._window, self._logout, courses=courses)
        else:
            self._window.config(menu='')
            self._frame = LoginFrame(self._window, self._authenticate)

        self._frame.draw()
        self._frame.pack()

    def run(self):
        self._draw()
        self._window.mainloop()
