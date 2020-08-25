import tkinter as tk
from tkinter import ttk


class TkMenu:
    def __init__(self, mSettings, master=tk.Tk()):
        self.mSettings = mSettings
        self.master = master  # The Tkinter instance.

        # The delay that will be applied to Tkinter using the self.enable_button() method.
        self.delay = 100

        self.master.title("Maze Generator")  # Title of the window.

        self.num_of_cols = tk.StringVar()  # Variable for future entry object value.
        self.num_of_rows = tk.StringVar()  # Variable for future entry object value.
        self.info_label_text = tk.StringVar()  # Variable for future label object value.
        self.cell_size = tk.StringVar()  # Variable for future entry object value.
        self.suggested_text_val = tk.StringVar()  # Variable for future label object.

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
        # self.validation_text = ttk.Label(self.frame_1, textvariable=self.info_label_text, wraplength=150)
        self.validation_text = ttk.Label(self.frame_1, textvariable=self.info_label_text, wraplength=225)

        # Create a label object within frame_1 with value the same as suggested_text_val.
        self.suggestion_label = ttk.Label(self.frame_1, textvariable=self.suggested_text_val)

        # Create an entry object with the value of the num_of_cols variable.
        # self.rows_entry = ttk.Entry(self.frame_1, width=1, textvariable=self.num_of_cols)
        self.rows_entry = ttk.Entry(self.frame_1, width=5, textvariable=self.num_of_cols)
        # Create an entry object with the value of the num_of_rows variable.
        # self.cols_entry = ttk.Entry(self.frame_1, width=1, textvariable=self.num_of_rows)
        self.cols_entry = ttk.Entry(self.frame_1, width=5, textvariable=self.num_of_rows)
        # Create an entry object with the value of the cell_size variable.
        # self.cell_size_entry = ttk.Entry(self.frame_1, width=1, textvariable=self.cell_size)
        self.cell_size_entry = ttk.Entry(self.frame_1, width=5, textvariable=self.cell_size)

        # Create the button object bind to the method generate().
        self.gene_butt = ttk.Button(self.frame_1, text="Generate", command=self.generate)

        # Griding:
        self.frame_1.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # self.title_text.grid(column=0, row=0, pady=15, columnspan=4)
        self.title_text.grid(column=0, row=0, pady=15, columnspan=7)
        # self.validation_text.grid(column=2, row=1, rowspan=2, padx=20)
        self.validation_text.grid(column=3, columnspan=3, row=1, rowspan=3, padx=[10, 0],
                                  sticky=(tk.W, tk.N, tk.W, tk.S))

        self.suggestion_label.grid(column=1, columnspan=2, row=4, sticky=(tk.W, tk.E), padx=[13, 0], pady=3)

        self.nums_rows_text.grid(column=0, row=1, sticky=tk.W)
        self.nums_cols_text.grid(column=0, row=2, sticky=tk.W)
        self.cell_size_text.grid(column=0, row=3, sticky=tk.W)

        self.rows_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=[15, 0])
        self.cols_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=[15, 0])
        self.cell_size_entry.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=[15, 0], pady=[3, 0])

        self.gene_butt.grid(column=6, row=1)

        # Column & Row configure:
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame_1.columnconfigure(1, weight=3)
        self.frame_1.columnconfigure(2, weight=3)
        self.frame_1.columnconfigure(3, weight=3)
        self.frame_1.columnconfigure(4, weight=3)
        self.frame_1.columnconfigure(5, weight=3)

        self.frame_1.rowconfigure(0, weight=1)
        self.frame_1.rowconfigure(1, weight=1)
        self.frame_1.rowconfigure(2, weight=1)
        self.frame_1.rowconfigure(3, weight=1)
        self.frame_1.rowconfigure(4, weight=1)

        # Bindings:
        self.rows_entry.bind("<Return>", self.generate)
        self.cols_entry.bind("<Return>", self.generate)
        self.cell_size_entry.bind("<Return>", self.generate)
        if self.gene_butt.cget("state") == "normal":
            self.gene_butt.bind("<1>", self.generate)
            self.gene_butt.bind("<Return>", self.generate)

        # Bind the event of the close button being press to the self.on_closing() method.
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Every self.delay milliseconds, apply the self.enable_button() method.
        self.master.after(self.delay, self.enable_button)

        # Set the minimum size of the Tkinter window.
        # self.master.minsize(548, 142)
        self.master.minsize(548, 163)

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

        self.suggested_text_val.set("")

        enable = False  # A flag that signals the enabling of the generation button.

        # If either of the values of the entries are ''
        if col_entry == '' or row_entry == '':
            self.info_label_text.set("")  # set validation message to ''.

        # Else if either of the entries as a non-numeric character
        elif not col_entry.isdigit() or not row_entry.isdigit():
            # display a message stating that only numeric characters should be entered.
            self.info_label_text.set("You must enter numbers only; no non-numeric characters.")

        # Else if the numbers for the columns and rows entries are outside of their bounds.
        elif not (2 <= int(col_entry) <= 31) or not (2 <= int(row_entry) <= 31):
            # display a message stating the condition.
            self.info_label_text.set(
                "The column and row numbers must be within a range of 2 to 31."
            )

        elif not self.validate_cell_size(col_entry, row_entry, cell_size_number):
            pass

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
            self.mSettings.cols, self.mSettings.rows = int(col_entry), int(row_entry)
            self.mSettings.size = int(cell_size_number)
        # Else
        else:
            # set the state of the generation button to disabled
            self.gene_butt.configure(state="disabled")

            # reset the value of the columns and rows and cell size
            self.mSettings.cols, self.mSettings.rows = None, None
            self.mSettings.size = None
        # Repeat this method after self.delay milliseconds.
        self.master.after(self.delay, self.enable_button)

    def validate_cell_size(self, col_nums, row_nums, cell_size_entry_val):
        self.info_label_text.set("")

        self.suggested_text_val.set(
            f"Suggested size: "
            f"{self.padding_func(max(int(col_nums), int(row_nums)))}")

        if not cell_size_entry_val.isdigit() and cell_size_entry_val != "":
            self.info_label_text.set("Cell size can't be a non-numeric character.")
        elif cell_size_entry_val != "" and not (10 <= int(cell_size_entry_val) <= 150):
            self.info_label_text.set("Cell size must be a number between 10 and 150 inclusively.")
        else:
            if cell_size_entry_val.isdigit():
                return True
        return False

    def on_closing(self):
        # If the close button is pressed (x button at the top-right corner),
        # close the window.
        raise SystemExit

    def get_wind_size(self):
        return self.master.winfo_width(), self.master.winfo_height()

    def padding_func(self, cols_or_rows):
        return int(round(161.89079 * 0.9006 ** cols_or_rows + 18.69355))

    def loop(self):
        self.master.mainloop()


if __name__ == "__main__":
    pass
