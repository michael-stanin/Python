from baseframe import *
from basebutton import *
from student import *
#from menu import *
from notebook import *


class MenuFrame(BaseFrame):

    def __init__(self, master=None, *args, **kwargs):
        BaseFrame.__init__(self, master, *args, **kwargs)

        #self.place(anchor=W)
        self.master = master
        
        #self.menu = Menu(self.master)
        self.notebook = Notebook(self.master, W)
        
    def show(self):
        print("In menu frame show")
        self._init_frames()
        self._init_sub_frames()
        self._add_to_notebook()

    def _init_frames(self):
        self.frames = []
        for i in range(10):
            frame = Frame(self.notebook())
            self.frames.append(frame)
            
    def _init_sub_frames(self):
        for i, frame in enumerate(self.frames):
            introductionFrame = Button(frame, text="Въведение в Урок 1",
                                command=lambda: print("Въведение в Урок 1"))
            excFrame = Button(frame, text="Упражнение",
                              command=lambda: print("Упражнение за урок 1"))
            dictationFrame = Button(frame, text="Диктовка",
                                command=lambda: print("Диктовка за урок 1"))
            introductionFrame.grid(row=0, column=1)
            excFrame.grid(row=0, column=2)
            dictationFrame.grid(row=0, column=3)

    def _add_to_notebook(self):
        self.configurable_frames = []
        for i, frame in enumerate(self.frames):
            self.configurable_frames.append(self.notebook.add_screen(
                frame, "Урок " + str(i)))           
            
        
        
    """ 
    @property
    def user(self):
        return self.user_

    @user.setter
    def user(self, value):
        self.user_ = value
    
    def _makelabel(self, row=0, rowspan=1, sticky=W, **options):
        label = Label(self, **options)
        label.grid(row=row, sticky=sticky, rowspan=rowspan)
        return label

    def init_units(self):
        #tasks = self.user.tasks
        #for task in tasks:
            #self.menu.add_command(label=task.title, command=self.on_click)
        for i in range(5):
            self.menu.add_command(label="Урок " + str(i), command=self.on_click)
            print("Урок " + str(i))
        self.master.config(menu=self.menu)
            
    def on_click(self, e):
        pass
    """
