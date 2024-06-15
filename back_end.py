
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import tkinter as tk
from tkinter import ttk

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

        # Create Entry widgets for the crossword grid
        for i, (row, col) in enumerate(self.index_data):
            entry = Entry(self.canvas, width=2, font=('Arial', 18), justify='center', validate='key', validatecommand=vcmd)
            entry.grid(row=row, column=col, padx=0, pady=0)
            self.cells[(row, col)] = entry
            self.entries.append(entry)

        # Add clue number labels to the grid
        clues1 = {
        (1, 9): "1.", (5, 4): "2.", (7, 6): "3.",
        (7, 14): "4.", (8, 4): "5.", (8, 11): "6.",
        (10, 2): "7.", (9, 6): "8.", (12, 7): "9.",
        (15, 7): "10.", (17, 8): "11."
    }

       

        for (row, col), text in clues1.items():
            if text:
                label = Label(self.canvas, text=text, font=('Arial', 12))
                label.grid(row=row, column=col, padx=0, pady=0)


        # Add clue number labels to the grid
        clues2 = {
        (2, 15): "1.", (3, 7): "2.", (4, 13): "3.",
        (5, 9): "4.", (5, 11): "5.", (7, 0): "6.",
        (6, 4): "7.", (10, 7): "8.", (11, 6): "9.",
        (11, 9): "10.", (14, 2): "11."
    }

       

        for (row, col), text in clues2.items():
            if text:
                label = Label(self.canvas, text=text, font=('Arial', 12))
                label.grid(row=row, column=col, padx=0, pady=0)
    
        # Add clue number labels to the grid
        clues3 = {
        (0, 5): "1.", (3, 11): "2.", (5, 0): "3.",
        (4, 13): "4.", (4, 20): "5.", (5, 15): "6.",
        (6, 3): "7.", (6, 7): "8.", (7, 10): "9.",
        (6, 18): "10.", (8, 9): "11.", (11, 4): "12.",
        (13, 0): "13.", (13, 10): "14.", (18, 5): "15."
    }

       

        for (row, col), text in clues3.items():
            if text:
                label = Label(self.canvas, text=text, font=('Arial', 12))
                label.grid(row=row, column=col, padx=0, pady=0)

    
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
        all_correct = True  # Flag to check if all entries are correct

        for i, (row, col) in enumerate(self.index_data):
            entry = self.cells[(row, col)]
            user_input = entry.get().lower()
            if user_input == self.correct_data[i]:
                entry.config(bg='green')
            else:
                entry.config(bg='red')
                all_correct = False

        if all_correct:
            messagebox.showinfo("Congratulations", "All entries are correct!")

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

    def cursor_move(self, event):
        self.move_cursor(0, -1)


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Crossword Game")
        self.master.geometry("400x300")
        label = Label(self.master, text="Welcome to the Crossword Game!")
        label.pack(pady=20)
        button_frame = Frame(self.master)
        button_frame.pack(pady=20)

        for i in range(1, 4):
            Button(button_frame, text=f"Start Level {i}", command=lambda i=i: self.start_game(i)).pack(side=LEFT, padx=10)

def start_game(self, level):
        level_data = {
            1: (level1_data, clues1),
            2: (level2_data, clues2),
            3: (level3_data, clues3),
        }
        
        if level not in level_data:
            messagebox.showerror("Error", "Level not available")
            return
        
        crossword_data, clues = level_data[level]
        
        game_window = Toplevel(self.master)
        game_window.geometry("900x900")
        game_window.title(f"Level {level}")
        
        game = CrosswordGame(game_window, crossword_data, clues)
        
        game_window.bind('<Return>', game.submit_button)
        game_window.bind('<Up>', game.cursor_up)
        game_window.bind('<Down>', game.cursor_down)
        game_window.bind('<Left>', game.cursor_left)
        game_window.bind('<Right>', game.cursor_right)
        game_window.bind('<BackSpace>', game.cursor_move)
        
        game_window.mainloop()

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "_main_":
    main() 