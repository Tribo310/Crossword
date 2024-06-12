
from tkinter import *
from back_end import *
from crossword_data import *
from tkinter import messagebox
from PIL import Image, ImageTk

def start_crossword_game():
    welcome_window.destroy()  # Close the welcome window
    show_crossword_game()     # Show the crossword game window
welcome_window = Tk()
welcome_window.geometry("900x900")
welcome_window.state('zoomed')

#welcome_window.title("Welcome to Crossword Game")
#welcome_window.configure(bg='#cfe2f3')

#welcome_label = Label(welcome_window, text="Welcome to Crossword Game!", font=('Arial', 30))
#welcome_label.pack(pady=200)

original_image = Image.open('images/image1.jpg')
resized_image = original_image.resize((900, 900), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(resized_image)

# Create a label to display the background image
background_label = Label(welcome_window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

start_button = Button(welcome_window, text="Start Game", font=('Arial', 20), command=start_crossword_game)
start_button.pack(pady=380)
start_button.pack()

welcome_window.mainloop()

if __name__ == "__main__":
    level1_data = [
        ["t", "c", "a", "t", "b", "l", "e", "y", "e"],
    [[0, 1],
     [1, 0], [1, 1], [1, 2],
     [2, 1],
     [3, 1],
     [4, 1], [4, 2], [4, 3]],
         "Across:\n6. Look at an unknown variable and decide what to do \n8. Refining and improving your code \n11. Repeating sections of code or functions \nDown: \n1. A mini-code or computer program with directions \n2. Lines of instruction for the computer \n3. What the computer does \n4. Putting Information in a computer \n5. Step by step, ordered directions \n7. Finding and fixing a mistake in code \n9. Something that is unknown \n10. Mistake in code"
    ]

    window = Tk()
    window.configure(bg='#8cbed6')
    window.geometry("900x900")
    window.state('zoomed')

    window.title("Crossword Game") 

    title_label = Label(window, text="Crossword Game", bg='white', font=('Arial', 24))
    title_label.pack(padx=0, pady=0, fill=BOTH)

    level_label = Label(window, text="Level 1", bg='#8cbed6', font=('Arial', 16, 'bold'))
    level_label.pack(side=TOP, padx=10, pady=10, anchor=NW)

    canvas = Canvas(window, bg='#80daeb')
    canvas.pack(padx=0, pady=0, fill=BOTH)

    frame = Frame(window, bg='#8cbed6')
    frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

    text_data = level1_data[2]
    explanation_text = Text(frame, wrap=WORD, font=('Arial', 12))
    explanation_text.insert(END, text_data)
    explanation_text.pack(side=RIGHT, padx=10, pady=10, fill=BOTH, expand=True)

    game = CrosswordGame(canvas, level1_data)

    window.bind('<Return>', game.submit_button)
    window.bind('<Up>', game.cursor_up)
    window.bind('<Down>', game.cursor_down)
    window.bind('<Left>', game.cursor_left)
    window.bind('<Right>', game.cursor_right)
    window.bind('<BackSpace>', game.cursor_move)


    second_window_button = Button(window, text="Open Second Window", command=open_second_window)
    second_window_button.pack(pady=20)

    window.mainloop()