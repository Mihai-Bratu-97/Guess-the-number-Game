from tkinter import messagebox  # imports messagebox method from tkinter library


# show, for 4 times, a message, with a specific rule
def show_rules():
    text1 = "Rule no.1: You'll have three tries to guess the number."
    text2 = """Rule no.2: After these tries, if you didn't guess the number, you'll get nothing at your score. 
You could play how many rounds as you wish(but no more than 15)."""
    text3 = """Rule no.3: At the end of the game(or games), someone will be declared victorious, 
based on the score that you, and the computer, have got."""
    text4 = """Rule no.4: But, because there is a high interval where you can guess the number, on each guessing
(depends on the length of the number), the computer will give you a clue, two clues, or three clues. 
Good luck, and may the odds be ever in your favor("Hunger games")"""
    messagebox.showinfo("Rule no.1", text1)
    messagebox.showinfo("Rule no.2", text2)
    messagebox.showinfo("Rule no.3", text3)
    messagebox.showinfo("Rule no.4", text4)
