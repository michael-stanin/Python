from tkinter import Button, messagebox
from tkinter import SUNKEN
from utilities import *


class Menu:

    def __init__(self, master):

        self.master = master
        
        self.notebook = ttk.Notebook(self.master)

        self.previous_unit = None
        self.current_unit = None

        self.current_frame = None
        self.ex_frames = []
        self.current_ex_frame_id = -1
        self.frames = []

        style_config()

    def show(self):
        self.notebook.grid(column=0, row=0, columnspan=2, sticky=N)
        self._fill_notebook()

    def _fill_notebook(self):
        for i in range(1, len(units_manager.units) + 1):
            frame = create_frame(self.notebook, borderwidth=5, relief="sunken", bg="green")

            buttons = self._create_buttons(frame)

            configure_frame(frame, buttons)

            configure_buttons(buttons)
            
            self._store_frame(frame, buttons)

            self.add_unit(frame, text="Урок " + str(i), state="disabled", sticky=E+W)

        self.tabs = self.notebook.tabs()
        self.current_tab = self.tabs[0]
        self.current_notebook_tab_index = self.notebook.index(self.current_tab)
        self.notebook.select(self.current_notebook_tab_index)

        self._enable_current_tab()
        self._enable_intro_button("yellow")

    def _enable_current_tab(self):
        self.notebook.tab(self.current_tab, state="normal")

    def _enable_intro_button(self, color):
        frame, buttons = self.frames[self.current_notebook_tab_index]

        intro_button = buttons[0]
        if intro_button["background"] != color:
            intro_button.configure(background=color)
            intro_button.configure(command=self._load_intro)
        # intro_button.invoke()
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

    def _load_exercise(self):
        self.current_frame = ExFrame(self.master, units_manager.current_unit)
        self.current_frame.show()
        self.ex_frames.append(self.current_frame)
        self.current_ex_frame_id += 1

        if units_manager.current_ex_idx:
            self.current_frame.bind_prev_button(self._to_prev_ex)
        else:
            self.current_frame.bind_prev_button(self._to_unit_intro)

        if units_manager.current_ex_idx + 1 < len(self.current_unit.exercises):
            self.current_frame.bind_next_button(self._to_next_ex)
        else:
            self.current_frame.bind_next_button(self._to_unit_dictation)

        self.current_frame.callback()

    def _load_intro(self):
        self.current_unit = units_manager.current_unit
        self.current_frame = IntroExFrame(self.master, units_manager.current_unit)
        self.current_frame.show()
        self.ex_frames.append(self.current_frame)
        self.current_ex_frame_id += 1

        if units_manager.current_unit_idx:
            self.current_frame.config_prev_button_state('normal')
            self.current_frame.bind_prev_button(self._to_prev_unit)
        if units_manager.current_ex_idx < len(self.current_unit.exercises):
            self.current_frame.bind_next_button(self._to_first_ex)

    def _to_unit_intro(self, event):
        self.current_frame.hide()
        self.current_frame = self.ex_frames[self.current_ex_frame_id - 1]
        self.current_frame.grid(row=0, column=0)
        self.current_ex_frame_id -= 1

    def _to_unit_dictation(self, event):
        if self.current_frame.check_exercise_answers():
            try:
                self.current_frame.hide()
                self.current_frame = self.ex_frames[self.current_ex_frame_id + 1]
                self.current_frame.grid(row=0, column=0)
                self.current_ex_frame_id += 1
            except IndexError:
                messagebox.showinfo("Правилен отговор", ":) Продължавай напред!")
                frame, buttons = self.frames[self.current_notebook_tab_index]
                buttons[self.current_button_idx].configure(background="green")
                buttons[self.current_button_idx].config(relief=SUNKEN)
                self.current_button_idx += 1
                buttons[self.current_button_idx].configure(background="yellow")
                self._load_dictation()

    def _to_first_ex(self, event):
        try:
            self.current_frame.hide()
            self.current_frame = self.ex_frames[self.current_ex_frame_id + 1]
            self.current_frame.grid(row=0, column=0)
            self.current_ex_frame_id += 1
        except IndexError:
            frame, buttons = self.frames[self.current_notebook_tab_index]
            buttons[self.current_button_idx].configure(background="green")
            buttons[self.current_button_idx].config(relief=SUNKEN)
            self.current_button_idx += 1
            buttons[self.current_button_idx].configure(background="yellow")
            self._load_exercise()

    def _to_prev_ex_from_dictation(self, event):
        self.current_frame.hide()
        self.current_frame = self.ex_frames[self.current_ex_frame_id - 1]
        self.current_frame.grid(row=0, column=0)
        self.current_ex_frame_id -= 1

    def _to_prev_ex(self, event):
        if units_manager.current_ex_idx:
            units_manager.previous_ex()
        self._to_prev_ex_from_dictation(event)

    def _to_next_ex(self, event):
        if self.current_frame.check_exercise_answers():
            units_manager.next_ex()
            try:
                self.current_frame.hide()
                self.current_frame = self.ex_frames[self.current_ex_frame_id + 1]
                self.current_frame.grid(row=0, column=0)
                self.current_ex_frame_id += 1
            except IndexError:
                messagebox.showinfo("Правилен отговор", ":) Продължавай напред!")
                frame, buttons = self.frames[self.current_notebook_tab_index]
                buttons[self.current_button_idx].configure(background="green")
                buttons[self.current_button_idx].config(relief=SUNKEN)
                self.current_button_idx += 1
                buttons[self.current_button_idx].configure(background="yellow")
                self._load_exercise()

    def _load_dictation(self):
        self.current_frame = DictationExFrame(self.master, units_manager.current_unit)
        self.current_frame.show()
        self.ex_frames.append(self.current_frame)
        self.current_ex_frame_id += 1

        self.current_frame.bind_prev_button(self._to_prev_ex_from_dictation)
        if self.current_notebook_tab_index + 1 < len(self.tabs):
            self.current_frame.config_next_button_state('normal')
            self.current_frame.bind_next_button(self._to_next_unit)
        else:
            frame, buttons = self.frames[self.current_notebook_tab_index]
            buttons[self.current_button_idx].configure(background="green")
            buttons[self.current_button_idx].config(relief=SUNKEN)
            frame.configure(background="green")
            messagebox.showinfo("Поздравления!", ":) Завърши обучението!")

    def _to_next_unit(self, event):
        frame, buttons = self.frames[self.current_notebook_tab_index]
        buttons[self.current_button_idx].configure(background="green")
        buttons[self.current_button_idx].config(relief=SUNKEN)
        frame.configure(background="green")

        self.tabs = self.notebook.tabs()
        self.current_notebook_tab_index += 1
        self.current_tab = self.tabs[self.current_notebook_tab_index]
        self.notebook.tab(self.current_tab, state="normal")
        self.notebook.select(self.current_notebook_tab_index)

        self.current_button_idx = 0
        frame, buttons = self.frames[self.current_notebook_tab_index]

        units_manager.next_unit()
        try:
            self.current_frame.hide()
            self.current_frame = self.ex_frames[self.current_ex_frame_id + 1]
            self.current_frame.grid(row=0, column=0)
            self.current_ex_frame_id += 1
        except IndexError:
            buttons[self.current_button_idx].configure(background="yellow")
            self._load_intro()

    def _to_prev_unit(self, event):
        self.current_frame.hide()
        self.tabs = self.notebook.tabs()
        self.current_notebook_tab_index -= 1
        self.current_tab = self.tabs[self.current_notebook_tab_index]
        self.notebook.select(self.current_notebook_tab_index)

        self.current_button_idx = 0

        units_manager.previous_unit()
        self.current_ex_frame_id = self.current_ex_frame_id - len(units_manager.current_unit.exercises) - 2
        self.current_frame = self.ex_frames[self.current_ex_frame_id]
        self.current_frame.grid(row=0, column=0)


