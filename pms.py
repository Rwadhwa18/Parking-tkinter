from tkinter import *

root = Tk()
root.geometry("1080x720")
root.title("Python Project")
Label(root, font="comicsansms 13 bold",pady=15,).grid(column=7)

frame = LabelFrame(root,text="PARKING WALA", padx=10,pady=5)
frame.grid(padx=150,pady=10)

def login():
    print("rediecting you to loging page")
    

def rag():
    print("rediecting you to Ragisteration page")
    

def parking():
    print("available lots are BLOCK_34 , BLOCK_26, and BH_6")

b1 = Button(frame,bg="blue",fg="black", text="Login",padx=40, pady=10,command=login).grid(row=4,column=6)
b2 = Button(frame,bg="blue",fg="black", text="Ragister",padx=40,pady=10, command=rag).grid(row=4,column=7)
b3 = Button(frame,bg="blue",fg="black", text="Available Parking",padx=40, pady=10,command=parking).grid(row=4,column=8)

root.mainloop()