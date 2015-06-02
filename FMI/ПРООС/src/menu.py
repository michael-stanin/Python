from tkinter import ttk, N, S, E, W
from unitparser import UnitParser


class Menu:

    def __init__(self, master=None, *args, **kwargs):
        self.tree = ttk.Treeview(master)
        self.master = master
        self.fill_tree()

    def fill_tree(self):
        parser = UnitParser()
        parser.parse()
        units = parser.units()

        for unit in units:
            self.tree.insert("", "end", unit, text=unit, tag=(unit), open=True)
            #self.tree.tag_configure(unit, background="gray")

    def show(self):
        print("test")
        """in_=self.master,"""
        self.tree.grid(in_=self.master, row=5, column=5, sticky=N+S+E+W)
