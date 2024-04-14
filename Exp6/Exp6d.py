import tkinter as tk
import random

# Write a GUI-based program that plays a guess-the-number game in which the roles of the computer and the user are the reverse of what they are in the Case Study of this chapter. In this version of the game, the computer guesses a number between 1 and 100 and the user provides the responses. The window should display the computer’s guesses with a label. The user enters a hint in response, by selecting one of a set of command buttons labeled Too small, Too large, and Correct. When the game is over, you should disable these buttons and wait for the user to click New game, as before.

class GuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guessing Game")
        
        self.computer_guess = None
        self.min_num = 1
        self.max_num = 100
        
        self.label = tk.Label(self.window, text="Guess a number between 1 and 100:")
        self.label.pack()
        
        self.button_small = tk.Button(self.window, text="Too small", command=self.too_small)
        self.button_small.pack()
        
        self.button_large = tk.Button(self.window, text="Too large", command=self.too_large)
        self.button_large.pack()
        
        self.button_correct = tk.Button(self.window, text="Correct", command=self.correct)
        self.button_correct.pack()
        
        self.button_new_game = tk.Button(self.window, text="New game", command=self.new_game, state=tk.DISABLED)
        self.button_new_game.pack()
        
        self.new_game()
        
        self.window.mainloop()
    
    def new_game(self):
        self.computer_guess = random.randint(self.min_num, self.max_num)
        self.label.config(text="Guess a number between 1 and 100:")
        self.button_small.config(state=tk.NORMAL)
        self.button_large.config(state=tk.NORMAL)
        self.button_correct.config(state=tk.NORMAL)
        self.button_new_game.config(state=tk.DISABLED)
    
    def too_small(self):
        self.min_num = self.computer_guess + 1
        self.make_guess()
    
    def too_large(self):
        self.max_num = self.computer_guess - 1
        self.make_guess()
    
    def correct(self):
        self.label.config(text=f"The computer guessed {self.computer_guess}.")
        self.button_small.config(state=tk.DISABLED)
        self.button_large.config(state=tk.DISABLED)
        self.button_correct.config(state=tk.DISABLED)
        self.button_new_game.config(state=tk.NORMAL)
    
    def make_guess(self):
        self.computer_guess = random.randint(self.min_num, self.max_num)
        self.label.config(text=f"The computer guessed {self.computer_guess}.")

GuessingGame()