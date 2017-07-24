import sys
import tkinter as tk
from PIL import Image, ImageTk

from loginframe import *
from menu import *

class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        # Set window title
        self.m_title = tk.Tk.title(self, string="Learn by practice")
        
        # Set window size
        self.m_geometry = tk.Tk.geometry(self, newGeometry="1500x768+250+100")

        # Do not allow resizing.
        self.resizable(width=False, height=False)

        # Set the window icon
        self.m_iconbitmap = tk.Tk.iconbitmap(self, bitmap="../images/favicon-32.ico")

        self.background = BackgroundFrame(self)
        self.background.grid(row=0, column=0, sticky=N+S+E+W)
        self.background.grid_rowconfigure(0, weight=1)
        self.background.grid_columnconfigure(0, weight=1)

        # Login Frame
        self.loginFrame = LoginFrame(self)
        
        # Menu Frame
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
        self.loginFrame.show()
        
        
    
class BackgroundFrame(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.master = master

        # Uncomment below if continuous resizing is required, i.e the window is resizable
        #self.master.bind('<Configure>', self._resize_image)

        self.grid(row=0,sticky=N+S+E+W)

        self.image = Image.open("../images/background1.png")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.grid(row=0, column=0, sticky=N+S+E+W)
        self.background.grid_rowconfigure(0, weight=1)
        self.background.grid_columnconfigure(0, weight=1)

        self._resize_image_once()

    def _resize_image(self, event=None, _last=[None] * 2):
        if event is not None and event.widget is self.master and (
            _last[0] != event.width or _last[1] != event.height):

            # size changed; update image
            _last[:] = event.width, event.height
            self._resize_image_once()

    def _resize_image_once(self):
        new_width = self.master.winfo_width()
        new_height = self.master.winfo_height()

        self.image = self.img_copy.resize((new_width, new_height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)