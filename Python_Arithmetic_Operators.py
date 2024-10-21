#21/10/2024
#calcilate simple interest
def simple_interest():
    principal=int(input("enter the principal amount:"))
    time=float(input("enter the time in years"))
    rate=float(input("enter the rate of interest: "))
    simple_interest=principal*time*rate/100
    print("simple interest=",simple_interest)

#compute area and perimeter for rectangular plots
def area_and_perimeter():
    length=float(input("enter the length in feet:"))
    width=float(input("enter the width in feet"))
    area=length*width
    perimeter=2*(length+width)
    print("area of plot:",area)
    print("perimeter of plot:",perimeter)

#convert celsius to fahrenheit
def celsius_to_fahrenheit():
    celsius=float(input("enter the temperature in celsius:"))
    fahrenheit=celsius*(9/5)+32
    print("after conversion of celsius to fahrenheit",fahrenheit)

#compute speed s=ut+1/2at^2
def speed():
    u=float(input("enter the initial velocity:"))
    t=float(input("enter time in seconds:"))
    a=float(input("enter the acceleration:"))
    speed=u*t+(1/2)*a*t**2
    print("speed:",speed)

#calculate Body Mass Index
def BMI():
    weight=float(input("enter the weight in kgs:"))
    height=float(input("enter the height in feet:"))
    BMI=weight/height*2
    print("Body Mass Index is",BMI)