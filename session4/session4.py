
a=str(input("Enter string"))
v=0
for i in a:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
       v=v+1
print(v)



c= range(1,11)
d=range(1,26)
for i in c:
    for j in d:
       print( str(i)+"*"+str(j)+"="+str(i*j))
    print('-'*50)


av=5
x=int(input("How many candies you want"))
i=1  #i is same as input
while(i<=x):
      print("Candy")
      i=i+1
      if i>av:
          print("Out of stock")
          break
print("bye")


#continue gets back to top of the lopp.And statements below continue are executed          
x=[1,2,3,4]
for i in x:
    if i==2:
        continue
    print(i)
    
e= range(1,101)
for i in e:
    if (i%2==0):
        continue
    print (i)


#string to dictionary

string="jeijjjeee"
string=set(string)
a = 0
  
for i in string: 
    if i == 'e': 
        a = a+ 1
  
 
print (a) 


i=1
for i in string:
    if(i==str):

       i=i+1
print(i)
    
   
  




#[1,2,3,4,5,6] find length without using len function
str = [1,2,3,4,5,6]
a=0
for i in str:
    a =a+1
print (a)



#user se string count number of word and character
a="mango apple "
v=0
for i in a:
    if(a==" "):
           print(len(a))

      

