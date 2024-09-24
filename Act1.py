import tkinter
import tkinter.messagebox
import random

root=tkinter.Tk()
root.minsize(350,260)
root.title("Random Number Game")

def btn_confirm():
    myName=name_entry.get()
    tkinter.messagebox.showinfo("name","well, "+ myName +", I am thinking of a number between 1 and 20.")

number = random.randint(1,20)
def guess_confirm():
    myGuess=guess_entry.get()
    myGuess=int(myGuess)
    if myGuess==number:
        tkinter.messagebox.showinfo("guess", "Good Job!!")
    elif myGuess<number:
        tkinter.messagebox.showinfo("guess", "Try Higher")
    elif myGuess>number:
        tkinter.messagebox.showinfo("guess", "Try Lower")



welcome=tkinter.Label(root, text="Number Guesser")
welcome.pack()

name=tkinter.Label(root, text="Whats your name?")
name.place(x=10, y=60)

name_entry=tkinter.Entry(root, width=20)
name_entry.place(x=10, y=90)

ok=tkinter.Button(root, text="Ok", command=btn_confirm)
ok.place(x= 200, y=85)

guess=tkinter.Label(root, text="Take a Guess:")
guess.place(x=10, y= 130)

guess_entry=tkinter.Entry(root, width=10)
guess_entry.place(x=95, y=130)

guess_btn=tkinter.Button(root, text="Guess", command=guess_confirm)
guess_btn.place(x=192, y=130)

root.mainloop()