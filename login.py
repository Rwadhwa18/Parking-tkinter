from tkinter import *

root = Tk()
root.geometry("1080x720")
root.title("Python Project")
Label(root, font="comicsansms 13 bold",pady=15,).grid(column=7)

frame = LabelFrame(root,text="PARKING WALA", padx=10,pady=5)
frame.grid(padx=150,pady=10)

name = Label(frame,text="User Name")
passw = Label(frame,text="Password")
name.grid(row=1,column=2)
passw.grid(row=2,column=2)

namevalue = StringVar()
passwvalue = StringVar()

nameentry = Entry(frame,textvariable=namevalue)
passwentry = Entry(frame,textvariable=passwvalue)

nameentry.grid(row=1,column=7)
passwentry.grid(row=2,column=7)

def hello():
    print("sajkf")

b2 = Button(frame,bg="blue",fg="black", text="Login",padx=40, command=hello).grid(row=4,column=7)
b3 = Button(frame,bg="blue",fg="black", text="New User",padx=40,command=hello).grid(row=4,column=8)

root.mainloop()