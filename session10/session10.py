subclass
inheritance


class bird:
    def __init__(self):
        print('Hugsy is ready')
    def whoisThis(self):
        print('This is Hugsy')
    def swim(self):
        print('Hugsy swims faster')
    def run(self):
        print('Hugsy runs faster')
class Penguin(bird):
    def __init__(self):
        super().__init__()
        print('Penguin is ready')
    def whoisThis(self):
        super().whoisThis()
        print('This is Penguin')
    def swim(self):
        print('Penguin swims faster')
    def run(self):
        print('Penguin runs faster')
        
         
b1=bird()              #object create 
bird.whoisThis(b1)
bird.swim(b1)
bird.run(b1)

p1=Penguin()   
p1.whoisThis()
p1.swim()
p1.run()
        
#super subclass ka main class   (inheritance)it has its own methods
#abstraction-implementation Hiding
#abstraction is an important aspect of object oriented programming.
#In python,we can also perform data hiding by
#adding the double underscore(__) as a prefix to the attribute which
#is to hidden.
#after this ,this attribute will not be visible outside of the class
#through the object.



class Employee:
    __count=0
    def __init__(self):
        Employee.__count=Employee.__count+1
    def display(self):
        print("The number of employe",Employee.__count)
emp=Employee()
emp2=Employee()
try:
    print(emp.__count)
except:
    emp.display()

#implementation ko hide karta hai ,,protecting the method



    #polymorphism
    #overload
class Human:
    def sayHello(self,name=None):
        if name is not None:
            print('Hello'+name)
        else:
            print('Hello')


#create instance
obj=Human()

#Call the method
obj.sayHello()

#Call the method with a parameter
obj.sayHello('Guido')
'''

class Numbers:
    def addition(self,num1=None,num2=None,num3=None):
        if (num1 is not None and num2 is  not None and num3 is not None):
            s=print(num1+num2+num3)
        elif(num1!=None and num2!=None):
            s=print(num1+num2)
        else:
            s=print(num1)
        return s
            
s1=Numbers()
print(s1.addition(8,5,1))

'''
class-animal
def speak
print speaking

subclass-dog
def speak
print barking


make object and call barking
'''

class Animal:
    
    def speaking(self):
        print('speaking')
class dog:
    
    def speaking(self):
        print('barking')
d1= Animal()       
d1.speaking()
a1=dog()
a1.speaking()

