from tkinter import Frame

# Colors
SEA_GREEN = "#2E8B57"
SPRING_GREEN = "#00FF7F"


class BaseFrame(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        # Set default positioning.
        self.place(in_=args[0], anchor="c", relx=.5, rely=.5)
        # Set default background color.
        self.configure(bg=SEA_GREEN)
    
