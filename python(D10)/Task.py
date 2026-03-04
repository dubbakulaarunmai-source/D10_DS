# calculates the movie tickets price
# def movie_ticket(price,quantity):
#     total_amount=price*quantity
# if total_amount>2000:
#   return('coke and popcorn')
# elif total_amount>1500:
#   return('coke')
# elif total_amount<1500:
#   return('Thankyou')
# price=int(input("Enter the price:"))
# quantity=int(input("enter no of tickets:"))
# print(show_time(price,quantity))  


# def movie_ticket(price,quantity):
#     total_amount=price*quantity

# if total_amount>2000:
#   return("coke and popcorn")
# elif total_amount>1500:
#   return("coke")
# elif total_amount<1500:
#   return("Thankyou")
# price=int(input("Enter the price:"))
# quantity=int(input("enter no of tickets:"))
# print(show_time(price,quantity))

##leap year or not
# year=int(input("enter a year:"))
# if year%100==0 and year%400!=0:
#     print("leap year")
# elif year%4==0:
#     print("leap year")
# else:
#     print("not a leap year")


##strings
# str1="SOMETHING IS FISHY"
# x=1
# for char in str1:
#     print(char,str1[x])
#     x+=1

# lst iterate-----char=s,x=1-------s o------x=2
# 2nd iteration----char=o,x=2------o m-------x=3

# str1="DATA"

# for char in str1:
#     print(char)

# str1="DATA"

# for char in str1:
#     print(f"{char}-HELLO")

# list1=[4,6,8,2,3,1,8,9]
# for i in list1:
#     print(i)

# list1=[4,6,8,2,3,1,8,9]
# for i in list1:
#     print(f"square of {i} is {i**2}") 

# list1=['shiva','karthik','karun','tejaswini','yamini','deepak','sathwik']
# for i in list1:
#     print(f"{i} length is {len(i)}")

# nums=[3,5,7,8,2,4,6,10]
# # x=0
# # for i in nums:
# #     print(f'{i*x}')
# #     x+=1

# ind=0
# for x in nums:
#     print(f"{x*ind}")
#     ind+=1


# str1="BANANA"
# dict1={}
# for x in str1:
#     if x in dict1:
#         dict1[x]+=1
#     else:
#         dict1[x]=1
# print(dict1)

# str1='hello'
# op=str1.upper()
# print(op)

# str2="ARUNMAI"
# op=str2.lower()
# print(op)

# list1=['apple','banana','SOME','hello','WELCOME','oops']
# for char in list1:
#     if char==char.upper():
#       print(char.lower())
#     else:
#        print(char.upper())

# 'apple'-------apple==APPLE------convert into lower
# 'banana'------banana==BANANA----convert into upper
# 'SOME'-------SOME==SOME------convert into lower


# list1=['apple','banana','SOME','hello','WELCOME','oops']
# op=[]
# for char in list1:
#     if char==char.upper():
#       op+=[char.lower()]

#     else:
#        op+=[char.upper()]
# print(op)

# s1='soMetHINg'
# op=''
# for char in s1:
#     if char==char.upper():
#        op+=char.lower()
#     else:
#        op+=char.upper()
# print(op) 

#print numbers from 5 to 25
# for x in range(5,26):
#     print(x)

#add the nums in between 5 to 10
# sum=0
# for x in range(5,11):
#    sum+=1
# print(sum)

#factorial of given number

# ip=int(input("enter a number:"))
# fact=1
# for x in range(ip,0,-1):
#    fact*=x
# print(fact)

# ip=int(input("enter a number:"))
# fact=1
# for x in range(1,ip+1):
#    fact*=x
# print(fact)
# ecommerce_data = [

