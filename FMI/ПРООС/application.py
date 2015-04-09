import sys
import tkinter as tk


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Set window title
        self.m_title = tk.Tk.title(self, string="Learn by practice")
        # Set window size
        self.m_geometry = tk.Tk.geometry(self, newGeometry="800x600+250+100")
        # Set the window icon
        self.m_iconbitmap = tk.Tk.iconbitmap(self, bitmap="favicon-32.ico")
        self.m_user_name_label = tk.Label(text="username: ",
                                         fg="blue").grid(row=0, column=0)
        self.m_user_pass_label = tk.Label(text="password: ",
                                         fg="blue").grid(row=1, column=0)        

    
