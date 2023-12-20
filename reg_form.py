from tkinter import *
root = Tk()
root.geometry("500x300")  #for frame

def getvals():
    print("Accepted")


#heading
Label(root, text="Registration form", font="arial 15 bold").grid(row=0, column=3)


#field name
name= Label(root, text="name")
phone= Label(root, text="phone")
gender= Label(root, text="gender (M/F)")
age= Label(root, text="age")
course= Label(root, text="course")

#packing our fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
age.grid(row=4,column=2)
course.grid(row=5,column=2)

#creating variable where values can be stored
namevalue= StringVar
phonevalue= StringVar
gendervalue= StringVar
agevalue= StringVar
coursevalue= StringVar

checkvalue= IntVar


#creating entry field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
ageentry = Entry(root, textvariable =agevalue)
courseentry = Entry(root, textvariable =coursevalue)

#packing entry fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
ageentry.grid(row=4,column=3)
courseentry.grid(row=5,column=3)

#creating checkbox
checkbtn = Checkbutton(text="all good? check once again..", variable = checkvalue)
checkbtn.grid(row=6, column=3)

#submit button
Button(text = "Submit", command = getvals).grid(row=7, column=3)

root.mainloop()
