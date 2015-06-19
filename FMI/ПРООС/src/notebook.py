from tkinter import *
from tkinter import ttk
from baseframe import *

class Notebook:
    # initialization. receives the master widget
    # reference and the notebook orientation
    def __init__(self, master, side="e"):
        self.active_fr = None
        self.count = 0
        self.choice = IntVar(0)
        
	
        # allows the TOP and BOTTOM
	# radiobuttons' positioning.
        #if side in (N, S):
            #self.side = E
        #else:
            #self.side = N
        self.side = side
        # creates notebook's frames structure
        self.rb_fr = BaseFrame(master, borderwidth=5, relief=RIDGE)
        self.rb_fr.grid(sticky=side)
        self.screen_fr = BaseFrame(master, borderwidth=5, relief=RIDGE)
        self.screen_fr.grid(sticky=side)

    # return a master frame reference for the external frames (screens)
    def __call__(self):
        return self.screen_fr

    # add a new frame (screen) to the (bottom/left of the) notebook
    def add_screen(self, fr, title):
        b = Radiobutton(self.rb_fr, text=title, indicatoron=0,
                        variable=self.choice, value=self.count,
                        command=lambda: self.display(fr))
        #b.grid(sticky=self.side)
        b.grid(sticky="n")

        # ensures the first frame will be
	# the first selected/enabled
        if not self.active_fr:
            fr.grid(sticky="nsew")
            self.active_fr = fr

        self.count += 1

        # returns a reference to the newly created
        # radiobutton (allowing its configuration/destruction)      
        return b

    # hides the former active frame and shows 
    # another one, keeping its reference
    def display(self, fr):
        self.active_fr.grid_forget()
        fr.grid(sticky=W)#+S+E+W)
        self.active_fr = fr
