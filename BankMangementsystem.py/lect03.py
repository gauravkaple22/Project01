from tkinter import *

root=Tk()
root.geometry("455x333")

root.title("Registration Form For Dancing Club")

def getvals():
    print("The Value Of Username Is:-",user_value.get())
    print("The Value Of Password Is:-",pass_value.get())
    print("The Value Of Gmail Is:-",Gmail_value.get())


User=Label(root,text="Username")
User.grid()

Password=Label(root,text="Password")
Password.grid(row=1)

Gmail=Label(root,text="Gmail")
Gmail.grid(row=2)


user_value = StringVar()
pass_value = StringVar()
Gmail_value=StringVar()

userEntry=Entry(root,textvariable=user_value)
passEntry=Entry(root,textvariable=pass_value)
Gmail_Entry=Entry(root,textvariable=Gmail_value)

userEntry.grid(row=0,column=1)
passEntry.grid(row=1,column=1)
Gmail_Entry.grid(row=2,column=1)

b=Button(text="Submit",command=getvals,bg="grey")
b.grid(row=4,column=1)

root.mainloop()
