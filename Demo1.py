from tkinter import *
window = Tk()

window.geometry("500x400+10+10")
window.title("My First GUI")

btn1 = Button(window, text="Click Me!", fg="red", bg="yellow")
btn1.place(x="200", y="80")

txtfld = Entry(window, border=2.50)
txtfld.place(x="170", y="50")

lbl = Label(window, text="My First Demo", font="Times_New_Roman")
lbl.place(x="180", y="20")

window.mainloop()
