from tkinter import *

root = Tk()
root.geometry("1080x720")
root.title("Python Project")
Label(root, font="comicsansms 13 bold",pady=15,).grid(column=7)

frame = LabelFrame(root,text="PARKING WALA", padx=100,pady=5)
frame.grid(padx=150,pady=10)

reg = Label(frame,text="Reg. No.")
hostel = Label(frame,text="Block")
pricing = Label(frame,text="Price")


menubutton1 = Menubutton(frame, text = "Choose Block")
menubutton2 = Menubutton(frame, text = "In Rs.")

reg.grid(row=2,column=2)
hostel.grid(row=3,column=2)
pricing.grid(row=4,column=2)

menubutton1.menu = Menu(menubutton1)
menubutton1["menu"]= menubutton1.menu
#
menubutton2.menu = Menu(menubutton2)
menubutton2["menu"]= menubutton2.menu


regvalue = StringVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()


regentry = Entry(frame,textvariable=regvalue)
menubutton1.menu.add_checkbutton(label = "BH_1",
                                variable = var1)  
menubutton1.menu.add_checkbutton(label = "BLOCK_33",
                                variable = var2)
menubutton1.menu.add_checkbutton(label = "BLOCK_26",
                                variable = var3)
#
menubutton2.menu.add_checkbutton(label = "20",
                                variable = var1)  
menubutton2.menu.add_checkbutton(label = "30",
                                variable = var2)
menubutton2.menu.add_checkbutton(label = "35",
                                variable = var3)                                


b1 = Button(frame,bg="blue",fg="black", text="order",padx=40, command="").grid(row=7,column=7)


regentry.grid(row=2,column=7)
menubutton1.grid(row=3,column=7)
menubutton2.grid(row=4,column=7)

#with open("records.text", "w") as f:
 #           f.write(f"({regvalue.get()},{namevalue.get()},{phonevalue.get()})")

root.mainloop()