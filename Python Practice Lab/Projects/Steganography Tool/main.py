from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb


root=Tk()
root.title("Steganography - Hide Secret Messages In Image")
root.geometry("1240x720+150+180")
root.resizable(False, False)
root.configure(background="#0f0f0f")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title = "Select an image File",
                                        filetypes=(("PNG file","*.png"),
                                        ("JPG file","*.jpg"), ("All file","*.txt")))
    img = Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=400,height=350,)
    lbl.image=img

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename), message)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END, clear_message)

def save():
    secret.save("hidden.png")



#icon
image_icon= PhotoImage(file="anony.png")
root.iconphoto(False, image_icon)


#LOGO
logo=PhotoImage(file="egg.png")
Label(root,image=logo,bg='#2f4155').place(x=20,y=20)
Label(root,text="Cyber Forensics", background="#0f0f0f",fg="white",font=('ariel 25 bold')).place(x=120, y=45)


#First Frame
f=Frame(root,bd=3,bg="black",width=580,height=400,relief=GROOVE)
f.place(x=20,y=150)

lbl=Label(f,bg="black")
lbl.place(x=80, y=30)

#Second Frame
frame2=Frame(root,bd=3,width=580,height=400,bg="black",relief=GROOVE)
frame2.place(x=640,y=150)

text1=Text(frame2, font="Roboto 20", bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0, y=0, width=580, height=400)

Scrollbar1=Scrollbar(frame2)
Scrollbar1.place(x=560,y=0,height=400)

Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

#third Frame

frame3=Frame(root,bd=3,bg="black",width=580,height=100,relief=GROOVE)
frame3.place(x=20,y=585)

Button(frame3,text="Open Image", width=16, height=2, font= "arial 15 bold", command=showimage).place(x=30,y=15)
Button(frame3,text="Save Image", width=16, height=2, font= "arial 15 bold", command=save).place(x=340,y=15)


#Fourth Frame

frame4=Frame(root,bd=3,bg="black",width=580,height=100,relief=GROOVE)
frame4.place(x=640,y=585)

Button(frame4,text="Encrypt", width=16, height=2, font= "arial 15 bold", command=Hide).place(x=30,y=15)
Button(frame4,text="Decrypt", width=16, height=2, font= "arial 15 bold", command=Show).place(x=340,y=15)
























root.mainloop()

