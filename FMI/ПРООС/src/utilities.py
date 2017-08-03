import os
import glob
from tkinter import ttk, Frame, PhotoImage, Label, Entry
from tkinter import N, S, E, W, RAISED, StringVar
from unitsmanager import UnitsManager


SEA_GREEN = "#2E8B57"

units_manager = UnitsManager()


def is_valid_file(f):
    return os.path.exists(f) and os.path.isfile(f)


def extract_file_paths(path):
    t = []
    fps = glob.glob(path + "**/**", recursive=True)
    for f in fps:
        if is_valid_file(f):
            t.append(f)
    return t


def configure_frame(frame, buttons):
    frame.grid(column=0, row=1, columnspan=1, rowspan=1, sticky=(N, S, E, W))
    for bi, b in enumerate(buttons):
        frame.columnconfigure(bi, weight=1)


def configure_buttons(buttons):
    for i, b in enumerate(buttons):
        b.grid(column=i, row=1, sticky=(N, S, E, W))


def create_frame(master, **kwargs):
    frame = Frame(master, **kwargs)
    return frame


def create_content_frame(master):
    return create_frame(master, width=450, height=400, relief=RAISED, borderwidth=1, background=SEA_GREEN)


def create_images(master, path):
    fps = extract_file_paths(path)
    images = []
    for i in fps:
        img = PhotoImage(file=i)
        lbl = Label(master, image=img)
        lbl.image = img
        images.append(lbl)
    return images


def show_pictures(pictures, needs_span=True):
    column = 0
    words = units_manager.current_ex
    options = {'row': 1, 'sticky': (S, N, W), 'padx': 5, 'pady': 5}
    for i, picture in enumerate(pictures):
        if needs_span:
            span = len(words[i])
            options['columnspan'] = span
            options['column'] = column
            column += span
        else:
            column = i
            options['column'] = column
        picture.grid(options)


def load_pictures(master, path, pictures):
    out_pictures = []
    for picture in pictures:
        img = PhotoImage(file=path + picture)
        lbl = Label(master, image=img)
        lbl.image = img
        out_pictures.append(lbl)
    return out_pictures


def make_entry(master, row, column, **options):
    entry = Entry(master, **options)
    entry.grid(row=row, column=column)
    return entry


def load_entries(master):
    entries = []
    words = "".join(units_manager.current_ex)
    for i, c in enumerate(words):
        entry_string = StringVar()
        background_color = "dark cyan" if c.isupper() else "cyan"
        entry = make_entry(master, 2, i, width=2, textvariable=entry_string, bg=background_color)
        entries.append((entry, entry_string))
    return entries


def style_config():
    ttk.Style().configure("RB.TButton", foreground='maroon', background='black', font=('Helvetica', 12))
