from tkinter  import *
import qrcode
import os
def generate_qrcode(url,qr_name,c_color):
    url1=str(url)
    qr_name=str(qr_name)
    c_color=str(c_color)
    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    qr.add_data(url)
    qr.make(fit=True)
    img=qr.make_image(fill_color=c_color,back_color="white")
    target_folder="QRcodes"
    try:
        os.makedirs(target_folder,exist_ok=False)
    except FileExistsError:
        pass
    file_path=os.path.join(target_folder,qr_name+".jpg")
    img.save(file_path)
win=Tk()
win.title("Welcome")
win.geometry("1366x768")
# win.configure(bg="")
h_lable=Label(win,text="QR CODE GENERATER",fg="blue",width=50,height=20,bg="lavender",font="times 60 bold")
h_lable.place(x=683, y=50, anchor="center")
#entry part
lable1=Label(win,text="ENTER YOUR URL",fg="green",bg="lavender",width=30,height=7,font="times 20 bold")
lable1.place(x=683, y=200, anchor="center")

url=Entry(win)
url.place(x=683,y=280,height=30,width=200,anchor="center")

lable2=Label(win,text="ENTER YOUR QR NAME:",fg="#1400c6",bg="lavender",width=30,height=7,font="times 15 bold")
lable2.place(x=340, y=370, anchor="center")

qr_name=Entry(win)
qr_name.place(x=700,y=370,height=50,width=200,anchor="center")

lable3=Label(win,text="CHOOSE QR COLOR:",fg="#1400c6",bg="lavender",width=30,height=5,font="times 12 bold")
lable3.place(x=340, y=500, anchor="center")

c_color=Entry(win)
c_color.place(x=700,y=500,height=40,width=200,anchor="center")

btn1 = Button(win, text="GENERATE", font="times 20 bold", command=lambda:generate_qrcode(url.get(),qr_name.get(),c_color.get()), fg="red", bg="white", padx=20, pady=15)
btn1.place(x=683, y=600, anchor="center")  
win.mainloop()