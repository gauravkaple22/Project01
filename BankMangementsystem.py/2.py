from tkinter import *
import tkinter.messagebox as tmsg


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

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    bms = BankManagementSystem1()
    bms.run()
