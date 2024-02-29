import tkinter as tk
from NEAMainGame2 import run_game
from tkinter import *

#creating an instance of tkinter as a window
window=tk.Tk()

#setting the title of the window
window.title('Main menu')

#sets the size of the window
window.geometry("1440x847+0+25")

#creates the command start_game to run the game for NEAMainGame on each difficulty level
def start_game(choice):
    selectedDifficulty.set(choice)
    if choice == "Easy":
        choice = 1
    if choice == "Normal":
        choice = 2
    if choice == "Hard":
        choice = 3
    if choice == "Very Hard":
        choice = 4
    run_game(choice=choice)
    window.mainloop()

#creating a function to quit the menu if the button is pressed
def quit_game():
    window.destroy()
    window.mainloop()

#configuring the windows minimum size and the columns within it's grid
window.rowconfigure([0,1,2], minsize=50, weight=1)
window.columnconfigure([0,1,2], minsize=50, weight=1)

#creating a canvas widget to serve as the background
canvas = Canvas(window, bg='green', height = '1440', width = '1694')
canvas.place(x=0,y=0)

#creating a variable to store the players difficulty selection
selectedDifficulty = tk.StringVar()

#creating the button to start the game
btn_startgame_easy = tk.Button(master=window, text="Start Game",width = 20, height = 10, borderwidth=0, command=lambda: start_game(selectedDifficulty.get()))
btn_startgame_easy.grid(row=1, column=0)

#button that allows the player to call the qit_game function
btn_quitGame = tk.Button(master=window, text='Quit Game', width=20, height=10, borderwidth=0, command=quit_game)
btn_quitGame.grid(row=1, column=2)

#drop down menu for the  player to use to select the difficulty
dropdown = tk.OptionMenu(window, selectedDifficulty, 'Easy', 'Normal', 'Hard', 'Very Hard')
dropdown.grid(row=1,column=1)

#label that instructs the player to select a difficulty from the dropdown menu
difficulty_label = tk.Label(window, text="Select a difficulty from the drop-down menu", width=30,bg='green')
difficulty_label.grid(row=0,column=1)

#running the main loop of the menu
window.mainloop()