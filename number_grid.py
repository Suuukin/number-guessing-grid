import tkinter as tk
import tkinter.font as font
import random

# making our window and defining font
window = tk.Tk()
window.title("Number Guessing Grid")
myFont = font.Font(family="Courier", size=20, weight="bold")


# variables
class State:
    answer = random.randint(0, 99)
    guess = None
    greater = None
    correct_guess = False
    reset = False


def btn_op(label):
    State.guess = label
    State.correct_guess = State.guess == State.answer
    State.greater = State.guess < State.answer
    grey_out()


def color_button(button_number, button):
    if State.reset == False:
        if button_number == State.answer:
            # colors correct guess purple
            button.configure(background="purple")
        elif button_number <= State.answer:
            # colors buttons lower than guess
            button.configure(background="red")
        elif button_number >= State.answer:
            # colors buttons greater than answer blue
            button.configure(background="blue")
    else:
        button.configure(background='white')


def grey_out():
    for button_number, button in buttons.items():
        if State.reset == False:
            if State.correct_guess:
                # if the number clicked is the correct button
                # it colors itself
                color_button(button_number, button)
            else:
                if State.greater:
                    if button_number <= State.guess:
                        # colors self if the buttons is the guess
                        # or greater than the guess
                        color_button(button_number, button)
                else:
                    if button_number >= State.guess:
                        # colors self if the button is the guess
                        # or smaller then the guess
                        color_button(button_number, button)
        else:
            color_button(button_number, button)

# function for making all buttons
def make_btn(parent, label):
    return tk.Button(
        parent,
        text=label,
        font=myFont,
        command=lambda: btn_op(label),
    )


def restart():
    State.answer = random.randint(0,99)
    State.correct_guess = False
    State.reset = True
    grey_out()
    State.reset = False

# label with instructions
label_1 = tk.Label(window, text="Click To Guess Hidden Number", font=myFont)
label_1.grid(row=0, column=0)


# frame to hold our grid of buttons
frame = tk.Frame(window)
frame.grid(row=1, column=0)


# button dictionary
buttons = {}
# makes our 100 buttons and puts them in grid
for i in range(100):
    buttons[i] = b = make_btn(frame, i)
    row, column = divmod(i, 10)
    # this makes the buttons pad themselves to fit the frame
    b.grid(row=row, column=column, sticky="nsew")




reset_button = tk.Button(window, text='Reset', command=restart)
reset_button.grid(row=2, column=0)

tk.mainloop()
