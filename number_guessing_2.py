import tkinter as tk
import tkinter.font as font
import random



window = tk.Tk()
window.title("Number Guessing Game")
#font - I define a font and call it myFont
myFont = font.Font(family='Courier', size=20, weight='bold')


#variables
class State:
    number = random.randint(1, 100)
    check_result = ' is incorrect'
    guess = None

#functions
def update_guess():
    State.guess = txt_box1.get()
    State.guess = int(State.guess)
    textbox_input = txt_box1.get()
    check()
    textbox_input = textbox_input + State.check_result
    label_3["text"] = textbox_input

# checks if guess is correct if not tells if it is too high or too low
def check():
    if State.guess != State.number:
        if State.guess > State.number:
            State.check_result = ' is too high'
        else:
            State.check_result = ' is too low'
    else:
        State.check_result = ' is correct'


#Create a label to display something
label_1 = tk.Label(window, text="Guess a number between 1-100",font=myFont)
label_1.grid(row=0, column=0, columnspan=2)

#Create first text box, then place it by using "grid"
txt_box1 = tk.Entry(window, width=21, borderwidth=5, font=myFont)
txt_box1.grid(row=1, column=0, columnspan=2)

#Create button #1 
btn1 = tk.Button(window, text="Guess Number", font=myFont, command=update_guess)
btn1.grid(row=4, column=0, columnspan=2)


#Create 3rd label used for OUTPUT display
label_3 = tk.Label(window,text="", font=myFont)
label_3.grid(row=5, column=0, columnspan=2)


tk.mainloop()
