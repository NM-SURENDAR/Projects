from tkinter import *
from play import *

def main():
    root = Tk()
    root.title("Welcome")
    root.geometry("1366x768")
    root.configure(bg="sky blue")

    label1 = Label(root, text="Welcome", fg="yellow",bg="dark blue", width=57, font="times 30 bold", height=2)
    label1.place(x=683, y=50, anchor="center")

    label2 = Label(root, text="Let's play Rock, Paper, Scissor--click your choice!", fg="blue",bg="sky blue",width=40, height=3, font="times 20 bold")
    label2.place(x=683, y=300, anchor="center")

    btn1 = Button(root, text="ROCK", font="times 20 bold", command=lambda:result("rock"), fg="#4267B2", bg="white", padx=20, pady=15)
    btn1.place(x=100, y=400)

    btn2 = Button(root, text="PAPER", font="times 20 bold", command=lambda:result("paper"), fg="#4267B2", bg="white", padx=20, pady=15)
    btn2.place(x=600, y=400)

    btn3 = Button(root, text="SCISSOR", font="times 20 bold", command=lambda:result("scissor"), fg="#4267B2", bg="white", padx=20, pady=15)
    btn3.place(x=1000, y=400)

    btn4 = Button(root, text="EXIT", font="times 20 bold", command=exit, fg="red", bg="white", padx=20, pady=15)
    btn4.place(x=600, y=600)

    # running the main loop
    root.mainloop()

if __name__ == '__main__':
    main()
