from tkinter import*  # imports everything from tkinter library
import create_login  # imports create_login libray(my library)
import create_account  # imports create_account library(also my library)
import rules_section  # imports rules_section library(still my library)


# this closes the main window
def quitting(window):
    window.destroy()


# this closes the actual window(which can be login, or create account) and goes back to the main window
def go_back(window):
    window.destroy()
    main_window()


def main_window():
    # opens the main window
    window = Tk()
    # creates a "Login" button, and once you click it, calls login method from create_login library,
    # and places it based on x and y-axis
    btn_login = Button(window, text="Login", command=lambda: create_login.login(window), fg='grey', font=("Arial", 16))
    btn_login.place(x=20, y=20)
    # creates a "Create account" button, and once you click it, calls create_account method from create_account library,
    # and places it based on x and y-axis
    btn_signup = Button(window, text="Create account", fg='grey', font=("Arial", 16),
                        command=lambda: create_account.create_account(window))
    btn_signup.place(x=420, y=20)
    # creates a "Quit" button, and once you click it, calls quitting function defined above, and places it based on
    # x and y-axis
    quit_btn = Button(window, text="Quit", fg='grey', font=("Arial", 16), command=lambda: quitting(window))
    quit_btn.place(x=20, y=300)
    # creates a "Rules" button, and once you click it, calls show_rules method from rules_section library, and places it
    # based on x and y-axis
    rule_btn = Button(window, text="Rules", fg='grey', font=("Arial", 16), command=lambda: rules_section.show_rules())
    rule_btn.place(x=500, y=300)
    message = """Hello and welcome to "Guess Number" Game.
    In this game, you would have to guess a number, 
    which is between 1 and 290.
    To play this game, you'll need an account.
    If you have one, select 'Login', and if you don't have,
    select 'Create account'.
    For more information, access "Rules" option."""
    # creates a text message, that shows a specific message(defined above), and places it based on x and y-axis
    hello_message = Label(window, text=message, fg='black', font=("Helvetica", 14))
    hello_message.place(x=20, y=120)
    # this sets the tile of our window(which I set it at "Main Window")
    window.title("Main window")
    # this sets the resolution of our window(width=400 and length=600)
    window.geometry("600x400+10+20")
    # this sets the resizable function(each of them are width and length, and both of them are "False" the user
    # can adjust neither height nor length(and vice-versa) and if one of them is "True", he can adjust either width
    # or length(depending on which is "True")
    window.resizable(False, False)
    # this sets a specific icon on our window(that sets it with the name of the ico file, and with the "ico" extension)
    window.iconbitmap('Artcore-Illustrations-Artcore-4-Games-folder.ico')
    # this loops the window to infinite until the user closes the window
    window.mainloop()


if __name__ == "__main__":
    main_window()
