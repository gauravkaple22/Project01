from tkinter import *
from tkcalendar import DateEntry
import tkinter.messagebox as tmsg
from tkinter import ttk


def get_dob():
    dob = dob_entry.get_date()
    l16.config(text="Date of Birth: " + dob.strftime("%Y-%m-%d"))


def validate():
    first_name = e13.get()
    last_name = e14.get()
    mobile_number = e15.get()
    dob = dob_entry.get_date()
    state = e17.get()
    city = e18.get()

    if first_name and last_name and mobile_number and dob and state and city:
        if len(mobile_number) == 10 and mobile_number.isdigit():
            btn11.config(state=NORMAL)
        else:
            btn11.config(state=DISABLED)
            tmsg.showerror("Invalid Input", "Please enter a valid 10-digit mobile number.")
    else:
        btn11.config(state=DISABLED)


root = Tk()
root.geometry("900x600")
root.configure(bg="grey")
root.title("Bank Management System")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 900) // 2
y = (screen_height - 600) // 2
root.geometry(f"900x600+{x}+{y}")


f12 = Frame(root, background="grey", highlightbackground="black", highlightthickness=2)
f12.grid(pady=5, padx=280)
l12 = Label(f12, text="CUSTOMER INFORMATION", font="lucida 20 bold")
l12.grid()


frame_width = root.winfo_width()
frame_height = root.winfo_height()
f13 = Frame(root, bg="grey", width=frame_width, height=frame_height)
f13.grid(pady=5)


l13 = Label(f13, text="FIRST NAME", font="Arial 15 bold")
l13.grid(row=0, column=0, sticky="W", pady=20, padx=10)
e13 = Entry(f13, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2)
e13.grid(row=0, column=1, padx=10, pady=10, sticky="w")


l14 = Label(f13, text="LAST NAME", font="Arial 15 bold")
l14.grid(row=1, column=0, sticky="W", pady=20, padx=10)
e14 = Entry(f13, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2)
e14.grid(row=1, column=1, padx=10, pady=10, sticky="w")


l15 = Label(f13, text="MOBILE NUMBER", font="Arial 15 bold")
l15.grid(row=2, column=0, sticky="W", pady=20, padx=10)
e15 = Entry(f13, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2)
e15.grid(row=2, column=1, padx=10, pady=10, sticky="w")
e15.bind("<KeyRelease>", lambda event: validate())


l16 = Label(f13, text="DOB", font="Arial 15 bold")
l16.grid(row=3, column=0, sticky="W", pady=20, padx=10)
dob_entry = DateEntry(f13, date_pattern='yyyy-mm-dd')
dob_entry.configure(width=25,font="Arial 11 bold")
dob_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")


l17 = Label(f13, text="STATE", font="Arial 15 bold")
l17.grid(row=4, column=0, sticky="W", pady=20, padx=10)
state = ttk.Combobox(f13, font="Helvetica 15 bold",background="red")
state['values'] = ( "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar","Chhattisgarh","Goa",  "Gujarat",
                         "Haryana","Himachal Pradesh", "Jharkhand","Karnataka", "Kerala","Madhya Pradesh", "Maharashtra",
                         "Manipur",  "Meghalaya", "Mizoram",  "Nagaland", "Odisha", "Punjab",  "Rajasthan", "Sikkim",
                         "Tamil Nadu", "Telangana",  "Tripura", "Uttar Pradesh","Uttarakhand", "West Bengal")
state.grid(row=4, column=1, padx=10, pady=10, sticky="w")


l18 = Label(f13, text="CITY", font="Arial 15 bold")
l18.grid(row=5, column=0, sticky="W", pady=20, padx=10)
e18 = Entry(f13, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2)
e18.grid(row=5, column=1, padx=10, pady=10, sticky="w")


btn11 = Button(f13,text="REGISTER",padx=25,pady=5,bg="yellow",highlightthickness=3,command=validate,state=DISABLED)
btn11.grid(row=6,column=0,padx=15,pady=20)


btn12 = Button(f13,text="ALREADY REGISTER?",padx=25,pady=5,bg="orange",highlightthickness=3)
btn12.grid(row=6,column=1,padx=12,pady=25)


root.mainloop()
