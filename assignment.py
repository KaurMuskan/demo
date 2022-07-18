# print("hello")

# 1 program to calculate length of string
# a = 'muskandeep'
# print (len(a))

# 2 program count no of cahracters
# a = 'google.com'
# x=a.count('g',0,9)
# print('g:',x)
# x=a.count('o',0,9)
# print('o=',x)
# x=a.count('l',0,9)
# print('l=',x)
# x=a.count('e',0,9)
# print('e=',x)
# x=a.count('c',0,9)
# print('c=',x)
# x=a.count('m',0,9)
# print('m=',x)
# x=a.count('.',0,9)
# print('.=',x)

# 3 program for last and first 2 charatcer string
# a = 'ambbuu'
# if(len(a)<=2):
#   print('empty string')
# else:
#   print(a[0:2]+a[-2:])  

# 4 program to to get a sting from given string
# a = 'restart'
# x= a[0]
# a=a.replace(x,'#')
# a=x+a[1:]
# print(a)

# 5 program to get a single string from two given strings separated by space and swap the first two characters of each string. 
# x= 'muskan' 
# y= 'muskan'
# a=y[:2]+x[2:]
# b=x[:2]+y[2:]
# print(a+' '+b)

 # 6 Write a Python program to add 'ing' at the end of a given string
# a= 'comunicat'
# length = len(a)
# if length > 2:
#     if a[-3:] == 'ing':
#       a += 'ly'
#     else:
#       a += 'ing'
# print(a)   

# #7program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string
# a='this is not okay not poor'
# snot = a.find('not')
# spoor = a.find('poor')
# print(snot)
# print(spoor)
# if spoor > snot and snot>0 and spoor>0:
#    a = a.replace(a[snot:(spoor+4)], 'good')
#    print(a)
# else:
#    print(a)

#8that takes a list of words and return the longest word and the length of the longest one.
# a=['you','are','beautiful']
# maxx=len(a[0])
# temp=a[0]
# for i in a:
#     if(len(i)>maxx):
#         maxx=len(i)
#         temp=i
# print ('the longest word is',temp)    
# print('length of word is',maxx)    

#9Python program to remove the nth index character from a nonempty string. 
# a='pythonclass'
# n=5
# frst=a[:n]
# scnd=a[n+1:]
# print(frst+scnd)

#10 program to change a given string to a new string where the first and last chars have been exchanged
# a='python'
# print(a[-1:]+a[1:-1]+a[:1])

#11program to remove the characters which have odd index values of a given string. 
# a='pythonclass'
# print(a[::2])
# r=''
# for i in range(len(a)):
#     if i%2==0:
#         r=r+a[i]
# print(r)

#12program to count the occurrences of each word in a given sentence. 
# line='everything will be best if u try ur best'
# word='best'
# a=line.split(' ')
# print(a)
# count=0
# for i in range(0,len(a)):
#     if(word==a[i]):
#         count=count+1
# print('count  of word is',count)

#13Python script that takes input from the user and displays that input back in upper and lower cases
# user_input=input('Hello how r u?')
# print(user_input.upper())
# print(user_input.lower())

#14program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
# sen=input('enter the words:').split(",")
# a=list(set(sen))
# a.sort()
# print(a)

#15Python function to create the HTML string with tags around the word(s). 
# tag='i'
# word='python'
# print("<%s>%s</%s>"%(tag,word,tag)) 

# 23 Write a Python program to check whether a string starts with specified characters. 
# a='i am the worst'
# print(a)
# if(a[0]=='i'):
#     print('it has specified char')
# else:
#     print('not a specified character')

# 21Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 
# a='MUSkan'
# print(a)
# num_upper=0
# for x in a[:4]:
#     if(x.upper()==x):
#        num_upper+=1
# if(num_upper>=2):
#     print(a.upper())

# 20 Write a Python function to reverses a string if it's length is a multiple of 4. 
# a='muskande'
# print(a)
# if(len(a)%4==0):
#     print(a[::-1])
# else:
#     print('a is not multiple of 4')    

#19 Write a Python program to get the last part of a string before a specified character. 
# a= 'i am the worst'
# print(a)
# print(a[1:]+a[0])

#18 Write a Python function to get a string made of its first three characters of a specified string
# a='muskan'
# if(len(a)<3):
#     print(a)
# else:
#     print(a[:3])    

# 22 Write a Python program to remove a newline in Python. 
# a='python class\n'
# print(a)
# print(a.rstrip())

# 17 Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 
# a= 'python'
# print(a[-2:]*4)


# 16 Write a Python function to insert a string in the middle of a string. 
# a='python class'
# b=' first'
# print(a[:6]+b+a[6:])






