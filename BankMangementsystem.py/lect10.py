from tkinter import *
import tkinter.messagebox as tmsg

def getdollar():
    print(f"We have credited {myslider2.get()} amount in your bak account")
    tmsg.showinfo("Amount Credited",f"We have credited {myslider2.get()} dollars in your bak account")

root=Tk()
root.geometry("455x233")
root.title("Slider Tutorial")

# myslider=Scale(root,from_=0, to=455)
# myslider.pack()


Label(root,text="How many dollars do you want?").pack()

myslider2=Scale(root,from_=0, to=100,orient=HORIZONTAL,tickinterval=25)
# myslider2.set(450)   # TODO: it set the value in slider
myslider2.pack()

Button(root,text="Get Dollars!",pady=10,command=getdollar).pack()
root.mainloop()





