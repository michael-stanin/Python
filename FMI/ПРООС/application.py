import sys
import tkinter as tk

from filereader import FileReader 
from filewriter import FileWriter


class Application(tk.Tk):


    users_storage = "users.txt"

    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Set window title
        self.m_title = tk.Tk.title(self, string="Learn by practice")
        
        # Set window size
        self.m_geometry = tk.Tk.geometry(self, newGeometry="800x600+250+100")
        
        # Set the window icon
        self.m_iconbitmap = tk.Tk.iconbitmap(self, bitmap="favicon-32.ico")

        # Username and password labels
        #self.m_user_name_label = tk.Label(text="username: ", fg="blue")
        #self.m_user_name_label.grid(row=0, column=0)
        #self.m_user_pass_label = tk.Label(text="password: ", fg="blue")
        #self.m_user_pass_label.grid(row=1, column=0)
        
        # Background
        self.background_image = tk.PhotoImage("background1.jpg")
        self.background_label = tk.Label(self,image=self.background_image)
        self.background_label.pack()


    def __users(self):
        return [user.split() for user in FileReader.read(self.users_storage)]

    def __correct_credentials(self, *args):
        if any(args[0] == user[0] and args[1] == user[1]
                            for user in self.__users()):
            return True
        return False
    
    # Registering the users using (username, password, gender, privileges)
    def register(self, *args):
        if len(args) == 4 and not(any(args[0] == user[0]
                            for user in self.__users())):
            FileWriter.write(self.users_storage, *args)
            print("{} registered!".format(args[0]))
        else:
            print("User name already exists. Try another user name.")

    # Login using (username, password)
    def login(self, *args):
        if len(args) < 2:
            print("Missing fields. Please enter both user name and password")
        elif self.__correct_credentials(*args):
            # TODO: Implement the logic after user login
            print("{} successfully logged in!".format(args[0]))
