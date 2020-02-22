
'''
ID='swed77'

i=1
while True:
    UI=input("Enter ID")
    if (ID==UI):
       print("Welcome")
    elif(ID!=UI):
      print("Try again")
 '''      
'''
#all function together called modules .these modules are called packages
module
time-sleep fucntion
pygame
'''
import time
id_num="1234"
id_tries=1
while True:
    id_check=input("Enter ID")
    if id_check==id_num:
       print("Welcome")
       break
    elif(id_tries==3):
      print("you have failed 3 times")
      print("System is freezing")
      time.sleep(10)
      id_tries=1

    elif(id_check!=id_num):
         print("incorrect id try again:")
         id_tries=id_tries+1
         
print("How may i help you?")
'''
pre-defined
built -in: function buit into python
user-defined-functions defined by users themselves
def function and call function
what is function??
-Group of related statements that erform a specific task
function make it more organized and manageable
they have multile statements
#return your function can return a value,store in a variable 
def is a keyword

'''
def func():
    print('Swede')

func()

'''
'''
def add(x,y):
    c=x+y
    return c
add(3,4)


def larger(x,y,z):
    if(x>=y and x>=z):
        print(x,"X is larger")
    elif (y>=x and y>=z):
        print(y,"y is larger")
    else:
        print(z,"z is larger")
        return x,y,z

larger(3,4,6)

def functions(x):
    return 5*x

print(functions("*"))

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
 

dict={"1":"1","2":"4","3":"9","4":"16"}
del dict["1"]
dict["7"]="3"
print(dict)


list=[1,2,3,4]
list.insert(2,3)
print(list)


         
      
   
  
