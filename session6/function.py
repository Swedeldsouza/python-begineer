li=[]
def func():
    
    id_num=55
    id_check=int(input("Enter ID:"))
    if id_check==id_num:
        print("Correct")
    elif(id_check<id_num):
        print("Smaller")
        li.append(id_check)
        print(li)
    elif(id_check>id_num):
        li.append(id_check)
        print("Greater")
        print(li)
                
func()


'''
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def div(x,y):
    return x/y

print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
choice=(input("Enter your choice"))   #enter choice

num1=int(input("enter user input x:")) #x variable
num2=int(input("enter user input y:")) #y  variable

if choice=="1":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="2":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=="3":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="4":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid choice")

'''
      
    
