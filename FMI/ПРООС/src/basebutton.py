from tkinter import Button

# Colors
SEA_GREEN = "#2E8B57"
SPRING_GREEN = "#00FF7F"


class BaseButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)

        self.__configure()

    def bgColor(self, color=SPRING_GREEN):
        self.configure(bg=color)

    def activeBackGround(self, color=SEA_GREEN):
        self.configure(activebackground=color)
        
    def __configure(self):
        self.bgColor()
        self.activeBackGround()
        
