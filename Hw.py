import tkinter
import tkinter.messagebox
import random

root=tkinter.Tk()
root.minsize(350,260)
root.title("2 Number Game")

import tkinter
import tkinter.messagebox
import random

root=tkinter.Tk()
root.minsize(350,260)
root.title("Random Number Game")

def btn_confirm():
    myName=name_entry.get()
    tkinter.messagebox.showinfo("name","well, "+ myName +", I am thinking of a number between 1 and 20.")

number1 = random.randint(1,20)
number2 = random.randint(1,20)
def guess_confirm():
    myGuess=guess1_entry.get()
    myGuess=int(myGuess)
    if myGuess==number1:
        tkinter.messagebox.showinfo("guess", "Good Job on the 1st!!")
    elif myGuess<number1:
        tkinter.messagebox.showinfo("guess", "Try Higher on the 1st")
    elif myGuess>number1:
        tkinter.messagebox.showinfo("guess", "Try Lower on the 1st")
   
    myGuess2=guess2_entry.get()
    myGuess2=int(myGuess2)
    if myGuess2==number2:
        tkinter.messagebox.showinfo("guess2", "Good Job on the 2nd!!")
    elif myGuess<number2:
        tkinter.messagebox.showinfo("guess2", "Try Higher on the 2nd")
    elif myGuess>number2:
        tkinter.messagebox.showinfo("guess2", "Try Lower on the 2nd")

welcome=tkinter.Label(root, text="Number Guesser")
welcome.pack()

name=tkinter.Label(root, text="Whats your name?")
name.place(x=10, y=60)

name_entry=tkinter.Entry(root, width=20)
name_entry.place(x=10, y=90)

ok=tkinter.Button(root, text="Ok", command=btn_confirm)
ok.place(x= 200, y=85)

guess1=tkinter.Label(root, text="Take a first Guess:")
guess1.place(x=10, y= 130)

guess1_entry=tkinter.Entry(root, width=10)
guess1_entry.place(x=115, y=130)

guess2=tkinter.Label(root, text="Take a second Guess:")
guess2.place(x=10, y= 160)

guess2_entry=tkinter.Entry(root, width=10)
guess2_entry.place(x=135, y=160)

guess_btn=tkinter.Button(root, text="Guess", command=guess_confirm)
guess_btn.place(x=205, y=140)

root.mainloop()