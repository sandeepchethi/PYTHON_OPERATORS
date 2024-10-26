'''Python program using tkinter to check speed of the car and give warning and penalty if speed exceeded conditions
--->speed_limit=90 kmph
--->speed<=speed_limit: NO PENALTY
--->speed<=speed_limit+20: WARNING
--->speed>speed_limit+20: PENALTY 2000'''

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("SPEED GUN")
window.geometry("250x300")

def speed_limit():
    speed=float(e1.get())
    if(speed<=90):
        messagebox.showinfo("NO PENALTY","HAVE A SAFE JOURNEY")
    elif(speed>=90 and speed<=129):
        messagebox.showinfo("WARNING!!!","PLEASE DRIVE WITHIN THE LIMIT")
    else:
        messagebox.showinfo("WARNING!!!","PENALTY: $2000, FOR EXCEEDING THE SPEED LIMIT")


l1=Label(window,text="Enter the speed")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Analyse",command=speed_limit)
b1.grid(row=1,column=0)
window.mainloop()


'''2. python program to withdraw money from ATM using tkinter
--balance=10000
--daily limit=20000
i. withdrawl amount <= balanace
ii. withdrawl notes should be multiples of 100
iii. daily limit should not be exceeded'''

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("ATM")
window.geometry("350x400")


def Atm_operation():
    balance = 10000
    withdrawn_amount = int(e1.get())
    if withdrawn_amount <= balance and withdrawn_amount % 100 == 0:
        messagebox.showinfo("withdrawl", "Please collect your money")
    elif withdrawn_amount % 100 !=0:
        messagebox.showinfo("!!!","withdraw only in hundreds(100)")
    elif withdrawn_amount > balance:
        messagebox.showinfo("daily limit", "You are exceeding the daily limit")
    else:
        messagebox.showinfo("balance", "total balance is")
        total_bal = withdrawn_amount - balance


def check_balance():
    balance = 10000
    withdrawn_amount = int(e1.get())
    if withdrawn_amount<=balance:
        messagebox.showinfo("Balance", balance - withdrawn_amount)
    else:
        messagebox.showinfo("!!!","Enter the amount within in balance limit")


l1 = Label(window, text="Enter the withdrawl amount")
l1.grid(row=0, column=0)
e1 = Entry(window)
e1.grid(row=0, column=1)

b1 = Button(window, text="withdraw", command=Atm_operation)
b1.grid(row=2, column=1)
b2 = Button(window, text="Balance", command=check_balance)
b2.grid(row=3, column=1)

window.mainloop()


'''write a python program using tkinter for checking customer
is eligible for discount or not
business condition:
inputs: purchase_amt
        membership= True or False
purchase_amt>5000 or membership==True: 20% discount avail'''

from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("CUSTOMER DISCOUNT")
window.geometry("350x400")

def discount_eligibility():
    purchase_amount=int(e1.get())
    membership=True
    if purchase_amount>5000 and membership==True:
        messagebox.showinfo("discount details","you will get '20% DISCOUNT'")
    else:
        messagebox.showinfo("Discount details ","SORRY, NO DISCOUNT ON YOUR PURCHASE")

l1=Label(window,text="Total Purchase Amount")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Discount",command=discount_eligibility)
b1.grid(row=2,column=1)

window.mainloop()