class BaseExFrame:

    def __init__(self, master, current_unit, needs_span):

        self.master = master
        self.frame = create_content_frame(self.master)
        self.current_unit = current_unit
        self.needs_span = needs_span
        self.heading_column_span = 1
        self.heading_options = {'background': SEA_GREEN, 'font': ("Helvetica", 20), 'fg': "cyan"}
        self.entries = []
        self.prev_button = None
        self.next_button = None

    def show(self):
        self.heading_options['text'] = self.current_unit.name
        heading = Label(master=self.frame, cnf=self.heading_options)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=self.heading_column_span)

        pictures = create_images(self.frame, self._images_path())
        show_pictures(pictures, self.needs_span)

        self.entries = self._load_entries()

        self.prev_button = Button(self.frame, text="Назад")
        self._config_prev_button()
        self.prev_button.grid(row=3, column=0, sticky=(W, S))

        self.next_button = Button(self.frame, text="Продължи", state="disabled")
        self._config_next_button()
        self._grid_next_button()

        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def grid(self, row, column):
        self.frame.grid(row=row, column=column)

    def _images_path(self):
        pass

    def _load_entries(self):
        pass

    def _callback(self):
        pass

    def _config_prev_button(self):
        self.prev_button['width'] = 10

    def bind_prev_button(self, command):
        self.prev_button.bind("<Button-1>", command)

    def _config_next_button(self):
        self.next_button['width'] = 10

    def _grid_next_button(self):
        self.next_button.grid(row=3, column=self.heading_column_span - 1, sticky=(E, S))

    def bind_next_button(self, command):
        self.next_button.bind("<Button-1>", command)


