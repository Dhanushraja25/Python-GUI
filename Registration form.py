from tkinter import *
from turtle import color
root = Tk()
root.geometry("500x250")
root.config(bg="light green")
root.title("registration form")
head=Label(root,text="Form",bg="lightgreen",fg="black").pack(anchor=CENTER)

Label(root,text="Name",bg="light green",fg="red").place(x=20,y=40)
Label(root,text="Course",bg="light green",fg="red").place(x=20,y=60)
Label(root,text="Semester",bg="light green",fg="red").place(x=20,y=80)
Label(root,text="Form No.",bg="light green",fg="red").place(x=20,y=100)
Label(root,text="Contact No.",bg="light green",fg="red").place(x=20,y=120)
Label(root,text="Email id",bg="light green",fg="red").place(x=20,y=140)
Label(root,text="Address",bg="light green",fg="red").place(x=20,y=160)

namevalue=StringVar()
coursevalue=StringVar()
semestervalue=StringVar()
formnovalue=StringVar()
contactnovalue=StringVar()
emailidvalue=StringVar()
addressvalue=StringVar()

nameentry=Entry(root,textvariable=namevalue)
courseentry=Entry(root,textvariable=coursevalue)
semesterentry=Entry(root,textvariable=semestervalue)
formentry=Entry(root,textvariable=formnovalue)
contactentry=Entry(root,textvariable=contactnovalue)
emailentry=Entry(root,textvariable=emailidvalue)
addressentry=Entry(root,textvariable=addressvalue)

nameentry.place(x=92,y=40)
courseentry.place(x=92,y=60)
semesterentry.place(x=92,y=80)
formentry.place(x=92,y=100)
contactentry.place(x=92,y=120)
emailentry.place(x=92,y=140)
addressentry.place(x=92,y=160)

Button(root,text="Submit",bg="red",fg="black").place(x=150,y=180)

root.mainloop()