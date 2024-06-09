from tkinter import *


class CrosswordGame:
    def __init__(self, canvas, size=5):
        self.canvas = canvas
        self.size = size
        self.cells = {}
        self.create_grid()
        self.create_ui()

    def create_grid(self):
        # Assuming correct_data.index_data is a list of lists containing row and column indices
        index_data = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]

        for i, (row, col) in enumerate(index_data):
            entry = Entry(self.canvas, width=2, font=('Arial', 18), justify='center')
            entry.grid(row=row, column=col, padx=0, pady=0)
            self.cells[(row, col)] = entry

    def create_ui(self):
        submit_button = Button(self.canvas, text='Submit', command=self.submit_button)
        submit_button.grid(row=6, column=1, columnspan=2, pady=10)
        clear_button = Button(self.canvas, text='Clear', command=self.clear_button)
        clear_button.grid(row=6, column=3, columnspan=2, pady=10)

    def submit_button(self):
        correct_data = ["t", "c", "a", "t", "b", "l", "e", "g", "e"]
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


if __name__ == "__main__":
    window = Tk()
    window.configure(bg='#8cbed6')  # Set the background color of the window

    window.title("Crossword Game")  # Set the title of the main window

    # Create the title label with a background color and allow it to expand horizontally
    title_label = Label(window, text="Crossword Game", bg='white', width=100)
    title_label.pack(padx=0, pady=0)  # Pack the label into the window with padding set to 0

    canvas = Canvas(window, width=500, height=500, bg='#80daeb')
    canvas.pack(padx=0, pady=0)  # Pack the canvas into the window with padding set to 0

    game = CrosswordGame(canvas)

    window.mainloop()