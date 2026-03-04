# #variables
# it is just a name which is given to a memory/storage which stores value/Data

# int()--------convert from string to intger
# float()------convert from string to float
# bool()------convert from string to bool

#DATA TYPES
# primitive data types:int,float,complex,string,bool  
# non primitive data types:list,tuple,dict

# here we can store hetrogeneous Data
# data will stores as per the index by default
# index values always starts from zero
# values inside the list can be considered as elements
# to access those elements using index in two ways---- +ve and -ve

# syntax of list
# listname[index_value]
# +ve starts from 0 to length-1
# -ve starts from -1 to -(length)

#to store contact details of my frnd in a list with dictionaries

# contacts=[{'name':'shiva','number':9912829719},
#           {'name':'kiran','number':7680828719},
#           {'name':'Arun','number':7416828719}
#          ]
# ##Adding new proprty to the kiran dictionary
# contacts[1]['status']='blocked'
# print(contacts)
# contacts[2]['number']=833300134
# print(contacts)


##which one is the greatest number 
# a=52
# b=3
# if a>b:
#     print("a is largest")
# else:
#     print("b is largest")

# a=129
# b=123
# c=431
# if a<b and a>c or a>b and a<c:
#     print("a is second largest")
# elif b<a and b>c or b>a and b<c:
#     print("b is  second largest")
# else:
#     print("c is second largest")

# if a>b and a>c:
#     print("a is largest")
# elif b>a and b>c:
#     print("b is largest")
# else:
#     print("c is largest")

##check whether given number is 2 digit or not

# a=789

# if a>100:
#     print("it is not 2digit number")
# elif a<100:
#     print(" is 2 digit number")
# else:
#     print(" it is invalid")

# b=78
# if b>100:
#     print("it is  not 2 digit number")
# elif b<100:
#     print("it is 2 digit number")
# else:
#     print("invalid number")


# num=int(input("enter a number:"))
# if num<9 and num>0:
#     print("it is single digit number")
# elif num>9 and num<100:
#     print("it is 2 digit number")
# elif num>=100 and num<=999:
#     print("it is 3 digit number")
# else:
#     print("more than 3 digit number")

##leap year or not
# year=int(input("enter a year:"))
# if year%100==0 and year%400!=0:
#     print("it is a leap year")
# elif year%4==0:
#     print("it is a leap year")
# else:
#     print("it is nor a leap year")
##

##nested if

# v1=int(input("enter a value:"))
# v2=int(input("enter a value:"))
# v3=int(input("enter a value:"))
# if v1+v2+v3==180:
#    if v1==v2==v3:
#        print("it is equilateral triangle")
#    elif v1==v2 or v2==v3 or v3==v1:
#        print("it is isoceles triangle")
#    else:
#        print("it is scalene triangle")
# else:
#    print("can not form traingle")

# using nested if
# temp is less than zero------it is frezzing
# temp is greater than zero---
#   temp less than 30----moderate
#   temp greater than 30----it is hot


# temp=int(input("enter temperature:"))
# if temp>=0:
#     if temp<30:
#         print("it is moderate")
#     else:
#         print("it is hot")
# else:
#     print("it is frezzing")  

##if we watch devara1 then only we can watch devara2
# otherwise go and watch devara1

# is_devara1_watched=False
# is_devara2_released=True

# if is_devara1_watched:
#     if is_devara2_released:
#         print("you can watch devara2")
#     else:
#         print("wait unitl devara2 release")
# else:
#     print("go and watch devara1")

##loops concepts

   

