#Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == '+':
    print("Sum is :", num1 + num2)

elif operator == '-':
    print("Difference is :", num1 - num2)

elif operator == '*':
    print("Product is :", num1 * num2)

elif operator == '%':
    print("Modulo is :", num1 % num2)

elif operator == '/' and num2 != 0:
    print("Division:", num1 / num2)
    
else:
    print("Invalid operator.")
    
#Input two number and find the greater number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number is:", a)
elif b > a:
    print("Greater number is:", b)
else:
    print("Both numbers are equal.")
    
#Input three number and find the largest
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)

elif b >= a and b >= c:
    print("Largest number is:", b)

else:
    print("Largest number is:", c)
    
#Finfthe smallest number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a <= b and a <= c:
 print("Smallest number is:", a)

elif b <= a and b <= c:
     print("Smallest number is:", b)
     
else:
     print("Smallest number is:", c)
     
#User name password checker
username = input("Enter username: ")
password = input("Enter password: ")

if (username == "Yashika" and password =="4567"):
    print("Login successful!!")
else:
    print("Incorrect username or password.")

