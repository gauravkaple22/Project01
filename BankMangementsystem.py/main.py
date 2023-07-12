from tkinter import *
from PIL import Image, ImageTk
import datetime
import tkinter.messagebox as tmsg
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
import random
import re


class AdminLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x550")
        self.root.configure(bg="pink")
        self.root.title("Bank Management System")

        self.font_style = ("Arial", 11, "bold")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 900) // 2
        y = (screen_height - 550) // 2

        self.root.geometry(f"900x550+{x}+{y}")

        self.f1 = Frame(self.root, background="grey", highlightbackground="black", highlightthickness=2)
        self.f1.pack(pady=15, padx=2)
        self.l = Label(self.f1, text="Admin Login", font="lucida 25 bold")
        self.l.pack(side=LEFT)

        self.image = Image.open("customer.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.gk_label = Label(image=self.photo, width=190, height=210, padx=100, pady=150)
        self.gk_label.pack(side=LEFT, padx=70, anchor="n", pady=50)

        self.f2 = Frame(self.root, bg="pink")
        self.f2.pack(pady=5)

        self.var1 = StringVar()
        self.var2 = StringVar()

        self.l1 = Label(self.f2, text="Username", font="Arial 20 bold", justify=LEFT, borderwidth=2, relief=SOLID,
                        highlightcolor="red")
        self.l1.grid(row=0, column=0, sticky="w", padx=50, pady=55)
        self.e1 = Entry(self.f2, textvariable=self.var1, relief=SUNKEN, font="Helvetica 15 bold",
                        highlightbackground="red", highlightthickness=2)
        self.e1.grid(row=0, column=1, padx=15, pady=10, sticky="w")

        self.l2 = Label(self.f2, text="Password", font="Arial 20 bold", borderwidth=2, relief=SOLID,
                        highlightcolor="red")
        self.l2.grid(row=1, column=0, sticky="w", padx=50, pady=40)
        self.e2 = Entry(self.f2, textvariable=self.var2, relief=SUNKEN, show="*", font="Helvetica 15 bold",
                        highlightbackground="red", highlightthickness=2)
        self.e2.grid(row=1, column=1, padx=15, pady=10, sticky="w")

        self.btn = Button(self.root, text="LOGIN", padx=25, pady=5, bg="yellow", highlightthickness=3, command=lambda: self.fuc1(), state=DISABLED)
        self.btn.pack(padx=15, pady=20)

        self.datetime_label = Label(self.root, font="Arial 14", pady=5, highlightbackground="green", fg="magenta")
        self.datetime_label.pack(side=BOTTOM, padx=10, pady=20, anchor="ne")

        self.update_datetime()

        # TODO: These used to bind the function non_emp_input to StringVar variables.....
        self.var1.trace("w", self.non_emp_input)
        self.var2.trace("w", self.non_emp_input)

    def update_datetime(self):
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.datetime_label.config(text="Date and Time: " + current_datetime)
        self.datetime_label.after(1000, self.update_datetime)

    def user_check(self):
        My_username = "gaurav"
        username = self.e1.get()

        if username == My_username:
            return True
        else:
            return False

    def non_emp_input(self, *args):
        if self.var1.get() and self.var2.get():
            self.btn.config(state=NORMAL)
        else:
            self.btn.config(state=DISABLED)

    def pass_check(self):
        My_password = "7777"
        password = self.e2.get()

        if password == My_password:
            return True
        else:
            return False

    def fuc1(self):
        uc = self.user_check()
        pc = self.pass_check()

        if uc and pc:
            self.root.withdraw()
            self.open_secondary_gui()
        else:
            tmsg.showerror("Error", "Incorrect username or password")

    def open_secondary_gui(self):
        sec_gui1 = Toplevel(self.root)
        secondary_gui = SecondaryGUI(sec_gui1)


class SecondaryGUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="pink")
        self.root.geometry("900x550")
        self.root.title("Bank Management System")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 900) // 2
        y = (screen_height - 550) // 2

        self.root.geometry(f"900x550+{x}+{y}")

        f12 = Frame(self.root, background="grey", highlightbackground="black", highlightthickness=2)
        f12.grid(pady=5, padx=280)
        l12 = Label(f12, text="CUSTOMER INFORMATION", font="lucida 20 bold")
        l12.grid()

        frame_width = self.root.winfo_width()
        frame_height = self.root.winfo_height()
        f13 = Frame(self.root, bg="pink", width=frame_width, height=frame_height)
        f13.grid(pady=5)

        l13 = Label(f13, text="FIRST NAME", font="Arial 15 bold")
        l13.grid(row=0, column=0, sticky="W", pady=20, padx=10)
        self.e13 = Entry(f13, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2)
        self.e13.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        l14 = Label(f13, text="LAST NAME", font="Arial 15 bold")
        l14.grid(row=1, column=0, sticky="W", pady=20, padx=10)
        self.e14 = Entry(f13, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2)
        self.e14.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        l15 = Label(f13, text="MOBILE NUMBER", font="Arial 15 bold")
        l15.grid(row=2, column=0, sticky="W", pady=20, padx=10)
        self.e15 = Entry(f13, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2)
        self.e15.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        # self.e15.bind("<KeyRelease>", lambda event: self.validate())

        l16 = Label(f13, text="DOB", font="Arial 15 bold")
        l16.grid(row=3, column=0, sticky="W", pady=20, padx=10)
        self.dob_entry = DateEntry(f13, width=15, background='blue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy', font="Helvetica 15 bold")
        self.dob_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        l17 = Label(f13, text="STATE", font="Arial 15 bold")
        l17.grid(row=4, column=0, sticky="W", pady=20, padx=10)
        self.state = ttk.Combobox(f13, values=("Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
                                               "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
                                                "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
                                                "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
                                                "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
                                                "West Bengal"), font="Helvetica 12 bold")
        self.state.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        l18 = Label(f13, text="CITY", font="Arial 15 bold")
        l18.grid(row=5, column=0, sticky="W", pady=20, padx=10)
        self.e18 = Entry(f13, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2)
        self.e18.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        self.btn11 = Button(f13, text="REGISTER", padx=25, pady=5, bg="yellow", highlightthickness=3, command=self.save_customer_information,state=DISABLED)
        self.btn11.grid(row=6, column=0, padx=15, pady=20)

        self.btn12 = Button(f13, text="NEXT", padx=25, pady=5, bg="orange", highlightthickness=3,command=self.next_page)
        self.btn12.grid(row=6, column=1, padx=12, pady=25)

        self.e13.bind("<KeyRelease>", lambda event: self.validate())
        self.e14.bind("<KeyRelease>", lambda event: self.validate())
        self.e15.bind("<KeyRelease>", lambda event: self.validate())
        self.dob_entry.bind("<<DateEntrySelected>>", lambda event: self.validate())
        self.state.bind("<<ComboboxSelected>>", lambda event: self.validate())
        self.e18.bind("<KeyRelease>", lambda event: self.validate())

    def validate(self):
        first_name = self.e13.get()
        last_name = self.e14.get()
        mobile_number = self.e15.get()
        state = self.state.get()
        city = self.e18.get()

        if first_name and last_name and mobile_number and state and city:
            if re.match(r"^[6-9]\d{9}$", mobile_number):
                self.btn11.configure(state=NORMAL)
            else:
                self.btn11.configure(state=DISABLED)
                tmsg.showerror("Invalid Input", "Please enter a valid 10-digit mobile number and starting from 6-9.")
        else:
            self.btn11.configure(state=DISABLED)

    def get_dob(self):
        dob = self.dob_entry.get_date()
        dob.config(text="Date of Birth: " + dob.strftime("%Y-%m-%d"))

    def save_customer_information(self):
        first_name = self.e13.get()
        last_name = self.e14.get()
        mobile_number = self.e15.get()
        dob = self.dob_entry.get_date().strftime("%Y-%m-%d")
        state = self.state.get()
        city = self.e18.get()

        if len(mobile_number) == 10 and mobile_number.isdigit():
            connection1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="lucifer*7812",
                database="bms_data"
            )

            cursor1 = connection1.cursor()

            insert_query1 = "INSERT INTO customer_information1 (first_name, last_name, mobile_number, dob, state, city) " \
                            "VALUES (%s, %s, %s, %s, %s, %s)"

            cursor1.execute(insert_query1, (first_name, last_name, mobile_number, dob, state, city))

            connection1.commit()

            cursor1.close()
            connection1.close()
            tmsg.showinfo("Success", "Customer information saved successfully! and Click Next To Proceed")
        else:
            tmsg.showerror("Invalid Input", "Please enter a valid 10-digit mobile number.")

    def next_page(self):
        self.root.destroy()
        BankManagementSystem()


