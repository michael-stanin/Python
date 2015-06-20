import sys
import tkinter as tk

from loginframe import *
from menu import *

class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        
        # Set window title
        self.m_title = tk.Tk.title(self, string="Learn by practice")
        
        # Set window size
        self.m_geometry = tk.Tk.geometry(self, newGeometry="800x600+250+100")
        
        # Set the window icon
        self.m_iconbitmap = tk.Tk.iconbitmap(self, bitmap="../images/favicon-32.ico")
        
        # Background
        self.background_image = tk.PhotoImage(file="../images/background1.png")
        self.background_label = tk.Label(self, image=self.background_image)
        
        # Login Frame
        self.loginFrame = LoginFrame(self)

        
        # Menu Frame
        #self.menuFrame = MenuFrame(self)
        self.menu = Menu(self)
        
        self.show()

        self.callback()
        
    def callback(self):
        # Check every 200 ms if the user has logged in
        self.after_id = self.after(1000, self.callback)
        if self.loginFrame.logged_in:
            self.menu.show()
            self.after_cancel(self.after_id)

    def show(self):
        self.background_label.grid(sticky=N+S+E+W)
        self.loginFrame.show()
        
        
    
