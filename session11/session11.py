'''
#encapsulation
data is stored in variable ,(information hiding)
'''
class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling price:",(self.__maxprice))
    def setMaxPrice(self,price):           #change variable by third method
        self.__maxprice=price

c=Computer()
c.sell()

#change the price
c._maxprice=1000
c.sell()

#using setter function
c.setMaxPrice(1000)
c.sell()


'''
#api
get  
post using py connect database
json:bunch of data kept.


2modules used
import request
import json
'''

