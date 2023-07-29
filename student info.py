from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("455x233")

Label(root,text="Regno").grid(row=1)
Label(root,text="Name:").grid(row=2)
Label(root,text="Dept").grid(row=3)
Label(root,text="Gender").grid(row=4)
Label(root,text="Age").grid(row=5)

regnovalue=StringVar()
namevalue=StringVar()
deptvalue=StringVar()
gendervar=IntVar()


regnoentry=Entry(root,textvariable=regnovalue)
nameentry=Entry(root,textvariable=namevalue)
deptentry=Entry(root,textvariable=deptvalue)
genderentry=Radiobutton(root,text="Male",variable=gendervar,value=1)
genderentry1=Radiobutton(root,text="Female",variable=gendervar,value=2)
spinentry=Spinbox(root,from_=19,to = 25)

regnoentry.grid(row=1,column=3)
nameentry.grid(row=2,column=3)
deptentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
genderentry1.grid(row=4,column=4)
spinentry.grid(row=5,column=3)

Button(text="Insert").grid(row=6)
Button(text="Update").grid(row=6,column=3)
Button(text="Delete").grid(row=7)
Button(text="Select").grid(row=7,column=3)

root.mainloop()