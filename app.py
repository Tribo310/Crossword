from tkinter import *
from back_end import *
from crossword_data import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import tkinter as tk
from tkinter import Tk, Label, Button, PhotoImage
from tkinter import ttk
from random import randint, choice

time_left = 60  
current_level_window = None
timer_label = None
timer_running = False
start_time = None
def submit_answers(window):
    print("Submitting answers...")
def switch_window(current_window, new_window_func):
    current_window.destroy()
    new_window_func()
def update_timer():
    global time_left, timer_label, current_level_window, timer_running
    if timer_running and time_left > 0:
        elapsed_time = time.time() - start_time
        remaining_time = time_left - int(elapsed_time)
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        if timer_label:
            timer_label.config(text=f"Time left: {minutes:02}:{seconds:02}")
        current_level_window.after(1000, update_timer)  # Update every second
    elif time_left <= 0:
        if timer_label:
            timer_label.config(text="Time's up!")  # Display message when time runs out

# Function to start the welcome window
def start_welcome_window():
    global current_level_window
    welcome_window = Tk()
    welcome_window.geometry("900x900")

    original_image = Image.open('images/image1.jpg')
    resized_image = original_image.resize((900, 900), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)

    background_label = Label(welcome_window, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    clock_label = Label(welcome_window, text="", font=('Arial', 20), bg='#cfe2f3', fg='black')
    clock_label.pack(pady=20)

    start_button = Button(welcome_window, text="Start Game", font=('Arial', 30),  bg='#020f12', fg='#05d7ff', command=lambda: switch_window(welcome_window, start_choice_level_window))
    start_button.pack(pady=300)

    

    def update_clock():
        current_time = time.strftime("%H:%M:%S")
        clock_label.config(text=current_time)
        welcome_window.after(1000, update_clock)  # Update the clock every second
    
    update_clock()
    current_level_window = welcome_window
    welcome_window.mainloop()

# Function to start the choice level window
def start_choice_level_window():
    global current_level_window
    choice_level_window = Tk()
    choice_level_window.geometry("900x900")
    choice_level_window.title("Choose Level")
    original_image = Image.open('images/image3.jpg')
    resized_image = original_image.resize((900, 900), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)

    background_label = Label(choice_level_window, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(choice_level_window, text="Choose a Level", font=('Arial', 35)).pack(pady=50)
    
    Button(choice_level_window, text="Level 1", font=('Arial', 20), command=lambda: switch_window(choice_level_window, start_level_1_window)).pack(pady=50)
    Button(choice_level_window, text="Level 2", font=('Arial', 20), command=lambda: switch_window(choice_level_window, start_level_2_window)).pack(pady=50)
    Button(choice_level_window, text="Level 3", font=('Arial', 20), command=lambda: switch_window(choice_level_window, start_level_3_window)).pack(pady=50)
    Button(choice_level_window, text="Exit", font=('Arial', 20), command=lambda: switch_window(choice_level_window, start_end_game_window)).pack(pady=100)

    current_level_window = choice_level_window
    choice_level_window.mainloop()

# Function to start the level 1 window
def start_level_1_window():
    global current_level_window, timer_label, timer_running, time_left, start_time
    level_1_window = Tk()
    level_1_window.geometry("900x900")
    level_1_window.title("Level 1")

    Label(level_1_window, text="Level 1", font=('Arial', 24)).pack(pady=20)

    level1_data=[
        ["c", "o", "n", "t", "r", "o", "l", "p", "a", "n", "e", "l", 
        "p", "a", "i", "n", "t", 
        "s", "p", "o", "o", "l", "e", "r",
         "t", "e", "r", "m", "i", "n", "a", "l", 
         "c", "a", "l", "e", "n", "d", "a", "r",
         "n", "o", "t", "e", "p", "a", "d", 
         "c", "a", "l", "c", "u", "l", "a", "t", "o", "r",
         "c", "l", "o", "c", "k", 
         "r", "e", "v", "e", "r", "s", "i",
         "c", "a", "r", "d", "f", "i", "l", "e", 
         "w", "r", "i", "t", "e"],
        [[2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9], [10, 9], [11, 9], [12, 9], [13, 9], 
        [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], 
        [7, 7], [7, 8], [7, 9], [7, 10],[7, 11], [7, 12], [7, 13],
         [8, 14], [9, 14], [10, 14], [11, 14], [12, 14], [13, 14], [14, 14], [15, 14], 
         [9, 4], [10, 4], [11, 4], [12, 4], [13, 4], [14, 4], [15, 4], [16, 4], 
         [9, 11], [10, 11], [11, 11], [12, 11], [13, 11], [14, 11], [15, 11], 
         [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10], [10, 11], [10, 12],
         [10, 6], [11, 6], [12, 6], [13, 6], [14, 6], 
         [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [12, 13], [12, 14],
         [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [15, 15], 
         [17, 9], [17, 10], [17, 11], [17, 12], [17, 13]],
         "Across:\n2. What raster graphics editor?\n3. What programm used to print on computers?\n7. What desktop calculator app?\n9. What game is known as Othello?\n10. What contacts manager?\n11. What word processing programm? \nDown: \n1. What app used to change settings?\n4. What app used to control devices?\n5. What calendaring app?\n6. What text editor?"
         ]
    timer_label = Label(level_1_window, text="", font=('Arial', 20))
    timer_label.pack(pady=20)
    time_left = 60 
    timer_running = True
    start_time = time.time()
    update_timer()
    
    frame = Frame(level_1_window, bg='#8cbed6')
    frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
    canvas = Canvas(frame, bg='#80daeb')
    canvas.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=True)
    text_data = level1_data[2]
    explanation_text = Text(frame, wrap=WORD, font=('Arial', 12))
    explanation_text.insert(END, text_data)
    explanation_text.pack(side=RIGHT, padx=10, pady=10, fill=BOTH, expand=True)
    #
    
    game = CrosswordGame(canvas, level1_data)


    level_1_window.bind('<Return>', game.submit_button)
    level_1_window.bind('<Up>', game.cursor_up)
    level_1_window.bind('<Down>', game.cursor_down)
    level_1_window.bind('<Left>', game.cursor_left)
    level_1_window.bind('<Right>', game.cursor_right)
    level_1_window.bind('<BackSpace>', game.cursor_move)

    Button(level_1_window, text="Submit", font=('Arial', 20), command=lambda: submit_answers(level_1_window)).pack(pady=10)
    Button(level_1_window, text="End Game", font=('Arial', 20), command=lambda: switch_window(level_1_window, start_end_game_window)).pack(pady=10)
    
    current_level_window = level_1_window
    level_1_window.mainloop()

def scroll_horizontal(event):
    global canvas
    if event.state & 0x1:  # Check if Shift key is pressed
        canvas.xview_scroll(-int(event.delta / 60), "units")



def submit_answers(window):
    global timer_running
    # Implement your submit logic here
    timer_running = False  # Stop the timer

    # Optionally, display final time taken
    final_time = time.time() - start_time
    minutes = int(final_time) // 60
    seconds = int(final_time) % 60
    messagebox.showinfo("Submission", f"Time taken: {minutes} minutes {seconds} seconds")


# Function to start the level 2 window
def start_level_2_window():
    global current_level_window, timer_label, timer_running, time_left, start_time
    level_2_window = Tk()
    level_2_window.geometry("900x900")
    level_2_window.title("Level 2")

    Label(level_2_window, text="Level 2", font=('Arial', 24)).pack(pady=20)
    # Add level 2 game logic here
    level2_data = [
        ["c", "o", "n", "d", "i", "t", "i", "o", "n", "a", "l", "s", "t", "a", "t", "e", "m", "e", "n", "t", 
         "i", "t", "e", "r", "a", "t", "i", "n", "g",
         "l", "o", "o", "p", "i", "n", "g",
         "f", "u", "n", "c", "t", "i", "o", "n", 
         "c", "o", "d", "i", "n", "g", 
         "o", "u", "t", "p", "u", "t", 
         "i", "n", "p", "u", "t", 
         "a", "l", "g", "o", "r", "i", "t", "h", "m",
         "d", "e", "b", "u", "g", 
         "v", "a", "r", "i", "a", "b", "l", "e",
         "b", "u", "g"],
        [[7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [7, 15], [7, 16], [7, 17], [7, 18], [7, 19], [7, 20],
         [10, 8], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13], [10, 14], [10, 15], [10, 16],
         [14, 3], [14, 4], [14, 5], [14, 6], [14, 7], [14, 8], [14, 9],
         [3, 15], [4, 15], [5, 15], [6, 15], [7, 15], [8, 15], [9, 15], [10, 15],
         [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7],
         [5, 13], [6, 13], [7, 13], [8, 13], [9, 13], [10, 13],
         [6, 9], [7, 9], [8, 9], [9, 9], [10, 9],
         [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [11, 11], [12, 11], [13, 11], [14, 11],
         [7, 4], [8, 4], [9, 4], [10, 4], [11, 4],
         [11, 7], [12, 7], [13, 7], [14, 7], [15, 7], [16, 7], [17, 7], [18, 7],
         [12, 9], [13, 9], [14, 9]
         ],
         "Across:\n6. Look at an unknown variable and decide what to do \n8. Refining and improving your code \n11. Repeating sections of code or functions \nDown: \n1. A mini-code or computer program with directions \n2. Lines of instruction for the computer \n3. What the computer does \n4. Putting Information in a computer \n5. Step by step, ordered directions \n7. Finding and fixing a mistake in code \n9. Something that is unknown \n10. Mistake in code"
    ]

    timer_label = Label(level_2_window, text="", font=('Arial', 20))
    timer_label.pack(pady=20)
    time_left = 60  # Reset time for each level
    timer_running = True
    start_time = time.time()
    update_timer()
    frame = Frame(level_2_window, bg='#8cbed6')
    frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
    canvas = Canvas(frame, bg='#80daeb')
    canvas.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=True)
    text_data = level2_data[2]
    explanation_text = Text(frame, wrap=WORD, font=('Arial', 12))
    explanation_text.insert(END, text_data)
    explanation_text.pack(side=RIGHT, padx=10, pady=10, fill=BOTH, expand=True)
    
    game = CrosswordGame(canvas, level2_data)

    level_2_window.bind('<Return>', game.submit_button)
    level_2_window.bind('<Up>', game.cursor_up)
    level_2_window.bind('<Down>', game.cursor_down)
    level_2_window.bind('<Left>', game.cursor_left)
    level_2_window.bind('<Right>', game.cursor_right)
    level_2_window.bind('<BackSpace>', game.cursor_move)

    Button(level_2_window, text="Submit", font=('Arial', 20), command=lambda: submit_answers(level_2_window)).pack(pady=10)
    Button(level_2_window, text="End Game", font=('Arial', 20), command=lambda: switch_window(level_2_window, start_end_game_window)).pack(pady=10)

    current_level_window = level_2_window
    level_2_window.mainloop()

# Function to start the level 3 window
def start_level_3_window():
    global current_level_window, timer_label, timer_running, time_left, start_time
    level_3_window = Tk()
    level_3_window.geometry("900x900")
    level_3_window.title("Level 3")

    Label(level_3_window, text="Level 3", font=('Arial', 24)).pack(pady=20)
    # Add level 3 game logic here
    level3_data = [
        ["i", "n", "t", "e", "r", "n", "e", "t", 
        "c", "r", "y", "p", "t", "o", "g", "r", "a", "p", "h", "y", 
        "i", "n", "t", "e", "r", "p", "r", "e", "t", "e", "r",
         "a", "t", "o", "m", 
         "j", "a", "v", "a", "s", "c", "r", "i", "p", "t",
         "c", "o", "m", "p", "u", "t", "e", "r", 
         "z", "e", "d", "s", "h", "a", "w", 
         "c", "o", "m", "p", "i", "l", "e", "r", 
         "p", "r", "o", "t", "o", "c", "o", "l",
         "l", "i", "n", "u", "x", 
         "a", "s", "s", "e", "m", "b", "l", "y",
         "d", "j", "i", "k", "s", "t", "r", "a", 
         "n", "e", "w", "l", "i", "n", "e", 
         "p", "r", "o", "g", "r", "a", "m", 
         "s", "t", "r", "o", "u", "s", "t", "r", "u", "p"],
        [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], 
        [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [11, 11], [12, 11], [13, 11], [14, 11], 
        [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10],[5, 11], 
        [5, 13], [6, 13], [7, 13], [8, 13], 
        [5, 20], [6, 20], [7, 20], [8, 20], [9, 20], [10, 20], [11, 20], [12, 20], [13, 20], [14, 20],
        [6, 15], [7, 15], [8, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15],
        [7, 3], [8, 3], [9, 3], [10, 3], [11, 3], [12, 3], [13, 3],
        [7, 7], [8, 7], [9, 7], [10, 7], [11, 7], [12, 7], [13, 7], [14, 7],
        [7, 11], [7, 12], [7, 13], [7, 14], [7, 15], [7, 16], [7, 17], [7, 18], 
        [7, 18], [8, 18], [9, 18], [10, 18], [11, 18], 
        [9, 9], [10, 9], [11, 9], [12, 9], [13, 9], [14, 9], [15, 9], [16, 9], 
        [11, 5], [11, 5], [11, 7], [11, 8], [11, 9], [11, 10], [11, 11], [11, 12],
        [13, 1], [13, 2], [13, 3], [13, 4], [13, 5], [13, 6], [13, 7],
        [13, 11], [13, 12], [13, 13], [13, 14], [13, 15], [13, 16], [13,17],
        [18, 6], [18, 7], [18, 8], [18, 9], [18, 10], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15]
         ],
         "Across:\n3. This is used in an IDE.\n9. The P in IP stands for .....\n12. Don't read about this guy.\n13. Backslash-n is used for ....\n14. This is another name for code.\n15. Creator of C++.\nDown:\n1. This is a root.\n2. This is the study of security.\n4. An optimized text editor.\n5. A language that goes with the web.\n6. You download things here.\n7. LPTHW's author.\n8. Something you need for C.\n10. This will be a good brand.\n11. A basic language."
         ]



    timer_label = Label(level_3_window, text="", font=('Arial', 20))
    timer_label.pack(pady=20)
    time_left = 60  
    timer_running = True
    start_time = time.time()
    update_timer()
    frame = Frame(level_3_window, bg='#8cbed6')
    frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
    canvas = Canvas(frame, bg='#80daeb')
    canvas.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=True)
    text_data = level3_data[2]
    explanation_text = Text(frame, wrap=WORD, font=('Arial', 12))
    explanation_text.insert(END, text_data)
    explanation_text.pack(side=RIGHT, padx=10, pady=10, fill=BOTH, expand=True)
    
    game = CrosswordGame(canvas, level3_data)

    level_3_window.bind('<Return>', game.submit_button)
    level_3_window.bind('<Up>', game.cursor_up)
    level_3_window.bind('<Down>', game.cursor_down)
    level_3_window.bind('<Left>', game.cursor_left)
    level_3_window.bind('<Right>', game.cursor_right)
    level_3_window.bind('<BackSpace>', game.cursor_move)

    Button(level_3_window, text="Submit", font=('Arial', 20), command=lambda: submit_answers(level_3_window)).pack(pady=10)
    Button(level_3_window, text="End Game", font=('Arial', 20), command=lambda: switch_window(level_3_window, start_end_game_window)).pack(pady=10)

    current_level_window = level_3_window
    level_3_window.mainloop()

# Function to start the end game window
def start_end_game_window():
    global current_level_window
    end_game_window = Tk()
    end_game_window.geometry("900x900")
    end_game_window.title("End Game")

    original_image = Image.open('images/image2.png')
    resized_image = original_image.resize((900, 900), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)

    background_label = Label(end_game_window, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    Label(end_game_window, text="End of Game", font=('Arial', 35)).pack(pady=50)
    Button(end_game_window, text="Try again...", font=('Arial', 30), command=lambda: switch_window(end_game_window, start_choice_level_window)).pack(pady=100)
    # Add end game logic here

    current_level_window = end_game_window
    end_game_window.mainloop()

# Start the welcome window
start_welcome_window()