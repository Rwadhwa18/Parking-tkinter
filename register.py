from tkinter import *

root = Tk()
root.geometry("1080x720")
root.title("Python Project")
root.aspect
Label(root, pady=15).grid(column=7)

frame = LabelFrame(root,fg="grey", text="PARKING WALA", padx=50, pady=50)
frame.grid(padx=250, pady=150)


name = Label(frame, text="Name")
reg = Label(frame, text="Reg. No.")
hostel = Label(frame, text="Hostel/Block")
gender = Label(frame, text="Gender")
phone = Label(frame, text="Mobile no")
email = Label(frame, text="Email Id")


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
nameentry = Entry(frame, textvariable=namevalue)
regentry = Entry(frame, textvariable=regvalue)
hostelentry = Entry(frame, textvariable=hostelvalue)
phoneentry = Entry(frame, textvariable=phonevalue)
emailentry = Entry(frame, textvariable=emailvalue)

# Paking the Entries
nameentry.grid(row=1, column=7)
regentry.grid(row=2, column=7)
hostelentry.grid(row=3, column=7)
phoneentry.grid(row=5, column=7)
emailentry.grid(row=6, column=7)


def hello():

    if regvalue.get() == "":
        print("Reg No. is compulsory")
    else:

        print(
            f"Your Reg. No is {regvalue.get()}, Your DATA has been registered Confirm Your name {namevalue.get()} ")
    with open("records.text", "w") as f:
        f.write(f"({regvalue.get()}, {namevalue.get()}, {phonevalue.get()}, {emailvalue.get()})")


# Button
b1 = Button(frame, bg="blue", fg="black", text="Submit",
            padx=40, command=hello).grid(row=7, column=7)

# checkbox
#chek1 = Checkbutton(frame,text="Male",variable=accept_male).grid(row=4,column=6)
#chek2 = Checkbutton(frame,text="Female",variable=accept_female).grid(row=4,column=7)
radio_gender = Radiobutton(
    frame, text="Male", variable=gender, value=1).grid(row=4, column=6)
radio_gender2 = Radiobutton(
    frame, text="FeMale", variable=gender, value=2).grid(row=4, column=7)
root.mainloop()
