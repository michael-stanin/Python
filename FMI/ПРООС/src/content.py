from tkinter import *


class IntroContent:

    def __init__(self, master=None, *args, **kwargs):

        self.master = master
        self.frame = Frame(background="yellow", width=200, height=100)
        self.frame.grid_bbox(column=2, row=2)
        
