#Computing Problem 2. Construct a GUI and create the Python programs (using Pycharm/ Tkinter module in creating widgets)
# that allow you to type in your Given Name, Middle Name, and Last Name inside the three consecutive Entry widgets and
# display the full name inside the last Entry widget by clicking "Show Full Name" button. (Note: The output window must
# be exactly the same as below image)
from tkinter import *
class Exam2:
    def __init__(self,window):
        self.lblA = Label(window, text="My Full Name")
        self.lblA.place(x="180", y="15")
        self.lblB = Label(window, text="Enter Given Name: ")
        self.lblB.place(x="85", y="40")
        self.txtB = Entry(window, border=2.0)
        self.txtB.place(x="270", y="40")
        self.lblC = Label(window, text="Enter Middle Name: ")
        self.lblC.place(x="85", y="70")
        self.txtC = Entry(window, border=2.0)
        self.txtC.place(x="270", y="70")
        self.lblD = Label(window, text="Enter Last Name: ")
        self.lblD.place(x="85", y="100")
        self.txtD = Entry(window, border=2.0)
        self.txtD.place(x="270", y="100")
        self.lblE = Label(window, text="My Full Name is: ")
        self.lblE.place(x="85", y="130")
        self.txtE = Entry(window, border=2.0)
        self.txtE.place(x="270", y="130")
        self.btn1 = Button(window, text="Show Full Name")
        self.btn1.place(x="180", y="160")
        self.btn1.bind('<Button-1>', self.show)

    def show(self,show):
        self.txtE.delete(0, 'end')
        gname = str(self.txtB.get())
        mname = str(self.txtC.get())
        lname = str(self.txtD.get())
        fname = gname + " " + mname + " " + lname
        self.txtE.insert(END, str(fname))

window = Tk()
wind = Exam2(window)
window.geometry("450x270")
window.title("Midterm Exam Problem 2")

window.mainloop()
