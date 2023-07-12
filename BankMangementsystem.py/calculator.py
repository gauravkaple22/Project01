from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root=Tk()
root.geometry("644x800")
root.title("Calculator by GK")
root.config(background="pink")

scvalue=StringVar()
scvalue.set("")

screen=Entry(root,textvariable=scvalue,font="lucida 40 bold",)
screen.pack(fill=X,ipadx=8,pady=4,padx=15)


f=Frame(root,background="grey",highlightbackground="black",highlightthickness=2)
b=Button(f,text="9",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="8",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="7",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,background="grey",highlightbackground="black",highlightthickness=2)
b=Button(f,text="6",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="5",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="4",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,background="grey",highlightbackground="black",highlightthickness=2)
b=Button(f,text="3",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="1",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,background="grey",highlightbackground="black",highlightthickness=2)
b=Button(f,text="0",font="lucida 30 bold",padx=19,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",font="lucida 30 bold",padx=21,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",font="lucida 30 bold",padx=21,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,background="grey",highlightbackground="black",highlightthickness=2)
b=Button(f,text="C",font="lucida 30 bold",padx=17,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="lucida 30 bold",padx=17,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="#",font="lucida 30 bold",padx=17,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,background="grey",highlightbackground="black",highlightthickness=2)
b=Button(f,text="/",font="lucida 30 bold",padx=25,pady=10)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="%",font="lucida 30 bold",padx=14,pady=10)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="=",font="lucida 30 bold",padx=17,pady=10)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()
