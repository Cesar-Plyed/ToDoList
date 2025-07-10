from tkinter import messagebox as mb, Tk, Label, Button, Frame

from app.components.show_table import show_table
from app.services.get_task_service import show_get_tasks
from ..components.show_navbar import show_navbar
from ..components.show_create_task import show_create_task
from ..resources.resources import get_height

def show_dashboard(w: Tk):
    for widget in w.winfo_children():
        widget.destroy()
        
    w.grid_rowconfigure(0, minsize=50, weight=0)   # navbar
    w.grid_rowconfigure(1, minsize=80, weight=0)   # create_task_labels
    w.grid_rowconfigure(2, minsize=80, weight=0)   # create_task
    w.grid_rowconfigure(3, minsize=80, weight=0)   # header_table
    w.grid_rowconfigure(4, minsize=(get_height(w) - (70 + 80*3)), weight=1)  # tabla principal

    show_navbar(w, 0, 0)
    table = show_table(w, 0, 4)
    show_create_task(w, table, 0, 1, rowspan=2)
    show_get_tasks(table)

    w.mainloop()