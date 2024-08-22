                                    # Registration Form
from tkinter import *
root=Tk()
root.geometry("800x400")

def getvals():
    print("Accepted")

# Heading

Label(root, text="Registration Form",font="ar 15 bold").grid(row=0,column=3)

# Field Name

name = Label(root, text="Name")
mobilenumber = Label(root, text="Mobil Number")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
dateofbirth = Label(root, text="Date of Birth")
addres = Label(root, text="Addres")
email = Label(root, text="Email")
city= Label(root, text="City")
state = Label(root, text="State")
paymentmood = Label(root, text="Paymentmood")


# Packing Fields

name.grid(row=1,column=2)
mobilenumber.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
dateofbirth.grid(row=5,column=2)
addres.grid(row=6,column=2)
email.grid(row=7,column=2)
city.grid(row=8,column=2)
state.grid(row=9,column=2)
paymentmood.grid(row=10,column=2)

# Variable for String Data

namevalue = StringVar
mobilenumbervalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
dateofbirthvalue = StringVar
addresvalue = StringVar
emailvalue = StringVar
statevalue = StringVar
cityvalue = StringVar
paymentmoodvalue = StringVar
checkvalue=IntVar

# Creating Entry Fields

nameentry = Entry(root, textvariable =namevalue)
mobilenumberentry = Entry(root, textvariable =mobilenumbervalue)
genderentry = Entry(root, textvariable =gendervalue)
emergencyentry = Entry(root, textvariable =emergencyvalue)
dateofbirthentry = Entry(root, textvariable =dateofbirthvalue)
addresentry = Entry(root, textvariable =addresvalue)
emailentry = Entry(root, textvariable =emailvalue)
stateentry = Entry(root, textvariable =statevalue)
cityentry = Entry(root, textvariable =cityvalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)

# Packing Entry Fields

nameentry.grid(row=1,column=3)
mobilenumberentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
dateofbirthentry.grid(row=5,column=3)
addresentry.grid(row=6,column=3)
emailentry.grid(row=7,column=3)
stateentry.grid(row=8,column=3)
cityentry.grid(row=9,column=3)
paymentmoodentry.grid(row=10,column=3)


# Creating Checkbox

checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=11,column=3)

# Submit

Button(text="Submit",command=getvals).grid(row=12,column=3)



root.mainloop()