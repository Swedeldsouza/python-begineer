'''
def square(a):
    c=(a**2)
    print(c)
square(5)


#notes

f=lambda a:a*a
r1=f(5)
print(r1)

def even(num):
    
    for i in num:
        if(i%2==0):
            print(i)

even([1,2,3,4,5])

def even(n):
    return n%2==0
num=[1,2,3,4,5]
even_num=list(filter(even,num))
print(even_num)

    
f=lambda a,b:a+b
r1=f(5,1)
print(r1)



num=[1,2,3,4,5]

even_num=list(filter(lambda i:i%2==0,num))
print(even_num)



import datetime
x=datetime.datetime.now()
print(x)


import mymodule
mymodule.greeting("Swedel")
a=mymodule.person1["name" ]
b=mymodule.person1["city"]
c=mymodule.person1["subject"]
print( a+" "+ b+ " "+c)
d=mymodule.person1
print(d)



import re
p=input("enter your password")
x=True
while x:
    if(len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    else:
         print("Valid password")
         x=False
         break
if x:
    print("Invalid")
                       
  
   
i=1
while(i<=5):
    print("1"*1)
    
    i=i+1
    

'''      
      
num = 1
n=5
for i in range(0, n):
    
    for j in range(0, i+1):
        print(num, end=" ")
        num = num + 1
        print("\r") 
  
 
                          