class IntroExFrame(BaseExFrame):

    def __init__(self, master, current_unit):
        super(IntroExFrame, self).__init__(master, current_unit, False)
        self.heading_column_span = 4  # 4 - THE NUMBER OF PICTURES SHOWN - THIS MIGHT NEED TO BE CHANGED

    def _images_path(self):
        return self.current_unit.intro_path()

    def _config_prev_button(self):
        self.config_prev_button_state('disabled')

    def _config_next_button(self):
        self.next_button['state'] = 'normal'

    def config_prev_button_state(self, state):
        self.prev_button['state'] = state


class DictationExFrame(BaseExFrame):
    def __init__(self, master, current_unit):
        super(DictationExFrame, self).__init__(master, current_unit, True)
        self.heading_column_span = len(units_manager.current_ex[0])  # little "hack" - I am fed up

    def _images_path(self):
        return self.current_unit.dictation_path()

    def config_next_button_state(self, state):
        self.next_button['state'] = state


class ExFrame(BaseExFrame):
    def __init__(self, master, current_unit):
        super(ExFrame, self).__init__(master, current_unit, True)
        self.heading_column_span = len("".join(units_manager.current_ex)) + 1
        self.after_current_ex_id = None

    def _images_path(self):
        return units_manager.current_ex_path()

    def _load_entries(self):
        return load_entries(self.frame)

    def callback(self):
        # Check every 200 ms if the user has logged in
        self.after_current_ex_id = self.frame.after(200, self.callback)

        filled = False

        for (entry, string) in self.entries:
            filled = not (string.get() == "")
            entry.delete(1, len(string.get()))

        if filled:
            self.frame.after_cancel(self.after_current_ex_id)
            self.next_button.configure(state="normal")

    def _grid_next_button(self):
        self.next_button.grid(row=3, column=self.heading_column_span - 2, sticky=(E, S))

    def check_exercise_answers(self):
        words = "".join(units_manager.current_ex)
        actual = ""
        for (entry, string) in self.entries:
            actual += string.get()

        # Gather all wrong input
        wrong_entries = []
        [wrong_entries.append(i) for i, ch in enumerate(actual) if not (ch == words[i].lower())]

        # Color the wrong input
        [self.entries[wr][0].configure(background="red") for wr in wrong_entries]

        if wrong_entries:
            messagebox.showinfo("Грешен отговор", ":( Опитай пак!")
            # Change back color of the entries to their default and reset the text as well
            for wrong_entry in wrong_entries:
                if words[wrong_entry].isupper():
                    self.entries[wrong_entry][0].configure(bg="dark cyan")
                else:
                    self.entries[wrong_entry][0].configure(bg="cyan")
                self.entries[wrong_entry][1].set("")
            self.next_button.configure(state="disabled")
            self._callback()
            return False
        return True
