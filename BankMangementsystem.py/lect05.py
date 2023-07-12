from tkinter import *

root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("GK GUI")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

# line goes from x1,y1 to x2,y2
can_widget.create_line(0,0,800,400, fill="blue")
can_widget.create_line(0,400,800,0)

# To create rectangle specify parameters in this order -coors of top left and coors of bottom right
can_widget.create_rectangle(3,5,700,300,fill="grey")

can_widget.create_text(200,200,text="Python")

can_widget.create_oval(344,233,244,355)
can_widget.create_arc(10,10,100,100)


root.mainloop()
