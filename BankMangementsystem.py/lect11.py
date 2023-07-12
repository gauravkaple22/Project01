from tkinter import *
import tkinter.messagebox as tmsg


def order():
    tmsg.showinfo(f"order received",f"We have received your order for {var.get()}. Thanks for ordering!")


root=Tk()
root.geometry("455x230")
root.title("RadioButton tutorial")

var=IntVar()


Label(root,text="what would you like to have sir?",justify=LEFT,padx=14,font="lucida 14 bold").pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=1)
radio.pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value=2)
radio.pack(anchor="w")
radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value=3)
radio.pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value=4)
radio.pack(anchor="w")

Button(root,text="order Now",command=order).pack()

root.mainloop()
