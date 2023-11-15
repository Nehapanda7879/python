# sum=lambda x,y:x+y
# print(sum(5,9))

# add_sub=lambda x,y:(x+y,x-y)
# r,z=add_sub(8,9)
# print(r)
# print(z)
# add=lambda x,y=3:x+y
# print(add(9))
#GLOBAL VARIABLE
# a=10
# def add(n):
#     a=5
#     print(a)
# add(6)
#
# a=10
# def myfun():
#     a+=1
#GLOBAL KEYWORD
# i=0
# def show():
#     global i
#     i+=1
#     print(i)
# show()
# i=1
# def show():
#     global i
#     while(i<10):
#         i+=1
#         print(i)
# show()
#global function
a=90
# def show():
#     a=10
#     print("local variable:",a)
#     x=globals()['a']
#     print("x:",x)
# show()
# print("global variable:A",a)
#pass list into function

# def count(list):
#     even=0
#     odd=0
#     for i in list:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd
# list=[30,89,76,34,67]
# even,odd=count(list)
# print(even)
# print(odd)
#
#fibonacci series
# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# fib(5)
#factorial of a number
# def fact(user):
#   user=int(input("enter a number"))
#   factorial=1
#   for i in range(1,user+1):
#         fact=fact*i
# print(fact(user))
#recursion

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# def greet():
#     print("hello")
#     greet()
# # greet()

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# result=fact(5)
# print(result)
# a=[10,20,40,70]
# def inc(a):
#     return a+2
# result=list(map(inc,a))
# print(result)
# print(type(result))
# for i in result:
#     print(i)
# a=[10,89,78,90]
# result=list(map(lambda n:n+2,a))
# print(result)

# a=[10,89,67,45,78]
# b=[90,76,45,34,30]
# result=list(map(lambda n,m:n+m,a,b))
# print(result)
# for i in result:
#     print(i)

#FILTER
# a=[90,89,56,34,45]
# def marks(n):
#     if n>=90:
#         return True
# result=list(filter(marks,a))
# print(result)

#filter using lambda
# a=[10,89,76,45,34]
# result=list(filter(lambda n:(n>=60),a))
# print(result)
# for i in result:
#     print(i)

#REDUCE
# from functools import reduce
# a=[10,78,56,54]
# result=reduce(lambda n,m:n+m,a)
# print(result)

# num=int(input("Enter The Number to show it factorial:"))
# fact=1
# for x in range(1,num+1):
#      fact*=x
# print("the factorial of this number is({})",fact)
# def decor(fun):
#     def inner():
#         print("before enhancing the function")
#         fun()
#         print("after enhancing function")
#     return inner
# def num():
#     print("we will use this function")
#     print("and will enhance this dict")
# result_fun=decor(num)
# result_fun()
# def decor(fun):
#     def inner():
#         a=fun()
#         add=a+5
#         return add
#     return inner
# def num():
#     return 10
# result_fun=decor(num)
# print(result_fun)
#




