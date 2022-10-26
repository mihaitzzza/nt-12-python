import tkinter as tk
from gui.login import LoginFrame
from gui.admin import AdminFrame
from gui.teacher import TeacherFrame
from gui.student import StudentFrame
from helpers.db import authenticate
from utility.enums import RoleTypes


class Application:
    def __init__(self):
        self._logged_user = None

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
        pass

    def _draw(self):
        if self._frame:
            self._frame.pack_forget()

        if self._logged_user:
            if self._logged_user.role.name == RoleTypes.admin:
                self._frame = AdminFrame(self._window, self._logout)
            elif self._logged_user.role.name == RoleTypes.teacher:
                self._frame = TeacherFrame(self._window, self._logout)
            else:
                self._frame = StudentFrame(self._window, self._logout)
        else:
            self._frame = LoginFrame(self._window, self._authenticate)

        self._frame.draw()
        self._frame.pack()

    def run(self):
        self._draw()
        self._window.mainloop()
