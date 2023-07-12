from tkinter import *


def gvk(event):
    print(f"You Click On The Button at {event.x},{event.y}")


root=Tk()
root.title("Events in tkinter")
root.geometry("644x334")

widget=Button(root,text="Click me please")
widget.pack()

widget.bind('<Button-1>',gvk)
widget.bind('<Double-1>',quit)


root.mainloop()