#     {
#         "order_id": "O1001",
#         "customer_name": "Ravi Kumar",
#         "city": "Hyderabad",
#         "product": "Wireless Mouse",
#         "category": "Electronics",
#         "price": 799,
#         "quantity": 2,
#         "total_amount": 1598,
#         "payment_method": "UPI",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1002",
#         "customer_name": "Sneha Reddy",
#         "city": "Bangalore",
#         "product": "Bluetooth Headphones",
#         "category": "Electronics",
#         "price": 1999,
#         "quantity": 1,
#         "total_amount": 1999,
#         "payment_method": "Credit Card",
#         "order_status": "Shipped"
#     },
#     {
#         "order_id": "O1003",
#         "customer_name": "Arjun Singh",
#         "city": "Mumbai",
#         "product": "Running Shoes",
#         "category": "Fashion",
#         "price": 2499,
#         "quantity": 1,
#         "total_amount": 2499,
#         "payment_method": "Cash on Delivery",
#         "order_status": "Processing"
#     },
#     {
#         "order_id": "O1004",
#         "customer_name": "Priya Sharma",
#         "city": "Delhi",
#         "product": "Smart Watch",
#         "category": "Electronics",
#         "price": 3499,
#         "quantity": 1,
#         "total_amount": 3499,
#         "payment_method": "Debit Card",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1005",
#         "customer_name": "Kiran Patel",
#         "city": "Chennai",
#         "product": "Laptop Backpack",
#         "category": "Accessories",
#         "price": 1299,
#         "quantity": 3,
#         "total_amount": 3897,
#         "payment_method": "UPI",
#         "order_status": "Shipped"
#     }
# ]
# ##print customer names who is using UPI payment method
# print("customers using UPI :")
# for i in ecommerce_data:
#     if i["payment_method"]=="UPI":
#         print(i["customer_name"])
# print("person who are purchasing quantity more than 1:")
# for i in ecommerce_data:
#     if i["quantity"]>1:
#         print(i["customer_name"])
# print("person who is purchasing other than electronics items:")
# for i in ecommerce_data:
#     if i["category"]=="Electronics":
#         print(i["customer_name"])        
  

##find the divisors of given numbr
#sum of those divisors
# num=14
# x=1
# while x<num:
#     if num%x==0:
#         print(x)
#     x+=1
# num=14
# x=1
# while x<num//2:
#     if num%x==0:
#         print(x)
#     x+=1

# num=14
# x=1
# sum=0
# while x<=num//2:
#     if num%x==0:
#         print(x)
#         sum+=1
#     x+=1
# if sum==num:
#     print('ít is a perfect number')
# else:
#     print('it is not perfect number')            

##perfect square logic-------

# num=14
# x=1
# while x<num:
#     if num%x==0:
#         print(x)
#     x+=1

# num=16
# x=1
# while x<=num//2:
#     if x*x==num:
#         print("it is a perfect square")
#     else:
#         print("not a perfect sqaure")
#     x=x+1

# a="5" 
# b=4
# print(a*b)
#mmobile rating analyzer:
# given a list of mobiles with rating,print 'Best'(>=4.5),"Average"(>=3),"poor"(<3).

# list=[1,2,3,3.5,4,4.5,5]
# mobile_rating=int(input("enter a number:"))
# if mobile_rating >=4.5:
#     print("it is Best")
# elif mobile_rating >=3:
#     print("it is average")
# else:
#     print("it is poor")

 ##Bus tickets system:
input age and print:
<5-----freee
5-60----full ticket
>60------discount
# age=int(input("enter age:"))
# if age <5:
#     print("it is free ticket")
# elif age <=60:
#     print("it is full ticket")
# else:
#     print("it is discount")

##digit count
# num=int(input("enter a number:"))
# digit_count={}
# for digit in number:
#   digit=int(digit)
# if digit in digit_count:
#    digit_count[digit]+=1
# else:
#     digit_count[digit]=1
# print(digit_count)

# employees={"name":"Arun","status":"present",
#            "name":"kiran","staus":"absent",
#            "name":"prem","status":"present",
#            "name":"raji","status":"present",
#            "name":"malli","status":"absent"}
# for emp in employees:
#     if emp["status"]=="present":
#       print(emp["name"])  
# x=7
# y=0
# print(x and y or 10)
# s="education"
# print(s.count("e"))

# x=2
# y=3
# while x<10:
#     x=x*y
#     print(x)

# count of all characters in the string

# str1="MADAM"
# char_dict=dict()
# for char in str1:
#     count=str1.count(char)
#     char_dict[char]=count
# print("Result:",char_dict)

##number of occurrence of a character
# str1="python for begineers"
# char="r"
# count=0
# for i in str1:
#     if i == char:
#         count += 1
# print("number of occurence:",count)

##count number of digits in given number
# x=225
# count=0
# while x>0:
#     ld=x%10
#     count+=1
#     x=x//10
# print(count)

##digit frequency counter:
##number of occurence in given number
# num=int(input("enter a number:"))
# freq={}
# for digit in num:
#     if digit in freq:
#         freq[digit]+=1
#     else:
#         freq[digit]=1
# print("output:", end="")

##amstrongg number
##259=2**3+5**3+9**3=259

