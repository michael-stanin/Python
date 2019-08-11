"""
from tkinter import ttk, Frame, Button, PhotoImage, Label, BOTH, Canvas, Scrollbar, LEFT, RIGHT, Y
import tkinter as tk

root = tk.Tk()
root.resizable(0,0)
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True)
notebook.pressed_index = None
container = Frame(notebook)
container.pack(fill=BOTH, expand=True)
for i in range(1, 31):
    notebook.add(container, text="Урок " + str(i))#, state="disabled")
#notebook.add(container, text='Mode A')

canvas = Canvas(container, width=200, height=400)
scroll = Scrollbar(container, command=canvas.yview)
canvas.config(yscrollcommand=scroll.set, scrollregion=(0,0,100,1000))
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)

frame = Frame(canvas, bg='white', width=200, height=1000)
canvas.create_window(100, 500, window=frame)

root.mainloop()
"""

from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.title("Title")
root.geometry("600x600")
root.configure(background="black")



class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("../images/background1.png")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image, relief="sunken")
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)




if __name__ == "__main__":
    e = Example(root)
    e.pack(fill=BOTH, expand=YES)

    root.mainloop()