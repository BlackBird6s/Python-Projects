                                 # Bill Management System

from tkinter import *
root=Tk()
root.geometry("1000x500")
root.title("Bill Management System")
root.resizable(False,False)

def Reset():
    entry_Dosa.delete(0,END)
    entry_Masala_Dosa.delete(0,END)
    entry_Shahi_Paneer.delete(0,END)
    entry_Dal_Makhani.delete(0,END)
    entry_Masala_Chaap.delete(0,END)
    entry_Choly_Kulcha.delete(0,END)
    entry_Khadhi_paneer.delete(0,END)

def Total():
    try:a1=int(Dosa.get())
    except: a1=0

    try:a2=int(Masala_Dosa.get())
    except: a2=0

    try:a3=int(Shahi_Paneer.get())
    except: a3=0

    try:a4=int(Dal_Makhani.get())
    except: a4=0

    try:a5=int(Masala_Chaap.get())
    except: a5=0

    try:a6=int(Choly_Kulcha.get())
    except: a6=0

    try:a7=int(Kadhai_Paneer.get())
    except: a7=0

# define cost of each item per quantity

    c1=95*a1
    c2=105*a2
    c3=188*a3
    c4=145*a4
    c5=157*a5
    c6=75*a6
    c7=198*a7

    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="yellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_Bill,bd=6,width=15,bg="green")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    String_bill="Rs.",str('%.2f' %totalcost)
    Total_Bill.set(String_bill)

Label(text="Bill Management Syetem",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

# MENU CARD

f=Frame(root,bg="green",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="green").place(x=80,y=0)

Label(f,font=("Lucida calligrapy",15,'bold'),text="Dosa.......Rs.95/plate",fg="black",bg="green").place(x=10,y=80)
Label(f,font=("Lucida calligrapy",15,'bold'),text="Masala Dosa.......Rs.105/plate",fg="black",bg="green").place(x=10,y=110)
Label(f,font=("Lucida calligrapy",15,'bold'),text="Shahi Paneer.......Rs.188/plate",fg="black",bg="green").place(x=10,y=140)
Label(f,font=("Lucida calligrapy",15,'bold'),text="Dal Makhani.......Rs.145/plate",fg="black",bg="green").place(x=10,y=170)
Label(f,font=("Lucida calligrapy",15,'bold'),text="Masala Chaap.......Rs.157/plate",fg="black",bg="green").place(x=10,y=200)
Label(f,font=("Lucida calligrapy",15,'bold'),text="Choly Kulcha.......Rs.75/plate",fg="black",bg="green").place(x=10,y=230)
Label(f,font=("Lucida calligrapy",15,'bold'),text="Kadhai Paneer.......Rs.198/plate",fg="black",bg="green").place(x=10,y=260)

#BILL

f2=Frame(root,bg="yellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri",20),bg="yellow")
Bill.place(x=120,y=10)

#Entery work

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Dosa=StringVar()
Masala_Dosa=StringVar()
Shahi_Paneer=StringVar()
Dal_Makhani=StringVar()
Masala_Chaap=StringVar()
Choly_Kulcha=StringVar()
Kadhai_Paneer=StringVar()
Total_Bill=StringVar()

# Label

ibl_Dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
ibl_Masala_Dosa=Label(f1,font=("aria",20,'bold'),text="Masala Dosa",width=12,fg="blue4")
ibl_Shahi_Paneer=Label(f1,font=("aria",20,'bold'),text="Shahi Paneer",width=12,fg="blue4")
ibl_Dal_Makhani=Label(f1,font=("aria",20,'bold'),text="Dal Makhani",width=12,fg="blue4")
ibl_Masala_chaap=Label(f1,font=("aria",20,'bold'),text="Masala Chaap",width=12,fg="blue4")
ibl_Choly_Kulcha=Label(f1,font=("aria",20,'bold'),text="Choly Kulcha",width=12,fg="blue4")
ibl_Khadhi_Paneer=Label(f1,font=("aria",20,'bold'),text="Khadhi Paneer",width=12,fg="blue4")
ibl_Dosa.grid(row=1,column=0)
ibl_Masala_Dosa.grid(row=2,column=0)
ibl_Shahi_Paneer.grid(row=3,column=0)
ibl_Dal_Makhani.grid(row=4,column=0)
ibl_Masala_chaap.grid(row=5,column=0)
ibl_Choly_Kulcha.grid(row=6,column=0)
ibl_Khadhi_Paneer.grid(row=7,column=0)

# Entry

entry_Dosa=Entry(f1,font=("aria",20,'bold'),textvariable=Dosa,bd=6,width=8,bg="pink")
entry_Masala_Dosa=Entry(f1,font=("aria",20,'bold'),textvariable=Masala_Dosa,bd=6,width=8,bg="pink")
entry_Shahi_Paneer=Entry(f1,font=("aria",20,'bold'),textvariable=Shahi_Paneer,bd=6,width=8,bg="pink")
entry_Dal_Makhani=Entry(f1,font=("aria",20,'bold'),textvariable=Dal_Makhani,bd=6,width=8,bg="pink")
entry_Masala_Chaap=Entry(f1,font=("aria",20,'bold'),textvariable=Masala_Chaap,bd=6,width=8,bg="pink")
entry_Choly_Kulcha=Entry(f1,font=("aria",20,'bold'),textvariable=Choly_Kulcha,bd=6,width=8,bg="pink")
entry_Khadhi_paneer=Entry(f1,font=("aria",20,'bold'),textvariable=Kadhai_Paneer,bd=6,width=8,bg="pink")
entry_Dosa.grid(row=1,column=1)
entry_Masala_Dosa.grid(row=2,column=1)
entry_Shahi_Paneer.grid(row=3,column=1)
entry_Dal_Makhani.grid(row=4,column=1)
entry_Masala_Chaap.grid(row=5,column=1)
entry_Choly_Kulcha.grid(row=6,column=1)
entry_Khadhi_paneer.grid(row=7,column=1)

# Button

btn_reset=Button(f1,bd=5,fg="black",bg="Lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="Lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()