#1 wap to check a no or string is palindrome or not
a='repaper'
print(a)
print(a[::-1])
if(a==a[::-1]):
  print('it ia a pallindrome')
else:
 print('not a pallindrome')

#  2factorial program
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
