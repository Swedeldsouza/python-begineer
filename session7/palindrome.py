'''
a="deleveled"
i=0
j=-1
for i in a:
    for j in a:
        if (a[i]==a[j]):
            print("match")
            break
        else:
            print("Not match")
    j=j-1
i=i+1
 '''

a="deleveled"


    
'''
def odd():
    n=int(input("enter input"))
    l=range(0,n+1)
    for x in l:
          if(x%2!=0):
              print(x,"odd")
odd()
          
         
          

      
try:
    print(x)
except:
        print("Hey")
else:
    print("Neee")


ui=input("Enter age") 
try:
    val=int(ui)
    print(" user input is int")

except Exception as e:
    print(e)
    

def divide(x,y):
    try:
        r= x//y
        print(r)
        
    except:
        print("error")
    

divide(2,0)


#list comprehension
li=[]

for i in range(1,101):
    li.append(i**2)
print(li)

squares=[i**2 for i in range(1,101)]
print(squares)

li=[]
for i in range(1,21):
    if(i%2==0):
        li.append(i)
print(li)

li= [  i for i in range(1,21) if i%2==0]
print(li)

'''
        
