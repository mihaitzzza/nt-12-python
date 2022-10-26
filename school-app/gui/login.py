import tkinter as tk
from gui.base import Frame
from utility.security import validate_email


class LoginFrame(tk.Frame, Frame):
    def __init__(self, master, authenticate, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._authenticate = authenticate
        self._error_message = tk.StringVar()

        self._label = tk.Label(self, text='Authenticate', font=('Arial', 16, 'bold'))
        self._email_entry = tk.Entry(self)
        self._password_entry = tk.Entry(self, show='*')
        self._button = tk.Button(self, text='Login', command=self._login)
        self._error_label = tk.Label(self, textvariable=self._error_message, fg='red')

    def _login(self):
        email = self._email_entry.get()

        if not validate_email(email):
            self._error_message.set('Invalid e-mail.')
            return

        self._error_message.set('')

        password = self._password_entry.get()

        user = self._authenticate(email, password)
        if user is None:
            self._error_message.set('Invalid credentials.')

    def draw(self):
        self._label.pack(pady=6)
        self._email_entry.pack(pady=6)
        self._password_entry.pack(pady=6)
        self._button.pack(pady=6)
        self._error_label.pack(pady=6)
