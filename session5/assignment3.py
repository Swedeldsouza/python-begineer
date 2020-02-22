#Write a Python function to sum all the numbers in a list.

def sumlist():
    sum = 0
    i = 0
    list1 = [2,3,4,5,6]
    while(i < len(list1)):
        sum = sum + list1[i] 
        i += 1
      
# printing total value 
        print("Sum of all elements in given list: ", sum)
sumlist()


# Write a Python function to multiply all the numbers in a list.
'''
def multiply(ans):
    list=[11,2,17,18,23]
    ans=1
    for x in list:
        ans=ans*x
        ans=ans+1
        return ans
    print(ans,"multiplicationof all numbers")
multiply(1)
    
   
def multiply(ans,i):
    
    ans = 1
    i=0
    list=[11,2,17,18,23]
    for i in list:
        ans =ans*i
        i=i+1
        
    print(multiply,"ans")
multiply(ans,0)

'''
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply([2,3,4,5,6]))


#define a function to get length without using len function

def length(str):
    a=0
    for i in str:
        a =a+1
        return a
print(length([2,3,4,5,6]))

#Python Program To Check A Number Is Even Or Odd Using Function
num=int(input("Enter a number : "))
def evenodd(num):
        
        if(num%2==0):
            print(num," Is an even")
        else:
            print(num," is an odd")
evenodd(num);
'''
'''
d=dict()
for x in range(1,12):
    d[x]=x**2
print(d)

'''#self exercise
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)
'''

#print length of string without len function

string=input("Enter string:")
countme=0
for i in string:
      countme=countme+1
print("Length of the string is:")
print(countme)
'''
def length(i):
    
    string=input("Enter string:")
    count=0
    for i in string:
      count=count+1
    print("Length of the string is:",count)
      
length(0)


'''

        
 
