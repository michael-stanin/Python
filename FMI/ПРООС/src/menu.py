from tkinter import ttk, Frame, Button, PhotoImage, Label, Entry, messagebox
from tkinter import N, S, E, W, RAISED, SUNKEN, StringVar
from unitsmanager import UnitsManager
from utilities import *


def clear_grid(root):
    for entry in root.grid_slaves():
        entry.destroy()



class Menu:

    def __init__(self, master, *args, **kwargs):

        self.master = master
        
        self.notebook = ttk.Notebook(self.master)

        self.previous_unit = None
        self.current_unit = None

        self.temp_ex_frame = None
        self.previous_ex_frame = None
        self.current_ex_frame = None

        self.frames = []

        style_config()

    def show(self):
        self.notebook.grid(column=0, row=0, columnspan=2, sticky=N)
        self._fill_notebook()

    def _fill_notebook(self):
        for i in range(1, len(mgr.units) + 1):
            frame = create_frame(self.notebook, borderwidth=5, relief="sunken", bg="green")

            buttons = self._create_buttons(frame)

            configure_frame(frame, buttons)

            configure_buttons(buttons)
            
            self._store_frame(frame, buttons)

            self.add_unit(frame, text="Урок " + str(i), state="disabled", sticky=E+W)

        self.tabs = self.notebook.tabs()
        self.current_tab = self.tabs[0]
        self.current_notebook_tab_index = self.notebook.index(self.current_tab)

        self._enable_current_tab()
        self._enable_intro_button("yellow")

    def _enable_current_tab(self):
        self.notebook.tab(self.current_tab, state="normal")

    def _enable_intro_button(self, color):
        frame, buttons = self.frames[self.current_notebook_tab_index]

        intro_button = buttons[0]
        if intro_button["background"] != color:
            intro_button.configure(background=color)
            intro_button.configure(relief=SUNKEN)
            intro_button.configure(command=self._load_intro)

        # TODO: Think how to change the colors of the notebook tabs:
        # https://stackoverflow.com/questions/23038356/change-color-of-tab-header-in-ttk-notebook

    def _store_frame(self, frame, buttons):
        self.frames.append((frame, buttons))
    
    def _create_buttons(self, master):
        buttons = []
        intro = Button(master, text="Въведение")
        ex1 = Button(master, text="Упражнение 1")
        ex2 = Button(master, text="Упражнение 2")
        dictation = Button(master, text="Диктовка")

        buttons.append(intro)
        buttons.append(ex1)
        buttons.append(ex2)
        buttons.append(dictation)

        self.current_button_idx = 0

        return buttons

    def add_unit(self, frame, **kwargs):
        self.notebook.add(frame, **kwargs)

    def _first_unit_exercise(self, event):
        # Prepare the notebook for the next unit

        frame, buttons = self.frames[self.current_notebook_tab_index]
        buttons[self.current_button_idx].configure(background="green")
        self.current_button_idx += 1
        buttons[self.current_button_idx].configure(background="yellow")

        # TODO: Change intro_frame to previous = current_frame and forget it
        self.intro_frame.grid_forget()

        self._load_exercise()

    def _previous_unit_ex(self, event):
        mgr.previous_ex()
        self.current_button_idx -= 1
        self.previous_ex_frame.grid(row=0, column=0)
        self.current_ex_frame.grid_forget()
        self.previous_ex_frame = self.current_ex_frame
        self.current_ex_frame = self.temp_ex_frame


    def _load_exercise(self):
        self.current_ex_frame = create_content_frame(self.master)

        heading = Label(self.current_ex_frame, text=self.current_unit.name, background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        pictures = create_images(self.current_ex_frame, mgr.current_ex_path())

        self.current_ex_entries = load_entries(self.current_ex_frame)
        show_pictures(pictures)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=len("".join(mgr.current_ex))+1)
        self.current_ex_frame.grid(row=0, column=0)

        prev_button = Button(self.current_ex_frame, text="Назад")
        if mgr.current_ex_idx:
            prev_button.bind("<Button-1>", self._previous_unit_ex)
        else:
            prev_button.bind("<Button-1>", self._to_unit_intro)
        prev_button.grid(row=3, column=0, sticky=(W, S))

        self.current_next_button = self.load_first_ex_frame_nextButton = Button(self.current_ex_frame, text="Продължи", state="disabled")
        self.load_first_ex_frame_nextButton.grid(row=3, column=len("".join(mgr.current_ex)), sticky=(E, S))
        if mgr.current_ex_idx + 1 < len(self.current_unit.exercises):
            self.load_first_ex_frame_nextButton.bind("<Button-1>", self._next_unit_exercise)
        else:
            self.load_first_ex_frame_nextButton.bind("<Button-1>", self._to_unit_dictation)

        self._current_ex_callback()

    def _next_unit_exercise(self, event):
        if self._check_exercise_answers():
            messagebox.showinfo("Правилен отговор", ":) Продължавай напред!")
            frame, buttons = self.frames[self.current_notebook_tab_index]
            buttons[self.current_button_idx].configure(background="green")
            self.current_button_idx += 1
            buttons[self.current_button_idx].configure(background="yellow")
            # TODO: Change intro_frame to previous = current_frame and forget it
            #if self.temp_ex_frame and self.temp_ex_frame is not None:
            self.temp_ex_frame = self.current_ex_frame
            self.current_ex_frame.grid_forget()
            mgr.next_ex()
            if self.previous_ex_frame and self.previous_ex_frame is not None:
                self.previous_ex_frame.grid(row=0, column=0)
                self.current_ex_frame = self.previous_ex_frame
            else:
                self.previous_ex_frame = self.current_ex_frame
                self._load_exercise()



    def _check_exercise_answers(self):
        words = "".join(mgr.current_ex)
        actual = ""
        for (entry, string) in self.current_ex_entries:
            actual += string.get()

        # Gather all wrong input
        wrong_entries = []
        [wrong_entries.append(i) for i, ch in enumerate(actual) if not (ch == words[i].lower())]

        # Color the wrong input
        [self.current_ex_entries[wr][0].configure(background="red") for wr in wrong_entries]

        if wrong_entries:
            messagebox.showinfo("Грешен отговор", ":( Опитай пак!")
            # Change back color of the entries to their default and reset the text as well
            for wrong_entry in wrong_entries:
                if words[wrong_entry].isupper():
                    self.current_ex_entries[wrong_entry][0].configure(bg="dark cyan")
                else:
                    self.current_ex_entries[wrong_entry][0].configure(bg="cyan")
                self.current_ex_entries[wrong_entry][1].set("")
            self.current_next_button.configure(state="disabled")
            self._current_ex_callback()
            return False
        return True

    def _previous_unit(self, event):
        frame, buttons = self.frames[self.current_notebook_tab_index]
        buttons[3].configure(background="green")
        frame.configure(background="green")
        self.intro_frame.grid_forget()

        self.tabs = self.notebook.tabs()
        self.current_notebook_tab_index -= 1
        self.current_tab = self.tabs[self.current_notebook_tab_index]
        self.notebook.select(self.current_notebook_tab_index)

        self.current_button_idx = 0

        self.previous_unit = self.current_unit
        mgr.previous_unit()
        self._load_intro()

    def _load_intro(self):
        self.current_unit = mgr.current_unit
        self.intro_frame = create_content_frame(self.master)

        heading = Label(self.intro_frame, text=self.current_unit.name, background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        labels = create_images(self.intro_frame, self.current_unit.intro_path())

        show_label_images(labels)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=4)
        self.intro_frame.grid(row=0, column=0)

        prev_button = Button(self.intro_frame, text="Назад", state="disabled", width=10)
        prev_button.grid(row=2, column=0, sticky=(W, S))
        if mgr.current_unit_idx:
            prev_button.configure(state="normal")
            prev_button.bind("<Button-1>", self._previous_unit)

        next_button = Button(self.intro_frame, text="Продължи", width=10)
        next_button.grid(row=2, column=3, sticky=(E, S))
        if mgr.current_ex_idx < len(self.current_unit.exercises):
            next_button.bind("<Button-1>", self._first_unit_exercise)

    def _to_unit_intro(self, event):
        self.current_button_idx -= 1
        self.current_ex_frame.grid_forget()
        self.intro_frame.grid(row=0, column=0)

    def _current_ex_callback(self):
        # Check every 200 ms if the user has logged in
        self.after_current_ex_id = self.current_ex_frame.after(200, self._current_ex_callback)

        filled = False

        for (entry, string) in self.current_ex_entries:
            filled = not(string.get() == "")
            entry.delete(1, len(string.get()))

        if filled:
            self.current_ex_frame.after_cancel(self.after_current_ex_id)
            self.current_next_button.configure(state="normal")

    def _to_unit_dictation(self, event):
        if self._check_exercise_answers():
            messagebox.showinfo("Правилен отговор", ":) Продължавай напред!")
            frame, buttons = self.frames[self.current_notebook_tab_index]
            buttons[self.current_button_idx].configure(background="green")
            self.current_button_idx += 1
            buttons[self.current_button_idx].configure(background="yellow")
            self.previous_ex_frame = self.current_ex_frame
            self.current_ex_frame.grid_forget()
            self._load_dictation()

    def _load_dictation(self):
        self.current_ex_frame = self.load_dictation_frame = create_content_frame(self.master)

        heading = Label(self.load_dictation_frame, text=self.current_unit.name, background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        pictures = create_images(self.load_dictation_frame, self.current_unit.dictation_path())

        show_pictures(pictures)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=4)
        self.load_dictation_frame.grid(row=0, column=0)

        prev_button = Button(self.load_dictation_frame, text="Назад")
        prev_button.bind("<Button-1>", self._previous_unit_ex)
        prev_button.grid(row=3, column=0, sticky=(W, S))

        self.load_dictation_frame_nextButton = Button(self.load_dictation_frame, text="Продължи", state="disabled", command=self._to_next_unit)
        if self.current_notebook_tab_index + 1 < len(self.tabs):
            self.load_dictation_frame_nextButton.configure(state="normal")
        self.load_dictation_frame_nextButton.grid(row=3, column=5, sticky=(E, S))

    """
    def _back_to_second_ex(self):
        self.load_second_ex_frame.grid(row=0, column=0)
        self.load_dictation_frame.grid_forget()
    """
    def _to_next_unit(self):
        frame, buttons = self.frames[self.current_notebook_tab_index]
        buttons[3].configure(background="green")
        frame.configure(background="green")
        self.load_dictation_frame.grid_forget()

        self.tabs = self.notebook.tabs()
        self.current_notebook_tab_index += 1
        self.current_tab = self.tabs[self.current_notebook_tab_index]
        self.notebook.tab(self.current_tab, state="normal")
        self.notebook.select(self.current_notebook_tab_index)

        self.current_button_idx = 0
        frame, buttons = self.frames[self.current_notebook_tab_index]
        buttons[self.current_button_idx].configure(background="yellow")
        buttons[self.current_button_idx].config(relief=SUNKEN)

        self.previous_unit = self.current_unit
        mgr.next_unit()
        self._load_intro()

    def _back_to_first_unit(self):
        # TODO: FIX THIS METHOD - IT CAN BE IMPLEMENTED AS BACK_TO_PREVIOUS_UNIT. Instead of hard coding the tabs index use the current_notebook_tab_index-1 etc...
        self.load_SU_intro_frame.grid_forget()
        self.notebook.select(self.notebook.index(self.tabs[0]))
        self.tabs = self.notebook.tabs()
        self.current_tab = self.tabs[1]
        self.intro_frame.grid(row=0, column=0)

    """
    def _load_second_unit_intro(self):
        self.load_SU_intro_frame = create_content_frame(self.master)

        heading = Label(self.load_SU_intro_frame, text="Буквата Ъъ", background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        pictures = create_images(self.load_SU_intro_frame, "../images/Letters/ъ/intro/")

        show_pictures1(pictures)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=16)
        self.load_SU_intro_frame.grid(row=0, column=0)

        prev_button = Button(self.load_SU_intro_frame, text="Назад", command=self._back_to_first_unit)
        prev_button.grid(row=3, column=0, sticky=(W, S))

        self.load_SU_intro_frame_nextButton = Button(self.load_SU_intro_frame, text="Продължи", command=self._second_unit_to_first_ex)
        self.load_SU_intro_frame_nextButton.grid(row=3, column=15, sticky=(E, S))

    def _second_unit_to_first_ex(self):
        pass
    """
