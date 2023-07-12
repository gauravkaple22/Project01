# travel Form

from tkinter import *

root =  Tk()
root.geometry("600x350")


def getvals():
    print("SSubmitting Form")
    print(f"{ nameValue.get(),phoneValue.get(),genderValue.get(),contactValue.get() ,payValue.get(), foodValue.get()}")

    with open("records.txt","w")as f:
        f.write(f"{ nameValue.get(),phoneValue.get(),genderValue.get(),contactValue.get() ,payValue.get(), foodValue.get()}\n0")


Label(root,text="Welcome To GK Travels",font="comicsansms 13 bold").grid(row=0, column=3, pady=15)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
contact=Label(root,text="Emergency Contact")
pay=Label(root,text="Payment Mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
contact.grid(row=4,column=2)
pay.grid(row=5,column=2)


nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
contactValue = StringVar()
payValue = StringVar()
foodValue=IntVar()

name_entry=Entry(root,textvariable=nameValue)
phone_entry=Entry(root,textvariable=phoneValue)

gender_entry=Entry(root,textvariable=genderValue)
contact_entry=Entry(root,textvariable=contactValue)
pay_entry=Entry(root,textvariable=payValue)


name_entry.grid(row=1 ,column=3)
phone_entry.grid(row=2 ,column=3)
gender_entry.grid(row=3 ,column=3)
contact_entry.grid(row=4 ,column=3)
pay_entry.grid(row=5 ,column=3)

foodValue1=Checkbutton(text="Want To Prebook Your Meal...",variable=foodValue)
foodValue1.grid(row=6,column=3,pady=5)


Button(text="Submit To GK Travel",command=getvals).grid(row=7,column=3)


root.mainloop()
