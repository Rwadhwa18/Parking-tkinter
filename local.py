from tkinter import *
from tkinter import messagebox


root3 = Tk()
root3.geometry("1080x720")
root3.title("Python Project")
frame3 = LabelFrame(root3, text="PARKING WALA", padx=10, pady=5)
frame3.grid(padx=150, pady=10)
root3 = Tk()
root3.geometry("700x300")
root3.title("Python Project")
frame3 = LabelFrame(root3, text="PARKING WALA", padx=10, pady=5)
frame3.grid(padx=150, pady=10)
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

# checkbox
#chek1 = Checkbutton(frame,text="Male",variable=accept_male).grid(row=4,column=6)
#chek2 = Checkbutton(frame,text="Female",variable=accept_female).grid(row=4,column=7)

radio_gender = Radiobutton(frame3, text="Male", variable=gender, value=1).grid(row=4, column=6)
radio_gender2 = Radiobutton(frame3, text="FeMale", variable=gender, value=2).grid(row=4, column=7)


def hello():
    if regvalue.get() == "":
       messagebox.showinfo("submited","you are registered")
       
       print("Reg No. is compulsory")
    else:
       
        print(
            f"Your Reg. No is {regvalue.get()}, Your DATA has been registered Confirm Your name {namevalue.get()} ")
    with open("records.text", "w") as f:
        f.write(f"({regvalue.get()},{namevalue.get()},{phonevalue.get()})")
b1 = Button(frame3, bg="blue", fg="black", text="Submit",padx=40, command=hello).grid(row=7, column=7)
root3.mainloop()            