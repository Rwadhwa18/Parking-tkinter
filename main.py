from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("1080x720")
root.title("Python Project")

photo = PhotoImage(file="23.png")

pts_label = Label(root,image=photo)
pts_label.grid(row=1,column=0)

frame = LabelFrame(root, text="PARKING WALA", padx=10, pady=5)
frame.grid(padx=150, pady=20)



def login():
    print("rediecting you to loging page")
    root2 = Tk()
    root2.geometry("700x300")
    root2.title("Python Project")
    frame2 = LabelFrame(root2, text="PARKING WALA", padx=10, pady=5)
    frame2.grid(padx=150, pady=10)
    name = Label(frame2, text="User Name")
    passw = Label(frame2, text="Password")
    name.grid(row=1, column=2)
    passw.grid(row=2, column=2)

    namevalue = StringVar()
    passwvalue = StringVar()
    ####------
    def on_entry(e):
        nameentry.delete(0,'end')
    def on_leave(e):
        if nameentry.get()=='':
            nameentry.insert(0,'Name')
    
    
    nameentry = Entry(frame2, textvariable=namevalue)
    nameentry.insert(0,'Name')
    nameentry.bind("<FocusIn>",on_entry)
    nameentry.bind("<FocusIn>",on_leave)

    passwentry = Entry(frame2, textvariable=passwvalue)
    passwentry.insert(0,'Password')
     

    nameentry.grid(row=1, column=7)
    passwentry.grid(row=2, column=7)

    b2 = Button(frame2, bg="blue", fg="black", text="Login",
                padx=40, command=parking).grid(row=4, column=7)
    b3 = Button(frame2, bg="blue", fg="black", text="New User", padx=40, command=rag).grid(row=4, column=8)

    root2.mainloop()


def rag():
    print("rediecting you to Registeration page")

    root3 = Tk()
    root3.geometry("700x300")
    root3.title("Python Project")
    frame3 = LabelFrame(root3, text="PARKING WALA", padx=10, pady=5)
    frame3.grid(padx=150, pady=10)
    def hello():
        if regvalue.get() == "":
           messagebox.showinfo("submited","you are registered")
           
           print("Reg No. is compulsory")
        else:
           
            print(
                f"Your Reg. No is {regvalue.get()}, Your DATA has been registered Confirm Your name {namevalue.get()} ")
        with open("records.text", "w") as f:
            f.write(f"({regvalue.get()},{namevalue.get()},{phonevalue.get()})")

    name = Label(frame3, text="Name")
    reg = Label(frame3, text="Reg. No.")
    hostel = Label(frame3, text="Hostel/Block")
    gender = Label(frame3, text="Gender")
    phone = Label(frame3, text="Mobile no")
    email = Label(frame3, text="Email Id")

    name.grid(row=1, column=2)
    reg.grid(row=2, column=2)
    hostel.grid(row=3, column=2)
    gender.grid(row=4, column=2)
    phone.grid(row=5, column=2)
    email.grid(row=6, column=2)

    # tkinter variable for storing entries
    namevalue = StringVar()
    regvalue = StringVar()
    hostelvalue = StringVar()
    phonevalue = StringVar()
    emailvalue = StringVar()

    # checkbox variable
    gender = IntVar()

    # Entries for our form
    nameentry = Entry(frame3, textvariable=namevalue)
    regentry = Entry(frame3, textvariable=regvalue)
    hostelentry = Entry(frame3, textvariable=hostelvalue)
    phoneentry = Entry(frame3, textvariable=phonevalue)
    emailentry = Entry(frame3, textvariable=emailvalue)

    # Paking the Entries
    nameentry.grid(row=1, column=7)
    regentry.grid(row=2, column=7)
    hostelentry.grid(row=3, column=7)
    phoneentry.grid(row=5, column=7)
    emailentry.grid(row=6, column=7)

    

    # Button
    b1 = Button(frame3, bg="blue", fg="black", text="Submit",padx=40, command=hello).grid(row=7, column=7)

    # checkbox
    #chek1 = Checkbutton(frame,text="Male",variable=accept_male).grid(row=4,column=6)
    #chek2 = Checkbutton(frame,text="Female",variable=accept_female).grid(row=4,column=7)
    
    radio_gender = Radiobutton(frame3, text="Male", variable=gender, value=1).grid(row=4, column=6)
    radio_gender2 = Radiobutton(frame3, text="FeMale", variable=gender, value=2).grid(row=4, column=7)
    root3.mainloop()


def parking():
    print("available lots are BLOCK_34 , BLOCK_26, and BH_6")
    root4 = Tk()
    root4.geometry("700x300")
    root4.title("Python Project")
    
    frame4 = LabelFrame(root4, text="PARKING WALA", padx=10, pady=5)
    frame4.grid(padx=150, pady=10)
    
    def parked():
        messagebox.showinfo("submited","your parking resquest submited")
        print(f"Your parking BLock is {var1}")

    rag = Label(frame4, text="Vehicle No.")
    hostel = Label(frame4, text="Block")
    pricing = Label(frame4, text="Price")

    menubutton1 = Menubutton(frame4, text="Choose Block")
    menubutton2 = Menubutton(frame4, text="In Rs.")

    rag.grid(row=2, column=2)
    hostel.grid(row=3, column=2)
    pricing.grid(row=4, column=2)

    menubutton1.menu = Menu(menubutton1)
    menubutton1["menu"] = menubutton1.menu
    #
    menubutton2.menu = Menu(menubutton2)
    menubutton2["menu"] = menubutton2.menu

    regvalue = StringVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()

    ragentry = Entry(frame4, textvariable=regvalue)
    menubutton1.menu.add_checkbutton(label="BH_1",variable=var1)
    menubutton1.menu.add_checkbutton(label="BLOCK_33", variable=var2)
    menubutton1.menu.add_checkbutton(label="BLOCK_26", variable=var3)
    #
    menubutton2.menu.add_checkbutton(label="20",variable=var1)
    menubutton2.menu.add_checkbutton(label="30", variable=var2)
    menubutton2.menu.add_checkbutton(label="35",variable=var3)

    b1 = Button(frame4, bg="blue", fg="black", text="order",
                padx=40, command=parked).grid(row=7, column=7)

    ragentry.grid(row=2, column=7)
    menubutton1.grid(row=3, column=7)
    menubutton2.grid(row=4, column=7)
    root4.mainloop()


b1 = Button(frame, bg="blue", fg="black", text="Login", padx=40,
            pady=10, command=login).grid(row=4, column=6)
b2 = Button(frame, bg="blue", fg="black", text="Ragister",
            padx=40, pady=10, command=rag).grid(row=4, column=7)
b3 = Button(frame, bg="blue", fg="black", text="Available Parking",
            padx=40, pady=10, command=parking).grid(row=4, column=8)

root.mainloop()