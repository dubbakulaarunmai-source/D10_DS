#x=12
#print(type(x))

#y=12.5
#print(type(y))

# z=3+6j
# print(type(z))

#Str1="data  science"
# print(Str1)
# print(type(Str1))

# op=len(Str1)
# print(op)
# print(Str1[6])

 #sequence type
 #list
#print(Str1[-3])

# List1=[1,2,'hi','hello',3.4]
# print(List1)
# print(len(List1))
# print(List1[3])
# print(List1[-3])
# print(List1[3][1])

# #nested list
# List1=[1,2,'hi','hello',3.4,[12,23,34]]
# print(List1[5][1])
# print(List1[-1][-2])

#update list
# List1[3]="welcome"#updating
# print(List1)
#deleting
# del List1[2] #deleting valuw from the list
# print(List1)

# List1=[1,2,'hi','hello',3.4,[12,23,34]]
# del List1
# print(List1)

#tuple

# tupl1=(1,2,3.4,'hello')
# print(tupl1)
# print(type(tupl1))
# print(tupl1[2])
# print(tupl1[-2])
# tupl1[3]='welcome'

#set
# set1={3,4,'hi','hello',5.6,4,'hi'}
# print(set1)
# set2={1,2,3,4,5,8,9,10,2,3}
# print(set2)
# print(hash(101))
# print(hash('hello'))

#dictionaries

# apple_info={"color":   "red",
#             "price":    75,
#             "validity":"one week",
#              "price":   90
#             }
# print(apple_info) 
# apple_info["origin"]="shimla"
# print(apple_info)

#bool

# is_pursuing_btech=True
# print(is_pursuing_btech)

#primitive data types
#immutable at same place
#int,float,complex,string,bool,none
# # x=125
# print(x)
# print(id(x))
# x=256
# print(x)
# print(id(x))

#non primitive data types
#mutable at the same place
#list,tuple,set,dict

# x=[1,2,3]
# print(id(x))
# x[1]='hello'
# print(id(x))
# x='hello'
# x[1]='a'
# print(x)

y=[1,2,3]
y[1]='hello'
print(y)



