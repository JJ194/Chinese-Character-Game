import tkinter as tk
import random
import time

# List of Chinese characters and correlating English word (simple characters)
flashcards = [
    {"chinese": "我", "english": "I"},
    {"chinese": "你", "english": "You"},
    {"chinese": "人", "english": "Person"},
    {"chinese": "日", "english": "Day/Sun"},
    {"chinese": "木", "english": "Tree"},
    {"chinese": "了", "english": "Past tense"},
    {"chinese": "金", "english": "Gold"},
    {"chinese": "水", "english": "Water"},
    {"chinese": "月", "english": "Moon or Month"},
    {"chinese": "山", "english": "Mountain"}
]

# Main window
root = tk.Tk()#creates main window
root.title("Chinese hanzi Game") #set the title for game
root.geometry("750x500") #set window size

# Game state
current_flashcard = None

def start_game():
    show_flashcard()

def show_flashcard():
    global current_flashcard

    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # Randomly pick a flashcard
    current_flashcard = random.choice(flashcards)

    # Shuffle the options (one correct, three random)
    options = [current_flashcard["english"]]
    while len(options) < 4:
        random_word = random.choice(flashcards)["english"]
        if random_word not in options:
            options.append(random_word)
    random.shuffle(options)

    # Display Chinese character
    chinese_label = tk.Label(root, text=current_flashcard["chinese"], font=("Arial", 50))
    chinese_label.pack(pady=20)

    # Display options
    for option in options:
        option_button = tk.Button(root, text=option, font=("Arial", 14), command=lambda opt=option: check_answer(opt))
        option_button.pack(pady=5)

def check_answer(selected_option):
    if selected_option == current_flashcard["english"]:
        display_feedback("green", True)
    else:
        display_feedback("red", False)

def display_feedback(color, is_correct):
    # Temporarily change background color to green or red
    root.configure(bg=color)
    root.update()
    time.sleep(1)

    # Reset background color
    root.configure(bg="white")
    
    if is_correct:
        show_continue_menu()
    else:
        show_correct_answer()

def show_correct_answer():
    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # Display red background and correct answer
    root.configure(bg="red")
    correct_label = tk.Label(root, text=f"The correct answer is: {current_flashcard['english']}", font=("Arial", 18), fg="white", bg="red")
    correct_label.pack(pady=20)
    root.update()
    time.sleep(1)

    root.configure(bg="white")
    show_continue_menu()

def show_continue_menu():
    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # Ask if the user wants to continue or go to main menu
    question_label = tk.Label(root, text="Do you want to continue?", font=("Arial", 18))
    question_label.pack(pady=20)

    continue_button = tk.Button(root, text="Continue", font=("Arial", 14), command=show_flashcard)
    continue_button.pack(pady=5)

    menu_button = tk.Button(root, text="Main Menu", font=("Arial", 14), command=main_menu)
    menu_button.pack(pady=5)

def main_menu():
    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # Display main menu
    start_button = tk.Button(root, text="Start", font=("Arial", 18), command=start_game)
    start_button.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", font=("Arial", 18), command=root.quit)
    exit_button.pack(pady=10)

# Start the game with the main menu
main_menu()

# Run the application
root.mainloop()