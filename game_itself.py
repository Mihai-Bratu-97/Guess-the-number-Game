from tkinter import*  # import everything from tkinter library
from tkinter import messagebox  # import messagebox method from tkinter library
import numpy as np  # import numpy library with an alias(np)
import play  # import play libray(my library)


# this function shows a message once the "check" button is click it
def show_info():
    text = "You can check if a number has been played in the previous games"
    messagebox.showinfo("info", text)


# this function sets a "box input"(with a specific width and height) for typing the number,
# places that "box input" based on x and y-axis, and then returns that number who has just been typed in
def check_num(game_window):
    check_num_input = Text(game_window, width=8, height=1)
    check_num_input.place(x=240, y=166)
    return check_num_input


# this function, whenever the "Check" button is click, takes the number who has been typed in,
# check if that numbers meets some specific conditions, and shows a message label based on what condition has been met,
# and ofcourse sets that message based on x and y-axis. And finally, gets the numbers from 'computer_number.csv' file
# for comparing with the actual number, and if the number is one of the numbers who exist in this file,
# show a message label who says, in percentage, how often was played in the previous games
def num_input(check_num_input, number_label):
    number_input = (check_num_input.get("1.0", "end"))
    number_input = number_input.rstrip("\n")
    pc_number = np.genfromtxt("computer_number.csv")
    if not number_input.isnumeric():
        sentence = "Only numbers allowed!"
    elif int(number_input) > 290 or int(number_input) < 0:
        sentence = "The number must be between 1 and 290!"
    elif 291 > int(number_input) > 0 and int(number_input) not in pc_number:
        sentence = "The number you've typed in hasn't played yet!"
    else:
        pc_number_mean = np.mean(pc_number == int(number_input))
        sentence = "This number has been played " + str(round(pc_number_mean * 100, 2)) + "% in the previous games!"
    number_label["text"] = sentence
    number_label.place(x=240, y=190)


# this function closes the actual window, when the "Exit" button is click it
def exit_1(game_window):
    game_window.destroy()


def game():
    # this one opens a new window for the game itself
    game_window = Tk()
    # this one creates a 'play button', that calls the play method from play library once it's click it and opens a
    # new window which is going to be the game, and at the same time closes the actual window
    play_btn = Button(game_window, text="Play", fg="blue", font=("Arial", 14), command=lambda: play.play(game_window))
    # this one sets the 'play button' based on x and y-axis
    play_btn.place(x=250, y=80)
    # this one calls the check_num function and saves the result in check_num_input variable
    check_num_input = check_num(game_window)
    # this one creates a text, which we'll use it when we click the "Check" button
    number_label = Label(game_window, font=("Arial", 8))
    # this creates a 'Check' button, that calls the num_input function and uses the text we've just created above
    # (number_label) for showing different text when the button is click it, based on what was typed in
    check_num_btn = Button(game_window, text="Check", fg="blue", font=("Arial", 10, "bold"),
                           command=lambda: num_input(check_num_input, number_label))
    # this sets the "check" button based on x and y-axis
    check_num_btn.place(x=316, y=163)
    # this creates a 'Check number info' that shows a message when it's click it about what "Check" button supposes
    # to do
    check_num_info = Button(game_window, text="Check number info", fg="black", font=("Arial", 10),
                            command=lambda: show_info())
    # this one sets the "check number info" based on x and y-axis
    check_num_info.place(x=115, y=163)
    # this one creates an "Exit" button that closes the game when it's click it
    exit_btn = Button(game_window, text="Exit", fg="blue", font=("Arial", 14), command=lambda: exit_1(game_window))
    # this one sets the "Exit" button based on x and y-axis
    exit_btn.place(x=250, y=250)
    # this one sets the title of the window(which is 'Game' in this case)
    game_window.title("Game")
    # this sets the resolution of our window(width=400 and length=600)
    game_window.geometry("600x400+10+20")
    # this sets the resizable function(each of them are width and length, and both of them are "False" the user
    # can adjust neither height nor length(and vice-versa) and if one of them is "True", he can adjust either width
    # or length(depending on which is "True")
    game_window.resizable(False, False)
    # this loops the window to infinite until the user closes the window
    game_window.mainloop()
