import math

#Take Square Root
a=int(input("Enter a Number : "))
print("Square Root of ",a," is ",math.sqrt(a))

#Take Log
a=int(input("Enter value of x : "))
b=int(input("Enter value of base : "))
print("Log of x=",a ,"and base=",b," is : ",math.log(a,b))

#Take Cos
a=float(input("Enter a number : "))
print("Cos of ",a," is : ",math.cos(a))

#Take Sin
b=float(input("Enter a number : "))
print("Sin of ",b," is : ",math.sin(b))

#Take Tan
c=float(input("Enter a number : "))
print("tan of ",c," is : ",math.tan(c))

#Calculate Degree
a=float(input("Enter a Number : "))
print("Degree of ",a," is : ",math.degrees(a))

#Find factorial
x=int(input("Enter a Number : "))
print("Factorial of ",x," is : ",math.factorial(x))

#Take Exponent
y=int(input("Enter a Number : "))
print("Exponent of ",y," is : ",math.exp(y))

#Take power
a=int(input("Enter base : "))
b=int(input("Enter power : "))
print("Power of ",a," is : ",math.pow(a,b))

#Take Base 10 log
a=int(input("Enter a number : "))
print("Base 10 log of ",a," is : ",math.log10(a))

#Take Base 2 log
b=int(input("Enter a number : "))
print("Base 2 log of ",b," is : ",math.log2(b))

#use fabs() absolute value means float
a=int(input("Enter a number : "))
print(math.fabs(a))

#use of floor()
x=float(input("Enter a float number : "))
print("Round down to nearest integer : ",math.floor(x))

#use of ceil()
y=float(input("Enter a float number : "))
print("Round up to nearest integer : ",math.ceil(y))

#Check number is finite or not
x=int(input("Enter a number : "))
print("Number is finite : ",math.isfinite(x))
