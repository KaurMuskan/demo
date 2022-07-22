#1 wap to check a no or string is palindrome or not
a='repaper'
print(a)
print(a[::-1])
if(a==a[::-1]):
  print('it ia a pallindrome')
else:
 print('not a pallindrome')

# 2factorial program
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)  

# 3 fibonicci series
fibArray=[0,1]
def fibonicci(n):
   if (n<0):
      print("incorrect input")
   elif (n<len(fibArray)):
      return fibArray[n]  
   else:
      fibArray.append(fibonicci(n-1)+fibonicci(n-2))
      return fibArray[n]
print(fibonicci((9)))

# Python program to check if the number is an Armstrong number or not
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# program for calculator 
def calculator():
    operation=input('enter operator')
    num1=int(input('Enter first no.:'))
    num2=int(input('Enter second no.:'))
    if (operation=='+'):
     print(num1+num2)
    elif(operation=='-'): 
     print(num1-num2)
    elif(operation=='*'): 
     print(num1*num2)
    elif(operation=='/'): 
     print(num1/num2)
    else:
        print('invalid input') 
calculator()                

# Pattern programs
row=int(input('enter number of rows:'))
for i in range(row):
    for j in range(i):
        print(i,end=' ')
    print('')     

#  2
row=int(input('enter number of rows:'))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print('') 

# 3
row=int(input('enter number of rows:'))
for i in range(row,0,-1):
    num=i
    for j in range(0,i):
        print(num,end=' ')
    print('') 

# 4
row=int(input('enter number of rows:'))
for i in range(row):
    for j in range(i):
        print(i,end=' ')
    print(" ")  
for i in range(row,0,-1):
    num=i
    for j in range(0,i):
        print(num,end=' ')
    print('')  

# leap year program
year=int(input('enter year:'))
if(year % 400 == 0)and(year % 100 == 0):
    print('it is a leap year')
elif(year % 4 == 0)and(year % 100 != 0):
    print('it is a leap year')
else:
    print('it is not a leap year') 

# program to check prime number
num=int(input('Enterr number:'))
if (num<=1):
    print('it is not prime number')
else:
    for i in range(2,num):
        if (num % i == 0):
          print('it is not prime number') 
          break
    else:
        print('it is a prime number')           

# program to find area
Area of rectangle
l=int(input('Enter length:'))   
b=int(input('Enter breadth:'))
Area=l*b
print('area of rectangle=',Area)

# area of circle
pi=3.14
r=float(input('enter radius:'))
Area=pi*r*r
print('Area of circle= ',Area)

#  area of square
side=int(input('Enter side of square:'))
Area=side*side
print('Area of square = ',Area)

# Program to reverse a list
l=[10,20,30,40]
l.reverse()
print('Reversed list:',l)

# program to find sum of all elements of list
l=[10,20,30,40]
sum=0
for i in range(0,len(l)):
    sum=sum+l[i]
print('sum of list:',sum)

# program to find average, max ,min
l=[10,20,30,40,28,67,8]
avg=sum(l)/len(l)
print('Average of list is:',avg)
print('Largest in list:',max(l))
print('min of list:',min(l))

# 13  grouping dictionary
def grouping_dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))

# 14 nested dictionary
def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
student_id = ["1", "2", "3"] 
student_name = ["khushdeep", "muskandeep ", "prabhdeep"] 
student_grade = [95,96,94]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch='a'
print(nested_dictionary(student_id, student_name, student_grade))


# 15.	Python program to check if a set is a subset of another set.
set1={'apple,mango,orange'}
set2={'mango,orange'}
if(set1<=set2):
    print('is set1 is subset of set2',set1.issubset(set2))
elif(set2<=set1):
    print('is set2 is subset of set1',set2.issubset (set1))  
else:
    print('no set is subset')  
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3}
setC = {1, 2, 3, 6, 7}
print("setA: ", setA)
print("setB: ", setB)
print("setC: ", setC)

print("Is setB a subset of setA?: ", setB.issubset(setA))
print("Is setA a subset of setB?: ", setA.issubset(setB))
print("Is setC a subset of setA?: ", setC.issubset(setA))

# 16.	Write a Python program to create a symmetric difference and set difference
A={'1','2','3','4','5'}
B={'2','4','6','8'}
print(A.symmetric_difference(B))

# 17.	Write a Python program to remove an empty tuple(s) from a list of tuples
tuples=[(10,20,30),(25,36,45),(),(4,6,78),()]
def Remove(tuples):
    tuples=[t for t in tuples if t]
    return tuples
print(Remove(tuples))

# 18.	Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
nums=((24,45,89),(10,45,67),(56,48,32))
def average_tuple(num):
    result=[sum(x)/len(x) for x in zip(*nums)]
    return result
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))

# 19.	Write a Python program to check the validity of a password (input from users).
import re

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password is valid")
            break

validate()
















