#if-else statement
pin=int(input("enter your 4-digit ATM pin"))

if pin==1234:
    print("Correct Pin")
else:
    print("Incorrect Pin")
    
#Even or odd 
num=int(input("Enter a number: "))

if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
    
#Find the large number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("The larger number is:", a)
elif b > a:
    print("The larger number is:", b)
else:
    print("Both numbers are equal.") 
    
#Leap year
year=int(input("Enter a year: "))
if year%4 == 0:
    print("Year is a leap year")
else:
    print("Year is not leap year")
    
#positive or negative no.
n=float(input("Enter a number: "))
if n>0:
    print("The number is positive.")
elif n<0:
    print("The number is negative.")
else:
    print("The number is zero.")
