import random
from random import sample

letters=['a','b','c','d','e','f','g','h','i','j','k',
         'A','B','C','D','E','F','G','H','I','J','K']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['@','_','+','%','!']
print("welcom to password suggestion")
nl=int(input("enter how many latters you want"))
nn=int(input("how many numbers u want "))
ns=int(input("who many symbols 1-5"))
password=""
for i in range(1,nl+1):
    char=random.choice(letters)
    password+=char
for i in range (1,nn+1):
    num=random.choice(numbers)
    password+=num
for i in range(1,ns+1):
    num1=random.choice(symbols)
    password+=num1
print(password)
#mix=' 'join random.sample(password,len(sample))
#print(mix)


