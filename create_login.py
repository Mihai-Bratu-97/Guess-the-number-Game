import csv  # this imports csv library(which I'll use it for storing the email and passwords as a database)
from tkinter import*  # this imports everything from tkinter library
from tkinter import messagebox  # this imports the messagebox method from tkinter library
import mainly_window  # this imports the main window libray(my library)
import game_itself

# these I'll use it later for checking the existing passwords and emails
password_list = []
email_list = []


def login_email(login_window):
    # this sets a text with the name "Email"
    email_label = Label(login_window, text="Email", fg="grey", font=("Arial", 14))
    # this sets an input text for the above "Email"
    email_input = Entry(login_window, width=23)
    # this places the email text and the email input on the window, based on x and y-axis
    email_input.place(x=270, y=124)
    email_label.place(x=200, y=120)
    return email_input


def login_password(login_window):
    # same as above, but this is for password, with a little change(password is shown with "*")
    password_label = Label(login_window, text="Password", fg='grey', font=("Arial", 14))
    password_input = Entry(login_window, show="*", width=23)
    password_input.place(x=270, y=202)
    password_label.place(x=175, y=200)
    return password_input


def check_login(user_email, user_password, login_window):
    # this get the text that was typed in email input, and then remove off the unnecessary spaces
    result_email = user_email.get()
    result_email = result_email.rstrip("\n")
    # same as above, but now for password
    result_password = user_password.get()
    result_password = result_password.rstrip("\n")
    # this checks the len of email and password, and if both of them are 0, opens the csv file.
    # and extracts and puts passwords into passwords_list and email into email_list
    if len(email_list) == 0 and len(password_list) == 0:
        with open("email_and_passw.csv") as second_email:
            read = csv.reader(second_email)
            # this I used it for not taking in the first line(which is the string "email" and "password"
            next(second_email)
            for row in read:
                email_list.append(row[0])
                password_list.append(row[1])
    # now checks if the email and password we've typed in exists in our password_list and email_list, and if they don't,
    # it shows a messagebox
    if result_email not in email_list or result_password not in password_list:
        messagebox.showinfo("show status", "Your password or email are incorrect! Try again!")
    # otherwise, if they exist, also show a messagebox, and close the actual login window and opens the main window
    else:
        messagebox.showinfo("show status", "You have connected successfully!")
        login_window.destroy()
        game_itself.game()


def login(window):
    # this closes the main window(for not having two windows opened at same time)
    window.destroy()
    # this creates a new window(for login)
    login_window = Tk()
    # here I called the both functions defined above(which both of them return the email and password input) with
    # the login window as a parameter
    email = login_email(login_window)
    password = login_password(login_window)
    # I defined a button, with "Login" name, and, once you click it, calls check_login function, with the email and
    # password we've typed in, and the login window as parameters, and places it based on x and y-axis
    check_btn = Button(login_window, text="Login", fg='Black', font=("Arial", 14),
                       command=lambda: check_login(email, password, login_window))
    check_btn.place(x=300, y=250)
    # here I defined another button, which is a "go_back" button for going back to the main window(which calls
    # go_back function from mainly_window library with the login window as a parameter)
    # and places it based on x and y-axis
    go_back_btn = Button(login_window, text="go back", fg='black',
                         font=("Arial", 14), command=lambda: mainly_window.go_back(login_window))
    go_back_btn.place(x=30, y=360)
    # this sets the tile of our window(which I set it at "Login")
    login_window.title("Login")
    # this sets the resolution of our window(width=400 and length=600)
    login_window.geometry("600x400+10+20")
    # this sets the resizable function(each of them are width and length, and both of them are "False" the user
    # can adjust neither height nor length(and vice-versa) and if one of them is "True", he can adjust either width
    # or length(depending on which is "True")
    login_window.resizable(False, False)
    # this loops the window to infinite until the user closes the window
    login_window.mainloop()
