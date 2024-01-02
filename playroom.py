from tkinter import *
import random
user_score=0
computer_score=0
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

    btn4 = Button(root, text="EXIT", font="times 20 bold", command=lambda:exit(), fg="red", bg="white", padx=20, pady=15)
    btn4.place(x=600, y=600)
    #functions
    def declare_result(result,input):
        top=Toplevel(root)
        top.configure(bg="sky blue")
        top.geometry("450x250")
        top.title("result")
        lb1=Label(top,text="your input:"+input,fg="yellow",bg="sky blue",font="times 20 bold",width=50)
        lb1.pack()
        lb1=Label(top,text="computer input:"+input,fg="yellow",bg="sky blue",font="times 20 bold",width=50)
        lb1.pack()
        lb1=Label(top,text=result,fg="yellow",bg="sky blue",font="times 35 bold",width=100)
        lb1.pack()
        btn1 = Button(top, text="ROCK", font="times 20 bold", command=lambda:top.destroy(), fg="#4267B2", bg="white", padx=20, pady=15)
        btn1.pack()

    def result(input):
        options=["rock","paper","scissor"]
        user_input=input
        computer_input=random.choice(options)
        if user_input==computer_input:
            declare_result("It is a Tie!",input)
        print("your choice is:"+input)
        return
    def exit():
        top1=Tk()
        top1.configure(bg="sky blue")
        top1.geometry("450x250")
        top1.title("result")
        lb1=Label(top1,text="your score:"+str(user_score),fg="yellow",bg="sky blue",font="times 20 bold",width=50)
        lb1.pack()
        lb1=Label(top1,text="computer score:"+str(computer_score),fg="yellow",bg="sky blue",font="times 20 bold",width=50)
        lb1.pack()
        if user_score==computer_score:
            x="Tie!!"
        elif user_score>computer_score:
            x="You Win!"
        else:
            x="computer wins!"
        lb1=Label(top1,text="result:"+x,fg="yellow",bg="sky blue",font="times 35 bold",width=100)
        lb1.pack()
        top1.mainloop()
        root.destroy()   
        # running the main loop
    root.mainloop()
    
if __name__ == '__main__':
    main()
