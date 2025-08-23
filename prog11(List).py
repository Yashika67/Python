#.add an element to the end of a list using appned method
li=[1,2,4,7,9,9,9]
print(li)
li.append(5)
print(li)

#.find  the length of list using (len).
print(len(li))

#.check if an element exists in a list or not
num=int(input("Enter a number to check in a list or not : "))
if (num in li):
    print("The number ",num," is in the list")
else:
    print("The number ",num," is in the list")

#find the sum of all element in a list
sum=0
for i in li:
    sum+=i
print(sum)

#print the square of each element in  list
print("Square of each element")
for j in li:
    print(j*j)
    
#sort a list in ascending and decending order
li.sort()
print("Ascending Order:", li)
li.sort(reverse=True)
print("Descending Order:", li)

#merge two list into one
li2=[10,20,30]
lis=li+li2
print(lis)

#remove duplicates from a list
unique=list(set(lis))
print(unique)

#find the second largest no. in a list
unique.sort(reverse=True)

if len(unique) >= 2:
    print("Second largest number is:", unique[1])
else:
    print("Not enough unique numbers.")
