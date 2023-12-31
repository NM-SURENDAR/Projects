from tkinter import *
def main():
    root = Tk()
    root.configure(bg="sky blue")
    root.title("Welcome")
    root.geometry("1366x768")
    label1=Label(root,text="SS RESTAURANT",fg="yellow",bg="#4267B2",width=250,font="times 50 bold")
    label1.place(x=683, y=40, anchor="center")
    btn =Button(root, text="Morning session foods",font="times 20 bold", command=page_1,fg="#4267B2",bg="white",padx=50,pady=25)
    btn.place(x=683, y=200, anchor="center")
    btn =Button(root, text="afternoon session foods",font="times 20 bold", command=page_2,fg="#4267B2",bg="white",padx=50,pady=25)
    btn.place(x=683, y=350, anchor="center")
    btn =Button(root, text="Evening session foods",font="times 20 bold", command=page_3,fg="#4267B2",bg="white",padx=50,pady=25)
    btn.place(x=683, y=500, anchor="center")
    # running the main loop
    root.mainloop()
main()
