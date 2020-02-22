'''
#practice
#On data structures
#list/  Tuple/set/Dictionaries

#all are collection
#list (ordered and changeable)/and written in square brackets
mylist=["apple","banana","cherry"]
print(mylist[1])
print(mylist)
mylist.append("orange")
print(mylist)
del mylist[0]
print(mylist)
5

#Tuple (ordered and unchangeable)//written in rounded brackets
mytuple=("apple","banana","cherry")
print(mytuple[1])

#set (set is in curly brackets } they are unordered and no indexing present here/
#you can loop through set items 
myset={"hello","jello","mello"}
print(myset)



#Dictionaries( curly and square brackets)
#unordered data values
#they hold  key:value pair .no duplicate members


mydictionary ={"name":"swedel","contact":"655949949","age":"88"}

print(mydictionary)
mydictionary["age"]=34
print(mydictionary)


#append and del dictionary
del mydictionary["age"]
print(mydictionary)


mydictionary ["email"]="swedel.dsouza1996@gmail.com"
print(mydictionary)


li=[2,3,4,5,6]
print(len(li))

si=[2,3,4,6]
print(li+si)

print(si*4)


print(li[2:])
print(li[2])
'''
li=(9,6,5,4,7)
hi=(4,6,6,7)
print(li+hi)

del hi[1]
print(hi)
