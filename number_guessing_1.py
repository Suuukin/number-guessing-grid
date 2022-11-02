import tkinter as tk
import tkinter.font as font
import random



window = tk.Tk()
window.title("Number Guessing Game")
#font - I define a font and call it myFont
myFont = font.Font(family='Courier', size=20, weight='bold')

#functions
def guess():
    textbox_input = txt_box1.get()
    textbox_input = textbox_input + ' was guessed'
    label_3["text"] = textbox_input


#Create a label to display something
label_1 = tk.Label(window, text="Guess a number between 1-100",font=myFont)
label_1.grid(row=0, column=0, columnspan=2)

#Create first text box, then place it by using "grid"
txt_box1 = tk.Entry(window, width=21, borderwidth=5, font=myFont)
txt_box1.grid(row=1, column=0, columnspan=2)

#Create button #1 
btn1 = tk.Button(window, text="Guess Number", font=myFont, command=guess)
btn1.grid(row=4, column=0, columnspan=2)


#Create 3rd label used for OUTPUT display
label_3 = tk.Label(window,text="", font=myFont)
label_3.grid(row=5, column=0, columnspan=2)


tk.mainloop()

