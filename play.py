import csv  # import csv library
from tkinter import*  # import everything from tkinter library
from tkinter import messagebox  # import messagebox method from tkinter library
import random  # import random library


# is the pc score, that we'll use it later for counting the general score, that we reset it when the game is over
pc_score = 0
# is the user score, that we'll use it later for counting the general score, that we reset it when the game is over
user_score = 0
# is a variable for counting the number of hints, that we reset it when a new number is played
count_hint = 0
# a list for putting the number played by the user every lap, that we reset it when the next lap comes
number_already_typed = []
# the number played by the computer, chosen random, between 1 and 290
pc_choice = random.randint(1, 290)
# a variable who counts the laps, and once the game is over, we reset it
count_laps = 0
# a variable who keeps showing the user how many tries he has left(because the user has 3 tries per laps),
# and once the lap is over, we reset it
count_tries = 3
# here I changed the type of pc_choice to str, because I need to do some operations on it who implies indexes
pc_choice = str(pc_choice)
# this checks if the len of the pc_choice number is == 3, and if it's, creates the below list with some hints(3) in it
if len(pc_choice) == 3:
    hint_list3 = ["The length of the number is:3",
                  "The number of hundreds is:" + pc_choice[0],
                  "The number of decimals is:" + pc_choice[1]]
# this checks if the len of the pc_choice number is == 2, and if it's, creates the below list with some hints(2) in it
elif len(pc_choice) == 2:
    hint_list2 = ["The length of the number is:2",
                  "The number of decimals is:" + pc_choice[0]]
# here I converted the pc_choice number back to int, because I need it to be in this form for using later
pc_choice = int(pc_choice)


# this one checks the hints, and creates a list, with some "hints" in them, based on the len of the pc_choice_number
def check_hint(number):
    global hint_list2, hint_list3
    number = str(number)
    if len(number) == 3:
        hint_list3 = ["The length of the number is:3",
                      "The number of hundreds is:" + number[0],
                      "The number of decimals is:" + number[1]]
    elif len(number) == 2:
        hint_list2 = ["The length of the number is:2",
                      "The number of decimals is:" + number[0]]
    number = int(number)


# this one shows 3, 2, or 1 different hints(per lap), every time when "Hint" button is click it,
# based on the len of the pc_choice number. Every hint is different, and it's shown randomly
def hint(number):
    global count_hint
    number = str(number)
    if count_hint < len(number):
        if len(number) == 3:
            random_hint = random.choice(hint_list3)
            hint_list3.remove(random_hint)
            messagebox.showinfo("hint", random_hint)
            count_hint += 1
        elif len(number) == 2:
            random_hint = random.choice(hint_list2)
            hint_list2.remove(random_hint)
            messagebox.showinfo("hint", random_hint)
            count_hint += 1
        elif len(number) == 1:
            messagebox.showinfo("hint", "The length of the number is:1")
            count_hint += 1
    else:
        messagebox.showinfo("no more hints", "You are outta hints!")


# this one shows how many tries do you have left(and sets that message based on x and y-axis),
# but also creates a "box input", checks if what user has typed in the "box input" is a number, a valid one,
# and shows a message based of what user has typed in(and sets the message and the "input box" based on x and y-axis)
def input_number(play_window, label_for_numbers, input_user_lap):
    info_label = Label(play_window, font=("Arial", 14), fg='blue', text="You have 3 more left")
    info_label.place(x=150, y=110)
    user = Label(play_window, text="Put in the number: ", font=("Arial", 12, 'bold'), fg="gray")
    user.place(x=170, y=140)
    user_input = Text(play_window, height=1, width=15)
    user_input.place(x=330, y=143)
    check_btn = Button(play_window, text="Check the number", font=("Arial", 8, 'bold'), fg='gray',
                       command=lambda: check_input(user_input, label_for_numbers,
                                                   input_user_lap, info_label, play_window))
    check_btn.place(x=460, y=141)


# this one check if the number who user has just typed in is a valid one, and show different message based on the number
# and after a valid number has been put in, a message will be shown, and the "input lap box", "check lap" button,
# and his labels text will disappear
def check_laps(play_window, input_lap, label_for_laps, check_lap_btn, text_lap, label_for_numbers):
    input_user_lap = input_lap.get('1.0', 'end')
    input_user_lap = input_user_lap.rstrip("\n")
    if len(input_user_lap) == 0:
        sentence = "You have to type in something!!"
        label_for_laps["text"] = sentence
    elif not input_user_lap.isnumeric():
        sentence = "Only numbers allowed!"
        label_for_laps["text"] = sentence
    elif int(input_user_lap) > 15 or int(input_user_lap) < 1:
        sentence = "The number must be between 1 and 15."
        label_for_laps["text"] = sentence
    elif 16 > int(input_user_lap) > 0 and int(input_user_lap) % 2 == 0:
        sentence = "The number must be an odd one!"
        label_for_laps["text"] = sentence
    else:
        messagebox.showinfo("Start", "The game has just started up!")
        check_lap_btn.destroy()
        input_lap.destroy()
        text_lap.destroy()
        label_for_laps.destroy()
        input_number(play_window, label_for_numbers, input_user_lap)


# this one creates the "input lap box" and his label text, set them based on x and y-axis, and return them
def laps(play_window):
    text_lap = Label(play_window, text="How many laps would you like to play?", font=("Arial", 14, 'bold'), fg='grey')
    input_lap = Text(play_window, width=10, height=1)
    text_lap.place(x=45, y=110)
    input_lap.place(x=410, y=115)
    return input_lap, text_lap


