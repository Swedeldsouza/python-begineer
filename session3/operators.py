'''
Equals :a==b
Not Equals: a!=b
Less than:a<b
less than equal to:a<=b
Greater than:a>b
Greater than equal to: a>=b
'''

#logical operators
''' and
    or'''

#if elif elif else

'''

x=5
if(x==10):
    print("answer is right ")
else:
    print("ans is wrong ,x value is :",x)


x=11
if (x==5):
    print("x is 5")
elif(x<5):
    print("x is less than 5")
elif(x>5 and x<10):
    print("x is greater than 5")

else:
    print ("x is ",x)
    


a=int(input("enter number :"))    # postive ,negative ,0
if(a>0):
    print("a is positive")
elif(a==0):
    print("a is 0")

else:
    print("x is negative")


a=int(input("Enter a number"))    # even and odd
if(a%2==0):
    print(a,"is even")
else:
    print(a,"is odd")

b=int(input("Enter a number"))    # divisble by 3 and 7
if(b%3==0 and b%7==0):
    print(b,"is divisible by both 3 and 7 ")
elif(b%3==0):
    print(b,"is divisble by 3")
elif(b%7==0):
    print(b,"is divisble by 7")
else:
    print(b,"not divisible by both 3 and 7")


# 3 numbers
u=int(input("Enter a number"))
v=int(input("Enter a number"))
w=int(input("Enter a number"))
if(u>v and u>w):
    print(u,"is greater than v and w")
elif(v>u and v>w):
    print(v,"is greater than u and w")
else:
    print(w,"is greater ")





#condition "while loop"
i=1
while(i<=5):
  print("Swedel",i)
  i=i+1
  
i=5
while(i>=1):
  print("Swedel",i)
  i=i-1

 
i=4
while(i>=1):
    print("*"*i)
    i=i-1
i=1
while(i<=4):
    print("*"*i)
    i=i+1

i=1
while(i<=10):
     print(10*i)
     i=i+1



li=[1,2,3,4,5]
for i in li:
   print(i)

li=[1,2,3,4,5]
print(li)

string=["korea","japan","australia","india","china"]
for i in string:
     if(i=="japan"):
       print(i)

li=range(1,21)
for i in li:
   
   if(i%2==0):
    print(i ,"is even")
'''
zi=range(1,31)
for i in zi:
    if(i%3==0):
      print(i,"divisible by 3")  
