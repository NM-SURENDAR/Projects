from tkinter import*
def final_scores(u_score,c_score):#show final scores and exit mainloop
    top1=Tk()
    top1.configure(bg="sky blue")
    top1.geometry("450x250")
    top1.title("result")
    
    if u_score==c_score:
        x="Tie!"#save the final result in variable 'x'
    elif u_score>c_score:
        x="You Win!"
    else:
        x="Computer wins!"
            
    lb1=Label(top1,text="Result:"+x,fg="blue",bg="sky blue",font="times 35 bold",width=100)
    lb1.pack()
        
    lb1=Label(top1,text="Your score:"+str(u_score),fg="green",bg="sky blue",font="times 20 bold",width=50)
    lb1.pack()
        
    lb1=Label(top1,text="Computer score:"+str(c_score),fg="green",bg="sky blue",font="times 20 bold",width=50)
    lb1.pack()
    top1.mainloop()