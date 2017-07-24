from tkinter import Label, Entry, messagebox, StringVar, PhotoImage
from tkinter import N, S, W, E

from baseframe import *
from basebutton import *
from filereader import *


USERS_STORAGE = "users.txt"


def users():
    return [user.split() for user in FileReader.read_users(USERS_STORAGE)]


def correct_credentials(*args):
        if any(args[0] == user[0] and args[1] == user[1] for user in users()):
            return True
        return False


class LoginFrame(BaseFrame):

    def __init__(self, master=None, *args, **kwargs):
        BaseFrame.__init__(self, master, *args, **kwargs)

        self.master = master

        self.logged_in_ = False
        
    @property
    def logged_in(self):
        return self.logged_in_

    @logged_in.setter
    def logged_in(self, value):
        self.logged_in_ = value

    def show(self):
        self._show_labels()
        self._show_entries()
        self._show_buttons()     

    def _makelabel(self, row=0, rowspan=1, sticky=E, columnspan=1, **options):
        label = Label(self, **options)
        label.grid(row=row, sticky=sticky, rowspan=rowspan, columnspan=columnspan)
        return label
    
    def _show_funny_owl_label(self):
        img = PhotoImage(file="../images/funnyowl.png")
        self.funnyowl = self._makelabel(sticky=N, columnspan=2, image=img)
        self.funnyowl.image = img

    def _show_labels(self):
        self._show_funny_owl_label()
        self._show_username_label()
        self._show_password_label()

    def _show_username_label(self):
        self.username_label = self._makelabel(1, 1, E, text="Потребителско име:", bg=SEA_GREEN)

    def _show_password_label(self):
        self.password_label = self._makelabel(2, 1, E, text="Парола:", bg=SEA_GREEN)

    def _makeentry(self, row, column, sticky=W, **options):
        entry = Entry(self, **options)
        entry.grid(row=row, column=column, sticky=sticky)
        return entry
    
    def _show_entries(self):
        self._show_username_entry()
        self._show_password_entry()
        
    def _show_username_entry(self):
        self.username = StringVar()
        self.username_entry = self._makeentry(1, 1, width=20, textvariable=self.username, bg=SEA_GREEN)
        self.username_entry.focus_set()

    def _show_password_entry(self):
        self.password = StringVar()
        self.password_entry = self._makeentry(2, 1, width=20, show="*", textvariable=self.password, bg=SEA_GREEN)
    
    def _show_buttons(self):
        self._show_login_button()
        
    def _show_login_button(self):
        self.login_button = BaseButton(self, text="Влез")
        self.login_button.bind("<Button-1>", self.login)
        self.login_button.bind("<Return>", self.login)
        self.login_button.grid(row=3, sticky=N+S+E+W, columnspan=2)

    def hide(self):
        self._hide_labels()
        self._hide_entries()
        self._hide_buttons()
        self.destroy()

    def _hide_labels(self):
        self.username_label.grid_remove()
        self.password_label.grid_remove()

    def _hide_entries(self):
        self.username_entry.grid_remove()
        self.password_entry.grid_remove()

    def _hide_buttons(self):
        self.login_button.grid_remove()

    def _username(self):
        return self.username.get()

    def _password(self):
        return self.password.get()

    # Login
    def login(self, event):
        if self._username() == "" or self._password() == "":
            messagebox.showwarning("Грешен вход", "Липсващи полета. Моля въведете потребителско име и парола.")
        elif correct_credentials(self._username(), self._password()):
            self.hide()
            self.logged_in_ = True
            messagebox.showinfo("Успешно влизане", "{} successfully logged in!".format(self._username()))
        else:
            messagebox.showerror("Грешен вход", "Грешно потребителско име или парола. Опитайте пак")
