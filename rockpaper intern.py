import random
import tkinter as tk

# Define the choices and their corresponding symbols
choices = ['rock', 'paper', 'scissors']
symbols = {
    'rock': '✊',
    'paper': '✋',
    'scissors': '✌️'
}

# Initialize scores
user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score

    # Generate computer choice
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
        result_color = "black"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        result_color = "green"
        user_score += 1
    else:
        result = "You lose!"
        result_color = "red"
        computer_score += 1

    # Update the result and score labels
    result_label.config(text=f"User: {symbols[user_choice]} | Computer: {symbols[computer_choice]} | {result}", fg=result_color)
    score_label.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")

def play_again():
    result_label.config(text="")
    score_label.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")

# Set up the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg='#f0f0f0')  # Light grey background

# Create and place the widgets
title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg='#f0f0f0', font=("Helvetica", 16))
title_label.pack(pady=5)

# Buttons for user choices
button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock ✊", command=lambda: play_game('rock'), bg='#4CAF50', fg='white', font=("Helvetica", 14), width=10)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper ✋", command=lambda: play_game('paper'), bg='#2196F3', fg='white', font=("Helvetica", 14), width=10)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors ✌️", command=lambda: play_game('scissors'), bg='#FF5722', fg='white', font=("Helvetica", 14), width=10)
scissors_button.grid(row=0, column=2, padx=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg='#f0f0f0')
result_label.pack(pady=10)

# Label to display the score
score_label = tk.Label(root, text=f"User Score: {user_score} | Computer Score: {computer_score}", font=("Helvetica", 14), bg='#f0f0f0')
score_label.pack(pady=5)

# Button to play again
play_again_button = tk.Button(root, text="Play Again", command=play_again, bg='#9E9E9E', fg='white', font=("Helvetica", 14))
play_again_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
