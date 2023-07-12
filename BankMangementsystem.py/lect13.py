from tkinter import *


root=Tk()
root.geometry("455x230")
root.title("ScrollBar tutorial")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill="y")

text=Text(root,yscrollcommand=Scrollbar.set)
text.pack(fill="both")

scrollbar.config(command=text.yview,width=20)

root.mainloop()
