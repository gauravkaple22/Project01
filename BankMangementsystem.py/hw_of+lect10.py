from tkinter import *
import tkinter.messagebox as tmsg


def rate():
    print(f"You Rate The Adipurush Movie {myslider3.get()} Out OOf 10")
    with open("abc.txt","a") as f:
        f.write(f"You Rate The Adipurush Movie {myslider3.get()} Out OOf 10")
    tmsg.showinfo("Rate Us","Thank You For Rating!")

root=Tk()
root.geometry("455x233")
root.title("Slider Tutorial")

Label(root,text="How Will You Rate Adipurush Movie On The Scale Of 10 ").pack()

myslider3=Scale(root,from_=0,to=10,orient=HORIZONTAL)
myslider3.pack()

Button(root,text="Submit!",pady=10,command=rate).pack()


root.mainloop()
