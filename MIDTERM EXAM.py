from tkinter import *

root=Tk()
root.title("Midterms in OOP")
L1=Label( text="Enter your Full Name :", font=40)
L1.grid(row=0, column=0)
L1=Label( text="", font=40)
L1.grid(row=1, column=0)

E1=Entry(root)
E1.grid(row=0, column=1)

def C1():
    E1.insert(0, "")
    L2=Label(LF, text=E1.get())
    L2.pack()


B1=Button(root, text="Click to Display Full Name :", font=40, command=C1)
B1.grid(row=1, column=0)

LF=Label(root)
LF.grid(row=1, column=1)

root.mainloop()