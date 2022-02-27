import csv  # this import the csv library(I'll use it for storing emails and passwords(as a database)
from tkinter import*  # this imports everything from tkinter library
from tkinter import messagebox  # this imports messagebox method from tkinter library
import os  # imports os library
import mainly_window  # imports the main window libray(my library)

# these I'll use it later for checking the email and write this "header" in csv file, if it's empty the csv file
header = ["email", "password"]
email_list = []


def account_email(account_window):
    # this sets a text with the name "Email"
    email_label = Label(account_window, text="Email", fg='blue', font=("Arial", 14))
    # this sets an input text for the above "Email"
    email_input = Entry(account_window, width=25)
    # this places the email text and the email input on the window, based on x and y-axis
    email_label.place(x=180, y=167)
    email_input.place(x=250, y=170)
    return email_input


def account_password(account_window):
    # same as above, but this is for password, with a little change(password is shown with "*")
    password_label = Label(account_window, text="Password", fg='blue', font=("Arial", 14))
    password_input = Entry(account_window, show="*", width=25)
    password_label.place(x=150, y=217)
    password_input.place(x=250, y=220)
    return password_input


def check_account(user_email, user_password, account_window):
    # this checks the length of the csv files
    test_size = os.path.getsize("email_and_passw.csv")
    # this get the text that was typed in email input, and then remove off the unnecessary spaces
    result_email = user_email.get()
    result_email = result_email.rstrip("\n")
    # same as above, but now for password
    result_password = user_password.get()
    result_password = result_password.rstrip('\n')
    # this checks the len of email_list and the len of file, and if the email_list is 0 and the len of file is not 0
    # (which means something is written in file), extracts the emails from csv file, and puts them into email_list
    if len(email_list) == 0 and test_size != 0:
        with open("email_and_passw.csv") as second_email:
            read = csv.reader(second_email)
            # this I used it for not taking in the first line(which is the string "email" and "password"
            next(second_email)
            for row in read:
                if len(row) != 0:
                    email_list.append(row[0])
    # checks if the email we've typed in above already exists in our database
    if result_email in email_list:
        messagebox.showinfo("show status", "Your email is already taken!")
    # after checking the email, and once the email isn't in our database, we check if the len of password is lower
    # than 8 characters
    elif len(result_password) < 8:
        messagebox.showinfo("show status", "The password must has 8 characters length!")
    # otherwise, if both of the above conditions aren't True(which means the email is not in our database and the len
    # of the password is greater than 7 characters, our account will be created, and a messagebox will be displayed.
    # And then, the email and password will be written in our csv file(our database)
    else:
        messagebox.showinfo("show status", "Your account has been created!")
        with open("email_and_passw.csv", "a", newline="") as second_email:
            writing = csv.writer(second_email)
            my_email_and_psw = [result_email, result_password]
            # this checks if the len of file is 0, and if it's, writes our header(which is "email" and "password")
            if test_size == 0:
                writing.writerow(header)
            writing.writerow(my_email_and_psw)
        # finally, our window for creating account will be closed, and the main window will be opened
        account_window.destroy()
        mainly_window.main_window()


def create_account(window):
    # this closes the main window
    window.destroy()
    # this opens a new window(for creating account)
    account_window = Tk()
    # these call the email and password functions defined above
    email = account_email(account_window)
    password = account_password(account_window)
    # creates a "Create account" button, and oce you click it, calls check_account function, with email and password
    # we've just typed in, and account_window as parameters, and places it based on x and y-axis
    account_btn = Button(account_window, text="Create account", fg='blue', font=("Arial", 16),
                         command=lambda: check_account(email, password, account_window))
    account_btn.place(x=240, y=270)
    # here I defined another button, which is a "go_back" button for going back to the main window(which calls
    # go_back function from mainly_window library with the account_window as a parameter)
    # and places it based on x and y-axis
    go_back_btn = Button(account_window, text="go back", fg='black',
                         font=("Arial", 14), command=lambda: mainly_window.go_back(account_window))
    go_back_btn.place(x=30, y=360)
    # this sets the tile of our window(which I set it at "Creating account")
    account_window.title("Creating account")
    # this sets the resolution of our window(width=400 and length=600)
    account_window.geometry("600x400+10+20")
    # this sets the resizable function(each of them are width and length, and both of them are "False" the user
    # can adjust neither height nor length(and vice-versa) and if one of them is "True", he can adjust either width
    # or length(depending on which is "True")
    account_window.resizable(False, False)
    # this loops the window to infinite until the user closes the window
    account_window.mainloop()
