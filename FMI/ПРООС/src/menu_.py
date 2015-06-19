from tkinter import ttk, Frame, Button, PhotoImage, Label
from tkinter import N, S, E, W
from content import *
import os, os.path

SEA_GREEN = "#2E8B57"

class Menu:

    def __init__(self, master, *args, **kwargs):

        self.master = master
        
        self.notebook = ttk.Notebook(self.master)

        self.frames = []

        self._style_config()

        self._fill_notebook()
        self.content = IntroContent

    def show(self):
        self._fill_notebook()


    def _style_config(self):
        ttk.Style().configure("RB.TButton", foreground='maroon',
                              background='black', font=('Helvetica', 12))
        
    def _fill_notebook(self):

        ################# PATCH PATCH PATCH #################
        for i in range(1, 11):
            frame = self._create_frame(self.notebook, borderwidth=5,
                                      relief="sunken", bg="green")

            buttons = self._create_buttons(frame)

            frame.grid(column=0, row=1, columnspan=1, rowspan=1,
                       sticky=(N, S, E, W))

            self._show_buttons(buttons)
            
            self._store_frame(frame, buttons)

            self.add_unit(frame, text="Урок " + str(i), state="disabled")

        self.tabs = self.notebook.tabs()
        self.current_tab = self.tabs[0]
        
        self._enable_tabs()
        self._enable_started_button("yellow")
            
        #self._initial_coloring(frame, buttons)

    def _enable_tabs(self):
        self.notebook.tab(self.current_tab, state="normal")

    def _enable_started_button(self, color):
        frame, buttons = self.frames[self.notebook.index(self.current_tab)]
        for button in buttons:
            if button["background"] != color:
                button.configure(background=color)
                button.configure(command=self._loadIntro)
                break

        #buttons[1].configure(command=self._loadFirstEx)
        #buttons[2].configure(command=self._loadSecondEx)
        #buttons[3].configure(command=self._loadDictation)

        
    def _initial_coloring(self, frame, buttons):
        ################# PATCH PATCH PATCH #################
        # Color only the first one, since we are not storing the results
        # of the done units yet...
        frame, buttons = self.frames[0]
        
        buttons[0].configure(background="yellow")
        buttons[0].config(relief=SUNKEN)

        frame.configure(background="yellow")
        frame.configure(relief=SUNKEN)
        
    def _show_buttons(self, buttons):
        for i, b in enumerate(buttons):
            b.grid(column=i, row=1, sticky=(N, S, E, W))
    
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

        return buttons
        
    def _create_frame(self, master, **kwargs):
        frame = Frame(master, **kwargs)
        return frame
    
    def show(self):
        self.notebook.grid(column=0, row=0, columnspan=2, sticky=N)

    def add_unit(self, frame, **kwargs):
        self.notebook.add(frame, **kwargs)

    def _create_label_images(self, master, path):
        labels = []
        for i in range(4):
            img = PhotoImage(file=path + "a" + str(i+1) + ".png")
            lbl = Label(master, image=img)
            lbl.image = img
            labels.append(lbl)

        return labels

    def _show_label_images(self, labels):
        for i, label in enumerate(labels):
            label.grid(row=1, column=i, sticky=(N, E, S, W), padx=5, pady=5)

    def _loadIntro(self):
        self.load_intro_frame = self._create_frame(self.master, width=450, height=400, relief=RAISED, borderwidth=1, background=SEA_GREEN)

        heading = Label(self.load_intro_frame, text="Буквата Аа", background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        labels = self._create_label_images(self.load_intro_frame, "../images/Letters/a/")

        self._show_label_images(labels)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=4)
        self.load_intro_frame.grid(row=0, column=0)

        prevButton = Button(self.load_intro_frame, text="Назад", state="disabled", width=10)
        prevButton.grid(row=2, column=0, sticky=(W,S))

        nextButton = Button(self.load_intro_frame, text="Продължи", width=10, command=self._toFirstEx)
        nextButton.grid(row=2, column=3, sticky=(E,S))

    def _toFirstEx(self):
        frame, buttons = self.frames[self.notebook.index(self.current_tab)]
        buttons[0].configure(background="green")
        buttons[1].configure(background="yellow")
        self.load_intro_frame.grid_forget()
        self._loadFirstEx()

    def _toIntro(self):
        self.load_intro_frame.grid(row=0, column=0)
        self.load_first_ex_frame.grid_forget()

    def _load_pictures(self, master, path, pictures):
        out_pictures = []
        for picture in pictures:
            img = PhotoImage(file=path + picture)
            lbl = Label(master, image=img)
            lbl.image = img
            out_pictures.append(lbl)
        return out_pictures

    def _show_pictures1(self, pictures):
        columnn = 0
        for picture in pictures:
            picture.grid(row=1, columnspan=4, column=columnn, sticky=(S, N, W), padx=5, pady=5)
            columnn += 4

    def _makeentry(self, master, row, column, **options):
        entry = Entry(master, **options)
        entry.grid(row=row, column=column)
        return entry


    def _load_entries1(self, master):
        entries = []
        for i in range(12):
            entry_string = StringVar()
            entry = self._makeentry(master, 2, i, width=2,
                            textvariable=entry_string, bg="cyan")
            if i in (0, 7, 9, 11):
                entry.configure(bg="dark cyan")
            
            entries.append((entry, entry_string))
        return entries
        
    def first_ex_callback(self):
        # Check every 200 ms if the user has logged in
        self.after_first_ex_id = self.load_first_ex_frame.after(200, self.first_ex_callback)

        filled = False

        for (entry, string) in self.first_ex_entries:
            filled = not(string.get() == "")
            entry.delete(1, len(string.get()))

        if filled:
            self.load_first_ex_frame.after_cancel(self.after_first_ex_id)
            self.load_first_ex_frame_nextButton.configure(state="normal")

    def _check_firstEx_answers(self, expected):
        actual = ""
        for (entry, string) in self.first_ex_entries:
            actual += string.get()
        
        # Gather all wrong input
        wrong_entries = []
        [wrong_entries.append(i) for i, ch in enumerate(actual) if not(ch == expected[i])]

        # Color the wrong input
        [self.first_ex_entries[wr][0].configure(background="red") for wr in wrong_entries]

        if wrong_entries:
            messagebox.showinfo("Грешен отговор",
            ":( Опитай пак!")
            # Change back color of the entries to their default and reset the text as well
            for wrong_entry in wrong_entries:
                if wrong_entry in (0, 7, 9, 11):
                    self.first_ex_entries[wrong_entry][0].configure(bg="dark cyan")
                else:
                    self.first_ex_entries[wrong_entry][0].configure(bg="cyan")
                self.first_ex_entries[wrong_entry][1].set("")
            self.load_first_ex_frame_nextButton.configure(state="disabled")
            self.first_ex_callback()
            return False
        return True


    def _loadFirstEx(self):
        self.load_first_ex_frame = self._create_frame(self.master, width=450, height=400, relief=RAISED, borderwidth=1, background=SEA_GREEN)

        heading = Label(self.load_first_ex_frame, text="Буквата Аа", background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        pictures = self._load_pictures(self.load_first_ex_frame, "../images/Letters/a/", ["Агне.png", "rose.png", "maika.png"])

        self.first_ex_entries = self._load_entries1(self.load_first_ex_frame)
        self._show_pictures1(pictures)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=12)
        self.load_first_ex_frame.grid(row=0, column=0)

        prevButton = Button(self.load_first_ex_frame, text="Назад", command=self._toIntro)#, width=10
        prevButton.grid(row=3, column=0, sticky=(W,S))

        self.load_first_ex_frame_nextButton = Button(self.load_first_ex_frame, text="Продължи", state="disabled", command=self._toSecondEx)#, width=10
        self.load_first_ex_frame_nextButton.grid(row=3, column=11, sticky=(E,S))

        self.first_ex_callback()

    def _toSecondEx(self):
        if self._check_firstEx_answers("агнерозамама"):
            messagebox.showinfo("Правилен отговор",
            ":) Продължавай напред!")
            frame, buttons = self.frames[self.notebook.index(self.current_tab)]
            buttons[1].configure(background="green")
            buttons[2].configure(background="yellow")
            self.load_first_ex_frame.grid_forget()
            self._loadSecondEx()

    def _show_pictures2(self, pictures):
        columnn = 0
        for i, picture in enumerate(pictures):
            if i == 0:
                picture.grid(row=1, columnspan=6, column=columnn, sticky=(S, N, W), padx=5, pady=5)
                columnn += 6
            elif i == 1:
                picture.grid(row=1, columnspan=4, column=columnn, sticky=(S, N, W), padx=5, pady=5)
                columnn += 4
            else:
                picture.grid(row=1, columnspan=5, column=columnn, sticky=(S, N, W), padx=5, pady=5)
                columnn += 5

    def _load_entries2(self, master):
        entries = []
        for i in range(15):
            entry_string = StringVar()
            entry = self._makeentry(master, 2, i, width=2,
                            textvariable=entry_string, bg="cyan")
            if i in (1, 5, 9, 11, 14):
                entry.configure(bg="dark cyan")
            
            entries.append((entry, entry_string))
        return entries

    def second_ex_callback(self):
        # Check every 200 ms if the user has logged in
        self.after_second_ex_id = self.load_second_ex_frame.after(200, self.second_ex_callback)

        filled = False

        for (entry, string) in self.second_ex_entries:
            filled = not(string.get() == "")
            entry.delete(1, len(string.get()))

        if filled:
            self.load_second_ex_frame.after_cancel(self.after_second_ex_id)
            self.load_second_ex_frame_nextButton.configure(state="normal")

    def _check_secondEx_answers(self, expected):
        actual = ""
        for (entry, string) in self.second_ex_entries:
            actual += string.get()
        
        # Gather all wrong input
        wrong_entries = []
        [wrong_entries.append(i) for i, ch in enumerate(actual) if not(ch == expected[i])]

        # Color the wrong input
        [self.second_ex_entries[wr][0].configure(background="red") for wr in wrong_entries]

        if wrong_entries:
            messagebox.showinfo("Грешен отговор",
            ":( Опитай пак!")
            # Change back color of the entries to their default and reset the text as well
            for wrong_entry in wrong_entries:
                if wrong_entry in (1, 5, 9, 11, 14):
                    self.second_ex_entries[wrong_entry][0].configure(bg="dark cyan")
                else:
                    self.second_ex_entries[wrong_entry][0].configure(bg="cyan")
                self.second_ex_entries[wrong_entry][1].set("")
            self.load_second_ex_frame_nextButton.configure(state="disabled")
            self.second_ex_callback()
            return False
        return True

    def _loadSecondEx(self):
        self.load_second_ex_frame = self._create_frame(self.master, width=450, height=400, relief=RAISED, borderwidth=1, background=SEA_GREEN)

        heading = Label(self.load_second_ex_frame, text="Буквата Аа", background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        pictures = self._load_pictures(self.load_second_ex_frame, "../images/Letters/a/", ["ranica.png", "пола.png", "шапка.png"])

        self.second_ex_entries = self._load_entries2(self.load_second_ex_frame)
        self._show_pictures2(pictures)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=15)
        self.load_second_ex_frame.grid(row=0, column=0)

        prevButton = Button(self.load_second_ex_frame, text="Назад", command=self._backToFirstEx)#, width=10
        prevButton.grid(row=3, column=0, sticky=(W,S))

        self.load_second_ex_frame_nextButton = Button(self.load_second_ex_frame, text="Продължи", state="disabled", command=self._toDictation)#, width=10
        self.load_second_ex_frame_nextButton.grid(row=3, column=14, sticky=(E,S))

        self.second_ex_callback()


    def _backToFirstEx(self):
        self.load_first_ex_frame.grid(row=0, column=0)
        self.load_second_ex_frame.grid_forget()

    def _toDictation(self):
        if self._check_secondEx_answers("раницаполашапка"):
            messagebox.showinfo("Правилен отговор",
            ":) Продължавай напред!")
            frame, buttons = self.frames[self.notebook.index(self.current_tab)]
            buttons[2].configure(background="green")
            buttons[3].configure(background="yellow")
            self.load_second_ex_frame.grid_forget()
            self._loadDictation()

    def _loadDictation(self):
        self.load_dictation_frame = self._create_frame(self.master, width=450, height=400, relief=RAISED, borderwidth=1, background=SEA_GREEN)

        heading = Label(self.load_dictation_frame, text="Буквата Аа", background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        pictures = self._load_pictures(self.load_dictation_frame, "../images/Letters/a/", ["UC2.png"])

        self._show_pictures1(pictures)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=4)
        self.load_dictation_frame.grid(row=0, column=0)

        prevButton = Button(self.load_dictation_frame, text="Назад", command=self._backToSecondEx)#, width=10
        prevButton.grid(row=3, column=0, sticky=(W,S))

        self.load_dictation_frame_nextButton = Button(self.load_dictation_frame, text="Продължи", command=self._toNextUnit)#, width=10
        self.load_dictation_frame_nextButton.grid(row=3, column=3, sticky=(E,S))

    def _backToSecondEx(self):
        self.load_second_ex_frame.grid(row=0, column=0)
        self.load_dictation_frame.grid_forget()

    def _toNextUnit(self):
        frame, buttons = self.frames[self.notebook.index(self.current_tab)]
        buttons[3].configure(background="green")
        frame.configure(background="green")
        self.load_dictation_frame.grid_forget()
        self.tabs = self.notebook.tabs()
        self.current_tab = self.tabs[1]
        self.notebook.tab(self.current_tab, state="normal")
        frame, buttons = self.frames[self.notebook.index(self.current_tab)]
        self.notebook.select(self.notebook.index(self.current_tab))
        buttons[0].configure(background="yellow")
        buttons[0].config(relief=SUNKEN)
        self._loadSUIntro()

    def _backToFU(self):
        self.load_SU_intro_frame.grid_forget()
        self.notebook.select(self.notebook.index(self.tabs[0]))
        self.tabs = self.notebook.tabs()
        self.current_tab = self.tabs[1]
        self.load_intro_frame.grid(row=0, column=0)

    def _loadSUIntro(self):
        self.load_SU_intro_frame = self._create_frame(self.master, width=450, height=400, relief=RAISED, borderwidth=1, background=SEA_GREEN)

        heading = Label(self.load_SU_intro_frame, text="Буквата Ъъ", background=SEA_GREEN, font=("Helvetica", 20), fg="cyan")
        pictures = self._load_pictures(self.load_SU_intro_frame, "../images/Letters/ъ/", ["ъ1.png", "ъ2.png", "ъ3.png", "ъ4.png"])

        self._show_pictures1(pictures)
        heading.grid(row=0, sticky=(N, S, E, W), columnspan=16)
        self.load_SU_intro_frame.grid(row=0, column=0)

        prevButton = Button(self.load_SU_intro_frame, text="Назад", command=self._backToFU)
        prevButton.grid(row=3, column=0, sticky=(W,S))

        self.load_SU_intro_frame_nextButton = Button(self.load_SU_intro_frame, text="Продължи", command=self._SUtoFirstEx)
        self.load_SU_intro_frame_nextButton.grid(row=3, column=15, sticky=(E,S))

    def _SUtoFirstEx(self):
        pass