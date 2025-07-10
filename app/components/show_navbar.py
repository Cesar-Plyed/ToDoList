import tkinter as tk

def show_navbar(w: tk.Tk, column, row, padx=0, pady=0):

    navbar = tk.Frame(w, bg="white")
    navbar.config(width=w.winfo_width())
    navbar.grid(column=column, row=row, padx=padx, pady=pady, sticky="nsew")
    navbar.grid_propagate(False)
    
    w.grid_rowconfigure(0, weight=1)
    w.grid_columnconfigure(0, weight=1)
    
    navbar.grid_columnconfigure(0, weight=1)
    navbar.grid_columnconfigure(1, weight=8)
    navbar.grid_columnconfigure(2, weight=1)

    logo = tk.Label(navbar, text="📝", bg="white", fg="black", font=("Arial", 19))
    logo.grid(row=0, column=0, sticky="w", padx=20, pady=10)

    title = tk.Label(navbar, text="ToDo List", bg="white", fg="black", font=("Arial", 22, "bold"))
    title.grid(row=0, column=1, sticky="w", padx=20, pady=8)

    config_btn = tk.Button(navbar, text="⚙️", bg="white", fg="black", borderwidth=0, font=("Arial", 16))
    config_btn.grid(row=0, column=2, sticky="e", padx=20, pady=10)
    
    return navbar