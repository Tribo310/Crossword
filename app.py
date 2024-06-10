from tkinter import *
from back_end import *
from crossword_data import *
from tkinter import messagebox

if __name__ == "__main__":
    crossword_data1 = [
        ["t", "o", "g", "t", "u", "v", "s", "h", "i", "n", "h", "o", "a", "a", "m", "o", "o", "j", "i", "g", "k", "a", "b", "a", "a", "s", "k", "a", "a"],
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
    window.configure(bg='#8cbed6')
    window.geometry("500x500")  # Set the window size

    window.title("Crossword Game")  # Set the title of the main window

    # Create the title label with a background color and allow it to expand horizontally
    title_label = Label(window, text="Crossword Game", bg='white', font=('Arial', 24))
    title_label.pack(padx=0, pady=0, fill=BOTH)  # Pack the label into the window with padding set to 0

    canvas = Canvas(window, bg='#80daeb')
    canvas.pack(padx=0, pady=0, fill=BOTH)  # Pack the canvas into the window with padding set to 0

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

    # Button to open the second window
    second_window_button = Button(window, text="Open Second Window", command=open_second_window)
    second_window_button.pack(pady=20)

    window.mainloop()
