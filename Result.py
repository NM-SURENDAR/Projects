def exit(user_score,computer_score):#show final scores and exit mainloop
        top1=Tk()
        top1.configure(bg="sky blue")
        top1.geometry("450x250")
        top1.title("result")
        
        lb1=Label(top1,text="your score:"+str(user_score),fg="yellow",bg="sky blue",font="times 20 bold",width=50)
        lb1.pack()
        
        lb1=Label(top1,text="computer score:"+str(computer_score),fg="yellow",bg="sky blue",font="times 20 bold",width=50)
        lb1.pack()
        
        if user_score==computer_score:
            x="Tie!!"#save the final result in variable 'x'
        elif user_score>computer_score:
            x="You Win!"
        else:
            x="computer wins!"
            
        lb1=Label(top1,text="result:"+x,fg="yellow",bg="sky blue",font="times 35 bold",width=100)
        lb1.pack()
    
        top1.mainloop()
        root.destroy()   