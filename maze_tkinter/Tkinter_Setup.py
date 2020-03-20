import tkinter as tk
from tkinter import ttk
from config import Vars, Debugger, PygameVars as Pyv


class TkinterWindow:
    def __init__(self, master):
        self.master = master

        self.delay = 100

        # Tkinter setup:
        self.master.title("Maze Generator")

        self.num_of_cols = tk.StringVar()
        self.num_of_rows = tk.StringVar()
        self.info_label_text = tk.StringVar()
        self.cell_size = tk.StringVar()

        # Object creation:
        self.frame_1 = ttk.Frame(self.master, padding=(10, 10, 10, 10), width=400, height=400)

        self.title_text = ttk.Label(self.frame_1, text="Maze Generator", anchor="n")
        self.nums_rows_text = ttk.Label(self.frame_1, text="Number of columns:")
        self.nums_cols_text = ttk.Label(self.frame_1, text="Number of rows:")
        self.cell_size_text = ttk.Label(self.frame_1, text="Cell size:")
        self.filter_text = ttk.Label(self.frame_1, textvariable=self.info_label_text, wraplength=150)

        self.rows_entry = ttk.Entry(self.frame_1, width=2, textvariable=self.num_of_cols)
        self.cols_entry = ttk.Entry(self.frame_1, width=2, textvariable=self.num_of_rows)
        self.cell_size_entry = ttk.Entry(self.frame_1, width=2, textvariable=self.cell_size)

        self.gene_butt = ttk.Button(self.frame_1, text="Generate", command=self.generate)

        # Griding:
        self.frame_1.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.title_text.grid(column=0, row=0, pady=15, columnspan=4)
        self.filter_text.grid(column=2, row=1, rowspan=2, padx=20)

        self.nums_rows_text.grid(column=0, row=1, sticky=tk.W, padx=10)
        self.nums_cols_text.grid(column=0, row=2, sticky=tk.W, padx=10)
        self.cell_size_text.grid(column=0, row=3, sticky=tk.W, padx=10, pady=4)
        self.rows_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))
        self.cols_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))
        self.cell_size_entry.grid(column=1, row=3, sticky=(tk.W, tk.E))

        self.gene_butt.grid(column=3, row=1, sticky=tk.E)

        # Column & Row configure:
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # frame_1.columnconfigure(0, weight=1)
        self.frame_1.columnconfigure(1, weight=2)
        self.frame_1.columnconfigure(2, weight=3)
        self.frame_1.columnconfigure(3, weight=3)

        self.frame_1.rowconfigure(0, weight=1)
        self.frame_1.rowconfigure(1, weight=1)

        self.frame_1.rowconfigure(2, weight=1)
        self.frame_1.rowconfigure(3, weight=1)

        # Column & Row configure: Size
        self.master.columnconfigure(1, minsize=2)

        # Bindings:
        self.rows_entry.bind("<Return>", self.generate)
        self.cols_entry.bind("<Return>", self.generate)
        self.cell_size_entry.bind("<Return>", self.generate)
        if self.gene_butt.cget("state") == "normal":
            self.gene_butt.bind("<1>", self.generate)
            self.gene_butt.bind("<Return>", self.generate)

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Other settings:
        self.master.after(self.delay, self.enable_button)
        # self.master.minsize(456, 131)
        # self.master.maxsize(1200, 1200)
        self.master.minsize(500, 131)

    def generate(self, *args):
        if str(self.gene_butt.cget("state")) == "normal":
            # Vars.
            # = math.floor((Pyv.WIDTH - 2 * Vars.BORDER) / Vars.COLS)
            self.master.destroy()
        else:
            pass

    def enable_button(self):
        col_entry, row_entry = self.num_of_cols.get(), self.num_of_rows.get()
        cell_size_number = self.cell_size_entry.get()
        enable = True

        if col_entry == '' or row_entry == '' or cell_size_number == '':
            enable = False
            self.info_label_text.set("")
        elif not col_entry.isdigit() or not row_entry.isdigit() or not cell_size_number.isdigit():
            enable = False
            self.info_label_text.set("You must enter numbers only; no non-numeric characters.")

        elif not(2 <= int(col_entry)) or not(2 <= int(row_entry)) and not (10 <= int(cell_size_number) <= 150):
            enable = False
            self.info_label_text.set("The column and row numbers must be within a range of 2 to 31."
                                     "\nThe cell size must be an integer from 10 to 150 (inclusive).")

        elif not(2 <= int(col_entry)) or not(2 <= int(row_entry)):
            enable = False
            self.info_label_text.set("The column and row numbers must be within a range of 2 to 31.")
        elif not(10 <= int(cell_size_number) <= 150):
            enable = False
            self.info_label_text.set("The cell size must be an integer from 10 to 150 (inclusive).")

        self.gene_butt.configure(state="disabled")
        Vars.COLS, Vars.ROWS = None, None
        Vars.SIZE = None

        if enable:
            self.info_label_text.set("")
            self.gene_butt.configure(state="normal")
            Vars.COLS, Vars.ROWS = int(col_entry), int(row_entry)
            Vars.SIZE = int(cell_size_number)

        self.master.after(self.delay, self.enable_button)

    def on_closing(self):
        raise SystemExit


def start_loop():
    root = tk.Tk()
    TkinterWindow(root)
    root.mainloop()


if __name__ == "__main__":
    start_loop()
