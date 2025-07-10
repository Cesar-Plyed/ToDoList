import tkinter as tk
from webbrowser import get
from ..resources.resources import BACKGROUND_COLOR, BACKGROUND_TABLE_COLOR, get_width, get_height

def show_table(w: tk.Tk, column, row, columspan=1, padx=0, pady=0):
    container = tk.Frame(w, bg=BACKGROUND_COLOR, width=get_width(w))
    container.grid(column=column, row=row, columnspan=columspan, padx=padx, pady=pady, sticky="nsew")

    w.grid_rowconfigure(0, weight=1)
    w.grid_columnconfigure(0, weight=1)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    
    canvas = tk.Canvas(container, bg=BACKGROUND_COLOR, highlightthickness=0, width=get_width(container), height=766)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    frame_scrollable = tk.Frame(canvas, bg=BACKGROUND_TABLE_COLOR)
    window = canvas.create_window((0, 0), window=frame_scrollable, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas_width = event.width
        canvas.itemconfig(window, width=canvas_width, height=766)

    frame_scrollable.bind("<Configure>", on_frame_configure)

    def on_canvas_configure(event):
        canvas.itemconfig(window, width=event.width)

    canvas.bind("<Configure>", on_canvas_configure)

    return frame_scrollable