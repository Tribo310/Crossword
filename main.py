from tkinter import *

class CrosswordGame:
    def __init__(self, canvas, size=5):
        self.canvas = canvas
        self.size = size
        self.cells = {}
        self.entries = []  # List to keep track of the Entry widgets
        self.create_grid()
        self.create_ui()

    def create_grid(self):
        index_data = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]

        vcmd = (self.canvas.register(self.validate_input), '%P', '%W')

        for i, (row, col) in enumerate(index_data):
            entry = Entry(self.canvas, width=2, font=('Arial', 18), justify='center', validate='key', validatecommand=vcmd)
            entry.grid(row=row, column=col, padx=0, pady=0)
            self.cells[(row, col)] = entry
            self.entries.append(entry)

    def validate_input(self, P, widget_name):
        if len(P) <= 1:
            if len(P) == 1:
                self.move_to_next_widget(widget_name)
            return True
        return False

    def move_to_next_widget(self, widget_name):
        current_widget = self.canvas.nametowidget(widget_name)
        if current_widget in self.entries:
            current_index = self.entries.index(current_widget)
            if current_index + 1 < len(self.entries):
                self.entries[current_index + 1].focus_set()

    def create_ui(self):
        submit_button = Button(self.canvas, text='Submit', command=self.submit_button)
        submit_button.grid(row=6, column=1, columnspan=2, pady=10)
        clear_button = Button(self.canvas, text='Clear', command=self.clear_button)
        clear_button.grid(row=6, column=3, columnspan=2, pady=10)

    def submit_button(self, event=None):
        correct_data = ["t", "c", "a", "t", "b", "l", "e", "y", "e"]
        index_data = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]

        for i, (row, col) in enumerate(index_data):
            entry = self.cells[(row, col)]
            user_input = entry.get().lower()
            if user_input == correct_data[i]:
                entry.config(bg='green')
            else:
                entry.config(bg='red')

    def clear_button(self):
        for cell in self.cells.values():
            cell.delete(0, END)
            cell.config(bg='white')

    def move_cursor(self, row_delta, col_delta):
        current_widget = self.canvas.focus_get()
        if current_widget in self.entries:
            current_index = self.entries.index(current_widget)
            current_row, current_col = list(self.cells.keys())[current_index]

            new_row = current_row + row_delta
            new_col = current_col + col_delta

            if (new_row, new_col) in self.cells:
                self.cells[(new_row, new_col)].focus_set()

    def cursor_up(self, event):
        self.move_cursor(-1, 0)

    def cursor_down(self, event):
        self.move_cursor(1, 0)

    def cursor_left(self, event):
        self.move_cursor(0, -1)

    def cursor_right(self, event):
        self.move_cursor(0, 1)

if __name__ == "__main__":
    window = Tk()
    window.configure(bg='#8cbed6')
    window.geometry("500x500")  # Set the window size

    window.title("Crossword Game")  # Set the title of the main window

    # Create the title label with a background color and allow it to expand horizontally
    title_label = Label(window, text="Crossword Game", bg='white', font=45)
    title_label.pack(padx=0, pady=0, fill=BOTH)  # Pack the label into the window with padding set to 0

    canvas = Canvas(window, bg='#80daeb')
    canvas.pack(padx=0, pady=0, fill=BOTH)  # Pack the canvas into the window with padding set to 0

    explanation_label = Label(window, text="Босоо:\n1. table\nХэвтээ:\n1. cat\n2. eye", font=100)
    explanation_label.pack(fill=BOTH)

    game = CrosswordGame(canvas)

    # Bind the Enter key to the submit_button method
    window.bind('<Return>', game.submit_button)
    window.bind('<Up>', game.cursor_up)
    window.bind('<Down>', game.cursor_down)
    window.bind('<Left>', game.cursor_left)
    window.bind('<Right>', game.cursor_right)

    window.mainloop()
