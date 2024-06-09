from tkinter import *
from back_end import CrosswordGame

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
