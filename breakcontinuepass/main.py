# for i in range(10):
#     print(i)
#     if(i==3):
#         break
# print("rest of the code")

# for i in range(10):
#     if(i==3):
#         print(i)
#         break
# print("rest of the code")
# for i in range(10):
#
#     if(i==3):
#         print(i)
#         continue
#         print("rest of the code")
# i=1
# while i<=10:
#     if(i==5):
#         pass
#     print(i)
#     i+=1
# print("rest of the code")
# if 5<3:
#     pass
# else:
#     print("hola")
# print("rest of the code")
# for i in range(4):
#     for j in range(i+1):
#         print("#",end="")
#     print()
# num=10
# for i in range(2,num):
#     if num % i==0:
#         print("not prime")
#         break
# else:
#     print("prime")
n=int(input("enter number"))
count=0
i=1
while i<=n:
      if n%i ==0:
         count+=1
      i+=1
if(count==2):
    print("prime number")
else:
    print("composite number")

