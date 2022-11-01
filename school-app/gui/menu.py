import tkinter as tk


class Menu(tk.Menu):
    def __init__(self, master, logout, *args, menu_options=(), **kwargs):
        super().__init__(master, *args, **kwargs)

        self._logout = logout
        self._menu_options = menu_options

    # def _get_recursive_options(self):
    #     for option in self._menu_options:
    #         if 'children' in option:
    #             sub_level_menu = tk.Menu(self, tearoff=0)
    #
    #             for children in option['children']:
    #
    #                 sub_level_menu.add_command(
    #                     label=children['name'],
    #                     command=children['command']
    #                 )
    #
    #             self.add_cascade(label=option['name'], menu=sub_level_menu)
    #         else:
    #             self.add_command(label=option['name'], command=option['command'])

    def _get_recursive_options(self, menu, options):
        for option in options:
            if 'children' in option:
                sub_level_menu = tk.Menu(self, tearoff=0)
                self._get_recursive_options(sub_level_menu, option['children'])
                menu.add_cascade(label=option['name'], menu=sub_level_menu)
            else:
                menu.add_command(label=option['name'], command=option['command'])

    def draw(self):
        self._get_recursive_options(self, self._menu_options)
        self.add_command(label='Logout', command=self._logout)
