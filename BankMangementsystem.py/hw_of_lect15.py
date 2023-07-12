from tkinter import *


class GUI1(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("644x350")
        self.title("Quiz")

    def label(self):
        Label(self, text="Q.1) Who Is Big B ?",font="bold").grid(row=0, column=0, sticky='w')
        Label(self, text="Q.2) What is the value of pi ?",font="bold").grid(row=6, column=0, sticky='w')

    def radio_button(self):
        self.var1=IntVar()
        self.var2=IntVar()

        Radiobutton(self,text="Salman khan",variable=self.var1,value=1).grid(row=1, column=0,sticky='w')
        Radiobutton(self,text="Shahrukh khan",variable=self.var1,value=2).grid(row=2, column=0,sticky='w')
        Radiobutton(self,text="Amari khan",variable=self.var1,value=3).grid(row=3, column=0,sticky='w')
        Radiobutton(self,text="Amitabh Bachhan",variable=self.var1,value=4).grid(row=4, column=0,sticky='w')

        Radiobutton(self,text="3",variable=self.var2,value=1).grid(row=7, column=0,sticky='w')
        Radiobutton(self,text="3.142",variable=self.var2,value=2).grid(row=8, column=0,sticky='w')
        Radiobutton(self,text="2.142",variable=self.var2,value=3).grid(row=9, column=0,sticky='w')
        Radiobutton(self,text="5",variable=self.var2,value=4).grid(row=10, column=0,sticky='w')

    def click(self):
        print("Button Clicked!")
        with open("abc.txt","w") as f:
            f.write(f"Selected answer Of User Is :-> Q.1) {self.var1.get()} Q.2) {self.var2.get()}")

    def button(self):
        Button(text="Submit",command=self.click).grid(row=11,column=3)


if __name__ == '__main__':
    window = GUI1()
    window.label()
    window.radio_button()
    window.button()
    window.mainloop()
