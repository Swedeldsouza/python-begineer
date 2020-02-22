#4 questions
'''
Take 3 sides of the triangle as input from the user and check
whether that triangle is equilateral, scalene or isosceles(if else)
'''
'''
a=int(input("Enter side1:"))
b=int(input("Enter side2:"))
c=int(input("Enter side3:"))
if(a==b and b==c ):
      print("equilateral triangle")
elif(a==b or b==c or a==c):
      print("isosceles triangle")

else:
      print("Scalene triangle")

'''

#Convert month name to a number of days(if else)
'''
x=["Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
for i in x:
    print(i)
a=str(input("Enter month:"))
if(a=="Jan"or a== "April" or a=="June" or a=="Aug" or a=="Oct" or a== "Dec"):
      print(a,"31 days")      
elif(a=="Feb"):
      print(a,"28 days")
else(a=="March" or a== "May"or a== "July" or a=="Sept" or a=="Nov" ):
      print(a,"30 days")
)
'''
'''
a=str(input("Enter month:"))
b=int(input("Enter year:"))
if(a=="Jan"):
    print(a,"31 days")
elif(a=="feb" and b%4==0):
    print(a,"29 days")
elif(a=="feb" and b%4!=0):
    print(a,"28 days")
elif(a=="March"):
    print(a,"30 days")
elif(a=="April"):
    print(a,"31 days")
elif(a=="May"):
    print(a,"30 days")
elif(a=="June"):
    print(a,"31 days")
elif(a=="July"):
    print(a,"30 days")
elif(a=="Aug"):
    print(a,"31 days")
elif(a=="Sept"):
    print(a,"30 days")
elif(a=="Oct"):
    print(a,"31 days")
elif(a=="Nov"):
    print(a,"30 days")
elif(a=="Dec"):
    print(a,"31 days")
    
'''

#generate dictionary from two list (while loop)

list1=["korea","japan","india","china"]
list2=["swedel","Jennifer","Jenny","Dsouza"]
'''
for key in list1:
      for value in list2:
         print((key)+":"+(value))
         continue        
print(dict (key:value))
'''
'''
#Method 2 zip
dictionary=dict(zip(list1,list2))
print(dictionary)


#Mthod 1 naive mthod
dictionary={}
for key in list1:
   for value in list2:
      dictionary[key]=value
      list2.remove(value)
      break
print(dictionary)
'''

#for loop(factors of number"
'''
u=int(input("Enter number:")
if(u%i==0):
      print(i,"divisible by 3")  
while(i<=10,u%i==0):
      print(i)
      i=i+1
   
'''
''''
u=int(input("enter number"))
zi=range(1,u)
for i in zi:
    if(u%i==0):
      print(i,"factorial of",u)       
    
'''
      
   
   


