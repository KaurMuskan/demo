# ....................day 1..........................
# string programs
print('hello')
a='muskan deep kaur'
print(a)
print(a[0:])
print(a[1:])
print(a[2:4])
print(a[::-1])
print(a[:-1])
print(a[:-2])
print(a[-1:])
print(a[-3:])
print(a.isupper())
print(a.islower())
print(a.upper())
print(a.capitalize())
print(a.casefold())
print(a.center(15,'*'))
print(a.encode())
print(a.endswith('n'))
print(a.expandtabs())
print(a.find('k'))
print(a.index('h'))
print(a.isalnum())
print(a.isalpha())
print(a.isdecimal())
print(a.isdigit())
print(a.partition('th'))

# conversions of data types 
# integer operations
a=10
print(a)
print(type(a))#print data type
print(id(a))
print(float(a))#convert to float
print(bool(a))#return bool value
print(complex(a))#conert to complex
print(str(a))#convert to string

# float value
a=23.56
print(a)
print(type(a))#print data type
print(id(a))
print(int(a))#convert to int
print(bool(a))#return bool value
print(complex(a))#conert to complex
print(str(a))#convert to string

# string
a='hello'
print(a)
print(type(a))#print data type
print(id(a))
#print(int(a))#convert to int(error if it is not a number)
print(bool(a))#return bool value
# print(complex(a))#conert to complex(error)
# print(float(a))#convert to float(error)

# complex number
a=23.56+0j
print(a)
print(type(a))#print data type
print(id(a))
# print(int(a))#convert to int
print(bool(a))#return bool value
# print(float(a))#conert to float
print(str(a))#convert to string

# bool 
a=True
print(a)
print(type(a))#print data type
print(id(a))
print(int(a))#convert to int
print(float(a))#convert to float
print(complex(a))#conert to complex
print(str(a))#convert to string
 
#  ......................DAY 2............................
# Operators
# ARITHMETIC OPERATORS
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**2)
print(a%b)

# RELATIONAL OPERATORS
a=10
b=20
print(a>b)
print(a<b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
print(20>15>4<22)

# LOGICAL OPERATORS
a=10
b=20
c=15
print(b>a and b>c)
print(a>b and b>c)
print(b>a or b>c)
print(a>b or b>c)
print(not(b>a and b>c))
print(not(a>b and b>c))
print(not(15>2))

# Bitwise operators
a=4
b=5
print(a&b)
print(a|b)
print(a^b)
print(a>>1)
print(b>>1)
print(a<<1)
print(b<<1)
print(~a)
print(~b)

# Identity operator
a=10
b=10
c=30
print(a is b)
print (a is c)
print(b is not c)

# MEMBERSHIP OPERATOR
a='python'
print('h' in a)
print('k' in a)

# CONTROL FLOW STATEMENTS
# conditional statements
# if statement
x=int(input('enter the number'))
if(x>0):
    print(x,'is positive')

# if-else statement
x=int(input('enter the number'))
if(x%2==0):
    print(x,'is even number')
else:
    print(x,'is odd number')

# nested if else
x=int(input('enter first number'))
y=int(input('enter second number'))
if(x!=y):
    if(x>y):
        print('first number(',x,')is greater than second number(',y,')')
    else:
        print('second number(',y,')is greater than first number(',x,')')
else:
    print('first number(',x,')is equal to second number(',y,')')

# looping statements
# for loop
for x in range(5):
    print(x)

for x in range(5):
    for y in range(5):
        print(x,y)
    print(' ')

for x in range(5):
    for y in range(x+1):
        print('*',end=' ')
    print(' ')

for x in range(5,0,-1):
    for y in range(1,x+1):
        print('*',end=' ')
    print(' ')
    
for x in range(5):
    for y in range(x+1):
        print('*',end=' ')
    print(' ')
for x in range(5,0,-1):
    for y in range(1,x+1):
        print('*',end=' ')
    print(' ')

sum=0
for x in range(1,6):
    sum+=x
print('sum of first 5 natural numbers:',sum)

num='2684'
for i in num:
    print(i,end=" ")

# while loop
num=0
while (num<=10):
    print(num)
    num+=1

num='2473'
sum=0
temp=int(num) 
print('num:',num)
print('digits:')
for i in num:
    print(i)
while temp>0:
    digit=temp % 10
    sum+=digit
    temp//=10
print('sum of digits of num:',sum)

# JUMPING STATEMENTS
# BREAK
for x in range(10):
    print(x)
    if x==5:
        break

for x in range(10):
    if x==5:
        break
    print(x)

for x in range(10):
    if x==5:
        continue
    print(x)

    # ................................DAY 3..................................
    #LISTS
l=[2,5,8,4,6,2.4,'hello']
print(l)
print(type(l))
print('elements of list:')
for x in l:
    print(x)
#ADD ELEMENT
a=(input('enter element to be added'))
l.append(a)
print(l)
print('after inserting at 3rd index:')
l.insert(3,7)
print(l)
print('after deleting element from 5th index')
l.pop(5)
print(l)
print('after deleting 5 from list:')
l.remove(5)
print(l)
l1=[1,5,8.3,4,2]
print('after extending list by adding other list')
l.extend(l1)
print(l)
print(l+l1)#other way
print('index of "4"in list')
print(l.index(4))
print('no. of times 4 in list:')
print(l.count(4))
l2=['hello','deep','amaze','full']
print('list:',l2)
print('sorted list:')
l2.sort()
print(l2)
print('list:',l1)
print('sorted list:')
l1.sort()
print(l1)
print('reversed list:')
l1.reverse()
print(l1)

# TUPLE
t=(2,5,3,'hey')
print(t)
print(type(t))
print('elements in tuple:')
for x in t:
    print(x)
print('length of tuple:',len(t))
l=list(t)
print('after converting tuple to list')
print(l)
print('after adding element:')
l.append(5)
print(l)
print('again converting from list to tuple:')
print(tuple(l))

#SETS
s={10,30,50,70}
print(s)
print(type(s))
print('after adding 40:')
s.add(40)
print(s)
print('after removing 50:')
s.remove(50)
print(s)
s1={20,40,60,80}
print('Difference (s-s1):')
print(s.difference(s1))
print('Intersection:',s.intersection(s1))
print(s.isdisjoint(s1))
print(s.issubset(s1))
print(s.issuperset(s1))
s2={10,30,}
print(s2.issubset(s))
print('union:',s.union(s1))

#DICTIONARY
dict1={'k':3,'p':4}
print(dict1)
print(type(dict1))
x=('k1','k2','k3')
y=1
dict1=dict.fromkeys(x,y)
print(dict1)

choice={'fruit':'pear','color':'black','flower':'rose'}
print(choice)
print('choice value of color:',choice.get('color'))
print(choice.get('money',1000))
print('dictionary items:',choice.items())
print('dictionary keys:',choice.keys())
print('dictionary values:',choice.values())
print('setdefault value:',choice.setdefault('fruit','mango'))
choice.pop('fruit')
print('after delete item:',choice)

'''while loop'''
i = 1
while i < 6:
  print(i)
  i += 1


''' Break Statement'''
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


''' Continue Statement'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



'''for loop'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

''' Break Statement'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


''' Continue Statement'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
print(x)


'''else'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")



'''Nested loop'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


'''if elif statements'''

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

    # dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# data type
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# functions of dictionary
# Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964'}
  
thisdict["color"] = "red"
print(thisdict)

# Removing Items
# pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# del()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)