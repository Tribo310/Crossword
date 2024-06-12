from tkinter import *
from PIL import Image, ImageTk
from random import choice


class CrosswordGame:
    def __init__(self, canvas, crossword_data):
        self.canvas = canvas
        self.correct_data = crossword_data[0]
        self.index_data = crossword_data[1]
        self.explanation_data = crossword_data[2]
        self.cells = {}
        self.entries = []  # List to keep track of the Entry widgets
        self.create_grid()
        self.create_ui()

    def create_grid(self):
        vcmd = (self.canvas.register(self.validate_input), '%P', '%W')

        for i, (row, col) in enumerate(self.index_data):
            entry = Entry(self.canvas, width=2, font=('Arial', 18), justify='center', validate='key',
                          validatecommand=vcmd)
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
        max_row = max(row for row, col in self.index_data)
        submit_button = Button(self.canvas, text='Submit', command=self.submit_button)
        submit_button.grid(row=max_row + 1, column=1, columnspan=2, pady=10)
        clear_button = Button(self.canvas, text='Clear', command=self.clear_button)
        clear_button.grid(row=max_row + 1, column=3, columnspan=2, pady=10)

    def submit_button(self, event=None):
        for i, (row, col) in enumerate(self.index_data):
            entry = self.cells[(row, col)]
            user_input = entry.get().lower()
            if user_input == self.correct_data[i]:
                entry.config(bg='green')
            else:
                entry.config(bg='red')

    def clear_button(self, event=None):
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

    def cursor_move(self, event):
        self.move_cursor(0, -1)


if __name__ == "__main__":
    crossword_data1 = [
        ["t", "o", "g", "t", "u", "v", "s", "h", "i", "n", "h", "o", "a", "a", "m", "o", "o", "j", "i", "g", "k", "a",
         "b", "a", "a", "s", "k", "a", "a"],
        [[1, 4],
         [2, 4],
         [3, 4],
         [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 10],
         [5, 4], [5, 7], [5, 10],
         [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12],
         [7, 7], [7, 10],
         [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 10]
         ],
        "Босоо:\n1. togso\n 2. namka\n 3. hajaa\nХэвтээ:\n1. tuvshin\n2. moojig\n 3. baaska"
    ]

    window = Tk()

    # Update the paths to the images
    background_images = [
        Image.open("C:/Users/monho/Desktop/pycharm/DadalgaPY/test_crossword/cover_image1.jpg"),
        Image.open("C:/Users/monho/Desktop/pycharm/DadalgaPY/test_crossword/cover_image2.jpg"),
        Image.open("C:/Users/monho/Desktop/pycharm/DadalgaPY/test_crossword/cover_image3.jpg")
    ]

    photo = ImageTk.PhotoImage(choice(background_images))
    bg_image = Label(window, image=photo)
    bg_image.image = photo  # Keep a reference to avoid garbage collection
    bg_image.pack(fill=BOTH, expand=YES)

    window.title("Crossword Game")  # Set the title of the main window

    # Create the title label with a background color and allow it to expand horizontally
    title_label = Label(window, text="Crossword Game", bg='white', font=('Arial', 24))
    title_label.pack(padx=0, pady=0, fill=BOTH)  # Pack the label into the window with padding set to 0

    canvas = Canvas(window, bg='#80daeb')
    canvas.pack(padx=0, pady=0, fill=BOTH, expand=YES)  # Pack the canvas into the window with padding set to 0

    text_data = crossword_data1[2]
    explanation_label = Label(window, text=text_data, font=('Arial', 16))
    explanation_label.pack(fill=BOTH)

    game = CrosswordGame(canvas, crossword_data1)

    # Bind the Enter key to the submit_button method
    window.bind('<Return>', game.submit_button)
    window.bind('<Up>', game.cursor_up)
    window.bind('<Down>', game.cursor_down)
    window.bind('<Left>', game.cursor_left)
    window.bind('<Right>', game.cursor_right)
    window.bind('<BackSpace>', game.cursor_move)

    window.mainloop()
