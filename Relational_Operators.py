'''write a python program to calculate a discount for a customer based on purchase amount using tkinter
purchase>=$500: 20% discount
purchase>=$200 and purchase<$200: 10% discount
purchase<$200: NO DISCOUNT'''
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Discount Calculator")
window.geometry("200x250")
def discount():
    purchase_amount=int(e1.get())
    if(purchase_amount>=500):
        discount=20/100
        messagebox.showinfo("discount","20%")
    elif(purchase_amount>=200 and purchase_amount<500):
        discount=20/100
        messagebox.showinfo("discount","10%")
    else:
        discount=0
        messagebox.showinfo("Discount","Sorry, No Discount")
    total_amount=purchase_amount-(purchase_amount*discount)
    print("Total amount to be paid: $",total_amount)


l1=Label(window,text="ENTER THE AMOUNT:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Calculate",command=discount)
b1.grid(row=2,column=0)

window.mainloop()


'''Python code for determining grade of the student
score>=90:A grade
B:score>=80 and score<90
c:score>70 and score<80
D:score>=60 and score<70
E:score<60'''

from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Grade Calculator")
window.geometry("200x250")
def grading_system():
    marks=int(e1.get())
    if(marks>=90):
        messagebox.showinfo("Grade","A")
    elif(marks>=80 and marks<90):
        messagebox.showinfo("Grade","B")
    elif(marks>=70 and marks<80):
        messagebox.showinfo("Grade","C")
    elif(marks>=60 and marks<70):
        messagebox.showinfo("Grade","D")
    else:
        messagebox.showinfo("Grade","E")

l1=Label(window,text="Enter the marks:",)
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Calculate",command=grading_system)
b1.grid(row=1,column=0)


window.mainloop()