class BankManagementSystem:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x600")
        self.root.configure(bg="grey")
        self.root.title("Bank Management System")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 900) // 2
        y = (screen_height - 600) // 2

        self.root.geometry(f"900x600+{x}+{y}")

        self.f21 = Frame(self.root, background="grey", highlightbackground="black", highlightthickness=2)
        self.f21.grid(pady=25, padx=280)
        self.l21 = Label(self.f21, text="USER VERIFICATION", font="lucida 25 bold", fg="black",width=20)
        self.l21.grid()

        self.f31 = Frame(self.root, bg="grey")
        self.f31.grid(pady=5)

        self.l31 = Label(self.f31, text="Captcha", font="Arial 15 bold")
        self.l31.grid(row=0, column=0, sticky="W", pady=40, padx=10)
        self.captcha_label = Label(self.f31, font="Arial 15 bold",width=10,bg="yellow")
        self.captcha_label.grid(row=0, column=1, pady=40, padx=10, sticky="w")

        self.l41 = Label(self.f31, text="Input Captcha", font="Arial 15 bold")
        self.l41.grid(row=1, column=0, sticky="W", pady=40, padx=10)
        self.captcha_entry = Entry(self.f31, relief=SUNKEN, font="Helvetica 15 bold", highlightbackground="black", highlightthickness=2, show="*",bg="pink")
        self.captcha_entry.grid(row=1, column=1, padx=10, pady=30, sticky="w")

        self.btn21 = Button(self.f31, text="PROCEED", padx=25, pady=5, bg="pink", highlightthickness=3, fg="black", command=self.fuc1)
        self.btn21.grid(row=2, columnspan=2, pady=30, sticky="ns")

        self.generate_captcha()

    def generate_captcha(self):
        captcha = random.randint(10000000, 99999999)
        self.captcha_label.config(text=f"{captcha}")
        self.captcha_entry.delete(0, END)

    def fuc1(self):
        captcha_input = self.captcha_entry.get()
        generated_captcha = int(self.captcha_label.cget("text"))

        if int(captcha_input) == generated_captcha:
            tmsg.showinfo("Success", "Correct Captcha")
            self.root.destroy()
            BankManagementSystem1()
        else:
            tmsg.showerror("Invalid Input", "Incorrect Captcha")
            self.generate_captcha()

    def run(self):
        self.root.mainloop()


