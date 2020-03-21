import tkinter as tk
from tkinter import ttk
from config import Vars, Debugger, PygameVars as Pyv


class TkinterWindow:
    def __init__(self, master):
        self.master = master  # The Tkinter instance.

        # The delay that will be applied to Tkinter using the self.enable_button() method.
        self.delay = 100

        self.master.title("Maze Generator")  # Title of the window.

        self.num_of_cols = tk.StringVar()  # Variable for future entry object value.
        self.num_of_rows = tk.StringVar()  # Variable for future entry object value.
        self.info_label_text = tk.StringVar()  # Variable for future label object value.
        self.cell_size = tk.StringVar()  # Variable for future entry object value.

        # Create a frame object in master.
        self.frame_1 = ttk.Frame(self.master, padding=(10, 10, 10, 10), width=400, height=400)

        # Create a label object within frame_1 with value "Maze Generator".
        self.title_text = ttk.Label(self.frame_1, text="Maze Generator", anchor="n")
        # Create a label object within frame_1 with value "Number of columns:"
        self.nums_rows_text = ttk.Label(self.frame_1, text="Number of columns:")
        # Create a label object within frame_1 with value "Number of rows:"
        self.nums_cols_text = ttk.Label(self.frame_1, text="Number of rows:")
        # Create a label object within frame_1 with value "Cell size:".
        self.cell_size_text = ttk.Label(self.frame_1, text="Cell size:")
        # Create a label object within frame_1 with value the same as the info_label_text variable.
        self.filter_text = ttk.Label(self.frame_1, textvariable=self.info_label_text, wraplength=150)

        # Create an entry object with the value of the num_of_cols variable.
        self.rows_entry = ttk.Entry(self.frame_1, width=2, textvariable=self.num_of_cols)
        # Create an entry object with the value of the num_of_rows variable.
        self.cols_entry = ttk.Entry(self.frame_1, width=2, textvariable=self.num_of_rows)
        # Create an entry object with the value of the cell_size variable.
        self.cell_size_entry = ttk.Entry(self.frame_1, width=2, textvariable=self.cell_size)

        # Create the button object bind to the method generate().
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

        # Every self.delay milliseconds, apply the self.enable_button() method.
        self.master.after(self.delay, self.enable_button)
        # self.master.minsize(456, 131)
        # self.master.maxsize(1200, 1200)

        # Minimum size of the Tkinter window.
        self.master.minsize(500, 131)

    def generate(self, *args):
        # If the state of the generation button is normal and the button was pressed
        if str(self.gene_butt.cget("state")) == "normal":
            # Vars.
            # = math.floor((Pyv.WIDTH - 2 * Vars.BORDER) / Vars.COLS)
            self.master.destroy()  # kill the window.

    def enable_button(self):
        # Get the values of the entries and store them in the given variables.
        col_entry, row_entry = self.num_of_cols.get(), self.num_of_rows.get()
        cell_size_number = self.cell_size_entry.get()

        enable = False  # A flag that signals the enabling of the generation button.

        # If either of the values of the entries are ''
        if col_entry == '' or row_entry == '' or cell_size_number == '':
            self.info_label_text.set("")  # set filter message to ''.

        # Else if either of the entries as a non-numeric character
        elif not col_entry.isdigit() or not row_entry.isdigit() or not cell_size_number.isdigit():
            # display a message stating that only numeric characters should be entered.
            self.info_label_text.set("You must enter numbers only; no non-numeric characters.")
        # Else if all of the entries have numbers outside of their established ranges.
        elif not(2 <= int(col_entry)) or not(2 <= int(row_entry)) and not (10 <= int(cell_size_number) <= 150):
            # display a message stating the condition.
            self.info_label_text.set("The column and row numbers must be within a range of 2 to 31."
                                     "\nThe cell size must be an integer from 10 to 150 (inclusive).")
        # Else if the numbers for the columns and rows entries are outside of their bounds and the number
        # in the cell size entry is within bound.
        elif not(2 <= int(col_entry)) or not(2 <= int(row_entry)):
            # display a message stating the condition.
            self.info_label_text.set("The column and row numbers must be within a range of 2 to 31.")
        # Else if the numbers for the columns and rows entries are within bounds but not the number
        # of the cell size entry.
        elif not(10 <= int(cell_size_number) <= 150):
            # display a message stating the condition.
            self.info_label_text.set("The cell size must be an integer from 10 to 150 (inclusive).")
        # Else, this means that the entries passed all the validation tests
        else:
            # hence, clear the validation message as the entries met all of their conditions
            self.info_label_text.set("")
            enable = True  # and raise the flag to enable the button.

        # If enable is true
        if enable:
            # set the state of the generation button to normal
            self.gene_butt.configure(state="normal")

            # let the variables of rows, columns and cell size be equal to
            # the respective entry values.
            Vars.COLS, Vars.ROWS = int(col_entry), int(row_entry)
            Vars.SIZE = int(cell_size_number)
        # Else
        else:
            # set the state of the generation button to disabled
            self.gene_butt.configure(state="disabled")

            # reset the value of the columns and rows and cell size
            Vars.COLS, Vars.ROWS = None, None
            Vars.SIZE = None

        # Repeat this method after self.delay milliseconds.
        self.master.after(self.delay, self.enable_button)

    def on_closing(self):
        # If the close button is pressed (x button at the top-right corner),
        # close the window.
        raise SystemExit


def start_loop():
    root = tk.Tk()  # Create a Tk() object.
    TkinterWindow(root)  # Run the TkinterWindow class with the root as argument.
    root.mainloop()  # Start the Tk() loop.


if __name__ == "__main__":
    start_loop()