# this one check if what user has typed in is a valid number, and also if it's the right one(and shows different
# messages based on that number or what user typed in)
# And after each lap,resets the count_hint, number_already_typed, and the number that pc will play
# And at the end of each lap, a message will appear, showing who won the lap,
# and at the end of the game, also a message will appear, showing who won the game
def check_input(user_input, label_for_numbers, input_user_lap, info_label, play_window):
    global count_laps, count_tries, pc_choice, number_already_typed, user_score, pc_score, count_hint, \
        hint_list2, hint_list3
    if count_laps < int(input_user_lap):
        if count_tries > 1:
            input_result = user_input.get('1.0', 'end')
            input_result = input_result.rstrip("\n")
            if len(input_result) == 0:
                sentence = "You have to type something in!"
                sentence_info = "You have " + str(count_tries) + " more left"
                info_label["text"] = sentence_info
                label_for_numbers["text"] = sentence
            elif not input_result.isnumeric():
                sentence = "Only numbers allowed! Try again!"
                sentence_info = "You have " + str(count_tries) + " more left"
                info_label["text"] = sentence_info
                label_for_numbers["text"] = sentence
            elif int(input_result) in number_already_typed:
                sentence = "This number you've already used it. Try another one!"
                sentence_info = "You have " + str(count_tries) + " more left"
                info_label["text"] = sentence_info
                label_for_numbers["text"] = sentence
            elif int(input_result) > 290 or int(input_result) < 0:
                sentence = "The number must be between 1 and 290"
                sentence_info = "You have " + str(count_tries) + " more left"
                info_label["text"] = sentence_info
                label_for_numbers["text"] = sentence
            elif 291 > int(input_result) > 0 and int(input_result) != pc_choice:
                number_already_typed.append(int(input_result))
                sentence = "The number you typed in is not the correct one!"
                count_tries -= 1
                sentence_info = "You have " + str(count_tries) + " more left"
                info_label["text"] = sentence_info
                label_for_numbers["text"] = sentence
            elif int(input_result) == pc_choice:
                user_score += 1
                count_tries = 3
                count_laps += 1
                count_hint = 0
                pc_choice = random.randint(1, 290)
                pc_choice = str(pc_choice)
                check_hint(pc_choice)
                messagebox.showinfo("Round number " + str(count_laps) + " won",
                                    "You got the number! You beaten the computer!")
        else:
            pc_score += 1
            count_tries = 3
            count_laps += 1
            with open("computer_number.csv", "a", newline="") as pc:
                writing = csv.writer(pc)
                writing.writerow([str(pc_choice)])
            messagebox.showinfo("Round number " + str(count_laps) + " lose",
                                "The round's just ended up! The computer won!")
            number_already_typed = []
            pc_choice = random.randint(1, 290)
            check_hint(pc_choice)
            count_hint = 0
            info_label["text"] = "You have 3 more left"
    if count_laps == int(input_user_lap):
        if user_score > pc_score:
            messagebox.showinfo("End game", "The game ended up! The user's won!")
        elif user_score < pc_score:
            messagebox.showinfo("End game", "The game ended up! The computer's won. Better luck next time!")
        play_window.destroy()


def play(game_window):
    # this one closes the game_window window
    game_window.destroy()
    # this one opens a new window
    play_window = Tk()
    # these variables call the laps function and save the both returns in them
    input_lap, lap_text = laps(play_window)
    # this one creates a label text, which we'll use it later for showing a specific message,
    # when "Check number" button is click it, based on what user has typed in and sets it based on x and y-axis
    label_for_numbers = Label(play_window, font=("Arial", 8))
    label_for_numbers.place(x=330, y=168)
    # this one creates a label text, which we'll use it later for showing a specific message,
    # when "Check laps" button is click it, based on what user has typed in and sets it based on x and y-axis
    label_for_laps = Label(play_window, font=("Arial", 8))
    label_for_laps.place(x=350, y=145)
    # creates a "Check laps" button for checking if what user has typed in is correct once it's click it,
    # and if it's a number between 1 and 15, to be an odd one, and sets it based on x and y-axis
    check_lap_btn = Button(play_window, text="Check laps", fg='grey', font=("Arial", 10, 'bold'),
                           command=lambda: check_laps(play_window, input_lap, label_for_laps, check_lap_btn, lap_text,
                                                      label_for_numbers))
    check_lap_btn.place(x=500, y=113)
    # creates a "Hint" button for asking hints, but not more that the len of pc_choice number, that shows a random hint
    # when it's click it, and sets it based on x and y-axis
    hint_btn = Button(play_window, text="Hint", fg='grey', font=("Arial", 14, "bold"),
                      command=lambda: hint(pc_choice))
    hint_btn.place(x=540, y=10)
    # sets the title of the window(which is "Inside tha game" in this case)
    play_window.title("Inside the game")
    # this sets the resolution of our window(width=400 and length=600)
    play_window.geometry("600x400+10+20")
    # this sets the resizable function(each of them are width and length, and both of them are "False" the user
    # can adjust neither height nor length(and vice-versa) and if one of them is "True", he can adjust either width
    # or length(depending on which is "True")
    play_window.resizable(False, False)
    # this loops the window to infinite until the user closes the window
    play_window.mainloop()
