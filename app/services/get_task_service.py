from ..components.show_table import show_table
from ..db.operations import get_tasks, delete_task, update_sussesful_task
from ..resources.resources import TEXT_FONT, BACKGROUND_TABLE_COLOR, BACKGROUND_DELETE_BUTTON, LABEL_TABLE_COLOR, BUTTON_TEXT_COLOR, BACKGROUND_EDIT_BUTTON
from tkinter import Label, Button, Frame

def show_get_tasks(place: Frame):
    table = show_table(place, 1, 3, columspan=4, padx=4, pady=4)
    
    columns = ["Tarea", "desde", "hasta", "","opciones"]

    for i, column in enumerate(columns):
        table.columnconfigure(i, weight=1, minsize=100)
        Label(table, text=column, font=TEXT_FONT, bg=BACKGROUND_TABLE_COLOR, fg=LABEL_TABLE_COLOR).grid(row=0, column=i, sticky="nsew", padx=10, pady=5)

    tasks = get_tasks()

    Frame(table, height=2, bg="gray").grid(row=1, column=0, columnspan=5, sticky="ew")

    for i, task in enumerate(tasks, 1):
        Label(table, text=task[1], font=TEXT_FONT, bg=BACKGROUND_TABLE_COLOR, fg=LABEL_TABLE_COLOR).grid(row=i+1, column=0, sticky="news", padx=10, pady=5)
        Label(table, text=task[2], font=TEXT_FONT, bg=BACKGROUND_TABLE_COLOR, fg=LABEL_TABLE_COLOR).grid(row=i+1, column=1, sticky="news", padx=10, pady=5)
        Label(table, text=task[3], font=TEXT_FONT, bg=BACKGROUND_TABLE_COLOR, fg=LABEL_TABLE_COLOR).grid(row=i+1, column=2, sticky="news", padx=10, pady=5)
        Label(table, text="✔️" if task[4] else "❌", font=TEXT_FONT, bg=BACKGROUND_TABLE_COLOR, fg=LABEL_TABLE_COLOR, width=10).grid(row=i+1, column=3, sticky="", padx=10, pady=5)

        eliminarBtn = Button(table, text="❌", font=TEXT_FONT, bg=BACKGROUND_DELETE_BUTTON, fg=BUTTON_TEXT_COLOR, width=2, border=0, command=lambda task_id=task[0]: delete_task(task_id) and upd_table(place))
        eliminarBtn.grid(column=4, row=i+1, sticky="e", pady=1, padx=100, ipadx=5)
        eliminarBtn.grid_propagate(False)
        markBtn = Button(table, text="✔️", font=TEXT_FONT, bg=BACKGROUND_EDIT_BUTTON, fg=BUTTON_TEXT_COLOR, width=2, border=0, command=lambda task_id=task[0]: update_sussesful_task(task_id) and upd_table(place))
        markBtn.grid(column=4, row=i+1, sticky="w", pady=1, padx=100, ipadx=5)
        markBtn.grid_propagate(False)

def upd_table(place: Frame):
    for widget in place.winfo_children():
        widget.destroy()
    show_get_tasks(place)