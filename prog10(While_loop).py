#1.print numbers from 1 to 10 using a while loop
num=1
while(num<=10):
    print(num)
    num+=1
#2.sum of first n natural number using while loop
n=int(input("Enter a number: "))
sum=0
i=1
while i <= n:
    sum += i
    i += 1
print(f"The sum of the first {n} natural numbers is: {sum}")

# 3 print the multiplication table of a number(eg.15)
j=1
while j<=10:
    print(n," * ",j," = ",n*j)
    j+=1
# print the factorial number using while loop
value = int(input("Enter a number: "))
fact = 1
i = 1
while i <= value:
    fact *= i
    i += 1
print(f"The factorial of {n} is: {fact}")

# print the pattern using loop 
# *
# **
# ***
# ****
# *****
a=1
while a<=5:
    print("*"*a)
    a+=1
