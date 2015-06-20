import tkinter as tk
from menuframe import *
from notebook import *
from baseframe import *
from tkinter import *
from tkinter import ttk
from menu_ import Menu as mMenu
from content import *


class App(tk.Tk):

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
        
        self.menu = mMenu(self)
        
        self.show()

    def show(self):
        #pass
        self.background_label.grid(row=0, column=0)
        self.menu.show()

def main():
    root = Tk()

    content = ttk.Frame(root, padding=(3,3,12,12))
    frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
    namelbl = ttk.Label(content, text="Name")
    name = ttk.Entry(content)

    onevar = BooleanVar()
    twovar = BooleanVar()
    threevar = BooleanVar()

    onevar.set(True)
    twovar.set(False)
    threevar.set(True)

    one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
    two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
    three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
    ok = ttk.Button(content, text="Okay")
    cancel = ttk.Button(content, text="Cancel")

    content.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
    namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
    name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
    one.grid(column=0, row=3)
    two.grid(column=1, row=3)
    three.grid(column=2, row=3)
    ok.grid(column=3, row=3)
    cancel.grid(column=4, row=3)

    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3)
    content.columnconfigure(1, weight=3)
    content.columnconfigure(2, weight=3)
    content.columnconfigure(3, weight=1)
    content.columnconfigure(4, weight=1)
    content.rowconfigure(1, weight=1)

    root.mainloop()

   
if __name__ == "__main__":
    app = App()
    #main()
    app.mainloop()








