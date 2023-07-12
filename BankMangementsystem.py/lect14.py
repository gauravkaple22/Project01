from tkinter import *
import tkinter.messagebox as tmsg


def Upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now...")


root=Tk()
root.geometry("455x230")
root.title("StatusBar tutorial")

statusvar = StringVar()
statusvar.set("Ready..")
sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)

Button(root,text="Upload",command=Upload).pack()

root.mainloop()
