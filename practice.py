import math
total=0
mul=1
count=0
while True:
    number=int(input("Enter a number: "))
    if number==0:
        break
    total+=number
    count+=1
    mul*=number

if count > 0:
    avg=total/count
    print("Average of numbers",avg)
    print("Sum of number",total)
    print("Multiplication of Numbers",mul)
else:
    print("Enter number greater than 0")


 #Main function
print("Exponential of number",math.exp(total))
print("Square of number",math.sqrt(total))