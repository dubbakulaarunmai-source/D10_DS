##looping statements("iterative"or "repetative")
# statements which excutes continuosly in a loop until it meets certain condition

# 1.for loop
# whenever if u want to use loop for the sequence type data we can use one type of for loop
# list1=['arun',5,0.5]
# for i in list1:
#      print(list1[0])

# str1="data science"
# for i in str1:
#     print(i)
# list1=['arun',5,0.5]
# for i in list1:
#         print(list1[0])


# list1=['hi','hello','some','welcome','thankyou']
# print(list1)

# list1=['hi','hello','some','welcome','thankyou']
# for i in list1:
#     print(i)
# list1=['hi','hello','some','welcome','thankyou']
# for i in list1:
#     print(list1[4][5])

# dict1={'name':'harish','city':'hyd','role':'developer'}
# print([dict1['name']])
# dict1={'name':'harish','city':'hyd','role':'developer'}
# for x in dict1:
#         print(x)
# dict1={'name':'harish','city':'hyd','role':'developer'}
# for x in dict1:
#    print(dict1[x])
# dict1={'name':'harish','city':'hyd','role':'developer'}
# for x in dict1:
#         print(f"{x}:{dict1[x]}")

# set1={'karun','kiran','shiva','yamini','arun','prem'}
# for name in set1:
#         print(name)

##print number from 1 to 10
# for x in range(1,11):
#         print(x)

#print squares of number from 10 to30
# for x in range(10,31):
#  print(x**2)


# list1=[10,23,45,31,24,67,87,45,34]
# x=1
# for num in list1:
#         print(x+num)
#         x+=1

#from number 1 to 50 count how many can be divisible by 3 and 5

# count=0
# for i in range(1,51):
#         print(i)
#         if i%3 or i%5==0:
#                 count+=1
#                 print(i)
# print(count)     
# 
# 
# from 1 to 30 add even numbers and multiply odd number using for loop
# sum1=0
# prod=1
# for x in range(1,31):
#         if x%2==0:
#            sum1+=x
#         else:
#               prod*=x
# print(f"sum of the even numbers are:{sum1}")
# print(f"product of odd numbers are:{prod}")              



        

##while loop
#to excute set of statements in an infinite loop until it meets certain condition we can use while Loop
#Syntax
# while condition:
#     //statements


##while loop is a never ending loop until it condition becomes false

# while True:
#     print('hello')

# is_recharge=True
# while is_recharg
#     print('can make calls and browser internet')
     

# limit=30
# starts=1
# while starts<=limlit:
#     print('able to make calls and browser internet')
#     starts+=1
# for x in range(1,31):/

# candies=10
# for i in range(candies):
#     print("giving a candy to a friend")
#     if candies-i==5:
#         print("only 5 candies left stopping distribution") 
# #         break

# i=1
# while i<=5:
#     print("Telsuko",end="")
#     j=1
#     while j<=4:
#         print("Rocks",end="")
#         j=j+1
#     i=i+1
#     print()   
  
# plan=30
# current_day=1
# while current_day<=plan:
#     print("watch and enjoy netflix")
#     current_day+=1

# i=1
# while i<=5:
#     print("hello")
#     i=i+1

# str1='something'
# x=0
# while x<len(str1):
#     if str1[x] in 'aeiou':
#       print(str1[x])
#     x=x+1

# str1='something'
# # x=len(str1)-1
# # count+=1
# # while x>=0:
# #     print(str1[x])
# #     x-=1
#coverting number into string
# num=48962
# str1=str(num)
# x=0
# while x<=len(str1)-1:
#     print(str1[x])
#     x+=1

# num=158
# while num>0:
#     id=num%10
#     print(id)
#     num=num//10

#count the numbers
# num=158
# count=0
# while num>0:
#     id=num%10
#     count+=1
#     num=num//10
# print(count)

#sum of the numbers
# num=1245
# sum=0
# while num>0:
#     id=num%10
#     sum+=id
#     num=num//10
# print(sum)

#palindrome
# num=965
# num1=num
# rev=0
# while num>0:
#     id=num%10
#     rev=rev*10+id
#     num=num//10
# print(rev)
# if rev==num1:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

## calculates the movie tickets price
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