class BankManagementSystem1:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x550")
        self.root.configure(bg="pink")
        self.root.title("Bank Management System")

        self.balance = 0
        self.transaction_history = []
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 970) // 2
        y = (screen_height - 550) // 2

        self.root.geometry(f"970x550+{x}+{y}")
        self.create_gui()

    def create_gui(self):
        l31 = Label(self.root, text="Bank Management System", font=("Arial", 20, "bold"),bg="orange")
        l31.grid(row=0, column=0, columnspan=2, pady=20,padx=310)

        deposit_button = Button(self.root, text="Deposit Amount", command=self.deposit_amount, bg="lightblue", fg="black", font=("Arial", 14, "bold"))
        deposit_button.grid(row=2, column=0, padx=10, pady=60, sticky="ew")

        withdraw_button = Button(self.root, text="Withdraw Amount", command=self.withdraw_amount, bg="lightgreen", fg="black", font=("Arial", 14, "bold"))
        withdraw_button.grid(row=2, column=1, padx=10, pady=60, sticky="ew")

        balance_button = Button(self.root, text="Check Balance", command=self.check_balance, bg="lightyellow", fg="black", font=("Arial", 14, "bold"))
        balance_button.grid(row=3, column=0, padx=10, pady=25, sticky="ew")

        history_button = Button(self.root, text="View Transaction History", command=self.view_transaction_history, bg="lightpink", fg="black", font=("Arial", 14, "bold"))
        history_button.grid(row=3, column=1, padx=10, pady=25, sticky="ew")

        logout_button = Button(self.root, text="Logout", command=self.root.quit, bg="red", fg="white", font=("Arial", 14, "bold"))
        logout_button.grid(row=4, column=0, columnspan=2, padx=370, pady=25, sticky="ew")

    def deposit_amount(self):
        amount = self.get_input("Enter amount to deposit:")
        if amount:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            tmsg.showinfo("Success", "Amount deposited successfully!")

    def withdraw_amount(self):
        amount = self.get_input("Enter amount to withdraw:")
        if amount:
            if amount <= self.balance:
                self.balance -= amount
                self.add_transaction("Withdrawal", -amount)
                tmsg.showinfo("Success", "Amount withdrawn successfully!")
            else:
                tmsg.showerror("Insufficient Balance", "Insufficient balance in your account.")

    def check_balance(self):
        tmsg.showinfo("Balance", f"Your current balance is: {self.balance}")

    def view_transaction_history(self):
        history_text = "\n".join(self.transaction_history)
        tmsg.showinfo("Transaction History", f"Transaction History:\n{history_text}")

    def get_input(self, message):
        input_dialog = Toplevel(self.root,bg="cyan")
        input_dialog.title("Enter Amount")
        input_dialog.geometry("400x200")

        label = Label(input_dialog, text=message)
        label.pack()

        amount_entry = Entry(input_dialog,bg="grey",font="helvetica 14 bold")
        amount_entry.pack(pady=15)

        submit_button = Button(input_dialog, text="Submit", command=lambda: self.process_input(amount_entry),bg="yellow")
        submit_button.pack()

        input_dialog.wait_window()

        if hasattr(self, "input_value"):
            return self.input_value

    def process_input(self, entry_widget):
        self.input_value = int(entry_widget.get())
        entry_widget.get()
        entry_widget.master.destroy()

    def add_transaction(self, transaction_type, amount):
        transaction = f"{transaction_type}: {amount}"
        self.transaction_history.append(transaction)

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lucifer*7812",
            database="bms_data"
        )
        cursor = connection.cursor()

        insert_query = "INSERT INTO transaction_history  (transaction_type, amount) VALUES (%s, %s)"
        values = (transaction_type, amount)
        cursor.execute(insert_query, values)

        connection.commit()

        cursor.close()
        connection.close()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    Admin_Login = AdminLogin(root)
    root.mainloop()
