##functionss

# function is a block of code/instruction to perform certain task based on the requirement and may or may not return the value.
# A function never excutes until it called by someone
# A function is a resuable block or container we can work with different types of inputs and gives outputs accordingly.
# idea of functions is to avoid repeatation of same logic kind of code instead of it keeping it in a block and can resuse the block with different type of inputs

# 1.predefined/built in........

##functions which are defined already by python itself for certain tasks.....

#2.userdefined function...
#functions which can be defined by as per his requirements then it is said to be userdefined functions

# a.static functions:-

#function which will give always fixed output whenever we call.

# b.dynamic funtions:-

# #function which can give different outputs based on inputs


# # Syntax
# #def func_name():#function definition

#     #\\Code  ##function body

# def sample():
#     print('hello im a sample function')
#     return 'thankyou'## to return any value specifically we can use return
# print(sample())


# def sample():
#     print("hello iam sample funtion")
#     return"thankyou"
#     print('visit the sample function')##the code what we write after the return statements they wont executes simply wll ignore

# print(sample())

# def sample():
#     print("hello im a sample function")
#     print("visit the sample function")
#     return"thankyou"
# print(sample())   

##to say hello for a student using a function as per his name
# def greetings(name):
#     print(f"hello {name}")
# greetings('kiran')
# greetings('arun')
# greetings('prem')
# greetings('hema')
    
# print(greetings("uday"))

##by default a function can return none as a value


# def showtime(name,movie):
#     print(f"{name} is watching {movie}")
#     return"thankyou for visiting us"

# print(showtime('arun','sarvam maya'))
# showtime("prem","OG")

##write a function to calculate the movie ticket
# def movie_ticket(price,quantity):
#     total=price*quantity
#     print(f"total amount is {total}")
# movie_ticket(200,3)

# ##dynamic functions:
# def dynamic(x,y,z):##parameters
#     print(x+y+z)
# dynamic(2,4,6)##arguments

##arguments
# 1.positional arguments----always positions of parameters and arguments should be match here
# 2.keyword arguments-------we use this when  we don't know the sequence or position of arguments 
# 3.arbitary arguments-----whenever we don't kncow how many arguments are passing then arbitary arguments are used
# 4.keyword arbitary----here n number of arguments can be pass with there keywords
# 
# 1.positional arguments:
# def student_info(sname,degree):
#     print(f"{sname} is prusuing {degree}")

# student_info('arun','b.tech')
# student_info('kiran','MBA')

# 2.keyword arguments

# def student_info(sname,degree):
#     print(f"{sname} is pursuing {degree}")

# student_info(degree='b.tech',sname='arun')

# 3.arbitary arguments--
 
# def demo(*ip):
#     print(ip)

# demo(1,2,3,4)
# demo('soap','shampoo','deodrant','snacks',)
# demo('chicken','mutton')
    
# 4.keyword arbitary--arg(**args)

# def demo1(**ip1): 
#     print(ip1)

# demo1(first='ram',third='bharath',second='lakshman')

##default parameter
#Always default parameter shouls pass end of the params
#whenever value is fixed/default we can use default params

# def student_info1(sname,city,batch='d10'):
#     print(f"{sname} is in {city} of batch {batch}")
          
# student_info1('arun','hyd')
# student_info1('kiran','hyd')
# student_info1('prem','medchal')
# student_info1('malli','hyd','d11')

# def student_info1(sname,city,batch='d10',institute='10000coders'):
#     print(f"{sname} is from {city} in batch {batch} from {institute}")

# student_info1("arun","hyd")
# student_info1("prem","medchal",'d11')

# def sum(a,b):
#     print(a+b)
#     return "something"
#     print("hello")##this will never execute
# x=sum(3,4)
# print(x)

# write a function that returns the length of given 

# def find_length(ip):
#     op=len(ip)
#     return op
# print(find_length("hello world"))
# print(find_length("something"))
# print(find_length([1,2,3,4]))
# print(find_length([4,5,6,7]))

##using a function find the length of the given input without using len method

def find_length(x):
    count=0
    for i in x:
        count+=1
    return count
print(find_length('hello'))
print(find_length("something"))
print(find_length([1,2,3,4]))
print(find_length([4,5,6,7]))
print(find_lenth(123))###we cant use loops for numbers
##only we use for list,tuple
x=123
print(isinstance(x,int))
##isinstance is used to check
whether x is int or not
