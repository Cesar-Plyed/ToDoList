import tkinter as tk
from tkcalendar import DateEntry
from ..services.create_task_service import create_task_service
from ..services.get_task_service import upd_table

def show_create_task(w: tk.Tk, place: tk.Frame, column, row, padx=0, pady=0, rowspan=1):

    createTask = tk.Frame(w, bg="white")
    createTask.config(width=w.winfo_width())
    createTask.grid(column=column, row=row, padx=padx, pady=pady, sticky="nsew", rowspan=rowspan)
    createTask.grid_propagate(False)
    
    w.grid_rowconfigure(0, weight=1)
    w.grid_columnconfigure(0, weight=6)
    createTask.grid_columnconfigure(0, weight=6)
    createTask.grid_columnconfigure(1, weight=3)
    createTask.grid_columnconfigure(2, weight=1)
    createTask.grid_columnconfigure(3, weight=1)
    createTask.grid_columnconfigure(4, weight=1)
    createTask.grid_rowconfigure(0, weight=1)
    createTask.grid_rowconfigure(1, weight=1, minsize=10)

    tk.Label(createTask, text="Crear tarea", bg="white", font=("Arial", 16)).grid(column=0, row=0, columnspan=3, pady=(10, 5), sticky="w")
    tk.Label(createTask, text="Desde:", bg="white", font=("Arial", 16)).grid(column=1, row=0, columnspan=3, pady=(10, 5), sticky="w")
    tk.Label(createTask, text="Hasta:", bg="white", font=("Arial", 16)).grid(column=2, row=0, columnspan=3, pady=(10, 5), sticky="w")
    
    task = tk.Entry(createTask, width=20, font=("Arial", 14), highlightcolor="green", highlightbackground="red", highlightthickness=1, border=0 )
    task.grid(column=0, row=1, padx=(10, 5), pady=(0, 10), sticky="we", ipadx=2)

    toDateEntry = DateEntry(createTask, width=20, font=("Arial", 14), highlightcolor="green", highlightbackground="red", highlightthickness=1, border=0, date_pattern='yyyy-mm-dd')
    toDateEntry.grid(column=1, row=1, padx=(5, 5), pady=(0, 10), sticky="we")
    fromDateEntry = DateEntry(createTask, width=20, font=("Arial", 14), highlightcolor="green", highlightbackground="red", highlightthickness=1, border=0, date_pattern='yyyy-mm-dd')
    fromDateEntry.grid(column=2, row=1, padx=(5, 10), pady=(0, 10), sticky="we")

    tk.Button(createTask, text="Vaciar campos", font=("Arial", 14), bg="#833131", fg="white", border=0, command=lambda: task.delete(0, tk.END)).grid(column=3, row=1, padx=(5, 10), pady=(0, 10), sticky="", ipadx=10)
    tk.Button(createTask, text="Crear tarea", font=("Arial", 14), bg="#4CAF50", fg="white", border=0, command=lambda: create_task_service(task.get(), toDateEntry.get(), fromDateEntry.get()) and upd_table(place)).grid(column=4, row=1, padx=(5, 10), pady=(0, 10), sticky="", ipadx=10)

    return createTask