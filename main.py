from tkinter import *
import play
def main():
    root = Tk()
    root.configure(bg="sky blue")
    root.title("Welcome")
    root.geometry("1366x768")
    label1=Label(root,text="Welcome",fg="yellow",width=50,font="times 40 bold",height=15)
    label1.place(x=683, y=100, anchor="center")
    label2=Label(root,text="Let's play Rock,paper,scissor--click your choice!",fg="yellow",width=50,height=5,font="times 25 bold")
    label2.place(x=683, y=300, anchor="center")
    btn1 =Button(root,text="ROCK",font="times 20 bold", command=lambda:play("rock"),fg="#4267B2",bg="white",padx=20,pady=15)
    btn1.place(x=100,y=400)
    btn2 =Button(root, text="PAPER",font="times 20 bold", command=lambda:play("paper"),fg="#4267B2",bg="white",padx=20,pady=15)
    btn2.place(x=600,y=400)
    btn3=Button(root, text="SCISSOR",font="times 20 bold", command=lambda:play("scissor"),fg="#4267B2",bg="white",padx=20,pady=15)
    btn3.place(x=1000,y=400)
    btn4=Button(root,text="EXIT",font="times 20 bold", command=exit,fg="red",bg="white",padx=20,pady=15)
    btn4.place(x=600,y=600)
    # running the main loop
    root.mainloop()
main()
