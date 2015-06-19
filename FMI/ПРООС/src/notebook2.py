from tkinter import *



class Notebookk:

    def __init__(self, master, side=LEFT):
        self.active_fr = None
        self.count = 0
        self.choice = IntVar(0)

        if side in (TOP, BOTTOM):
            self.side = LEFT
        else:
            self.side = TOP

        self.rb_fr = Frame(master, borderwidth=2, relief=RIDGE)
        self.rb_fr.pack(side=side, fill=BOTH)
        self.screen_fr = Frame(master, borderwidth=2, relief=RIDGE)
        self.screen_fr.pack(fill=BOTH)

    def __call__(self):
        return self.screen_fr

    def add_screen(self, fr, title):
        b = Radiobutton(self.rb_fr, text=title, indicatoron=0,
                        variable=self.choice, value=self.count,
                        command=lambda: self.display(fr))
        b.pack(fill=BOTH, side=self.side)

        if not self.active_fr:
            fr.pack(fill=BOTH, expand=1)
            self.active_fr = fr

        self.count += 1

        return b

    def display(self, fr):
        self.active_fr.forget()
        fr.pack(fill=BOTH, expand=1)
        self.active_fr = fr

def main():
    a = Tk()
    n = Notebookk(a, LEFT)

    # uses the notebook's frame
    f1 = Frame(n())
    b1 = Button(f1, text="Button 1")
    e1 = Entry(f1)
    # pack your widgets before adding the frame 
    # to the notebook (but not the frame itself)!
    b1.pack(fill=BOTH, expand=1)
    e1.pack(fill=BOTH, expand=1)

    f2 = Frame(n())
    # this button destroys the 1st screen radiobutton
    b2 = Button(f2, text='Button 2', command=lambda:x1.destroy())
    b3 = Button(f2, text='Beep 2', command=lambda:Tk.bell(a))
    b2.pack(fill=BOTH, expand=1)
    b3.pack(fill=BOTH, expand=1)

    f3 = Frame(n())

    # keeps the reference to the radiobutton (optional)
    x1 = n.add_screen(f1, "Screen 1")
    n.add_screen(f2, "Screen 2")
    n.add_screen(f3, "dummy")

    a.mainloop()

if __name__ == "__main__":
        main()
