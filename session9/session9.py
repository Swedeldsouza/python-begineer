'''
import mymodule1
mymodule1.operation(2,3)
'''
'''
object oriented 
class
objects-methods



class is a keyword

class MyClass:            #class 
    x=5 
p1=MyClass()        # object p1
print(p1.x)

'''
'''
class computer:       #self represents object of that class,
    def config(self):
        print("i5,16gb")
    def config2(self):
        print("i9,32gb")


com1=computer()
com2=computer()

computer.config(com1)
computer.config2(com2)

com1.config()   #alternative method
com2.config2()



class test:
    def __init__(self):  #constructor   
        print('hiral')
t1=test()                #no need to attach method





class Person:
    def __init__(self,name,age):    
        self.abc=name
        self.pqr=age
p1=Person("John",35)
print(p1.abc)
print(p1.pqr)



class college:
    def __init__(self,name,branch):
        self.uvw=names
        self.xyz=branch
        
p2=college("Swedel","Electronics")
p3=college("Jennifer","Computers")
print(p2.uvw)
print(p2.xyz)
print(p3.uvw)
print(p3.xyz)



            

