# # functions - user defined and pre-defined 
# # pre-defined - input, print, sum, ..... lower(), upper() 
# # user defined functions - def 
# def func1():
#     print("Hello")

# # func1()

# def myfunc(a,b):  # parameters  
#     print(a+b)

# # myfunc(10,14)  # arguments 
# # i=int(input("i "))
# # j=int(input("j "))
# # myfunc(i,j)
# # i=int(input("i "))
# # j=int(input("j "))

# # def myFunc1(a,b,c):
# #     # print(a+b+c)
# #     return a+b+c
# #     # print('hi')
    
# # # print(myFunc1(12,13,14))
# # ans=myFunc1(12,13,14)
# # # print(ans)



# # function with default parameter 

# # def defaultFunc(a,c,b=10):
# #     print(a*b)
    
# # defaultFunc(12,20)


# #keyword arguments 

# # def keyArgs(a,b,c):
# #     print(a,b,c)

# # # i=10
# # # j=20
# # # k=30
# # keyArgs(c=10,b=20,a=30)


# l=[12,13,19,44,32,33]
# # print(sum(l))

# def listSum(a):
#     # print(a)
#     s=0 
#     for i in l:
#         s+=i
#     return s

# print(listSum(l))


# def oddEven(i):
#     if i%2==0:
#         return "Even"
#     else:
#         return "Odd"
# n=int(input("Enter num "))
# print(oddEven(n))

# arbitrary arguments - *args - args - any variable name
# def sumall(*a):
#     # print(a)
#     s=0
#     for i in a:
#         s+=i 
#     print(s)

# sumall(12,13)
# sumall(12,13,15)
# sumall(12,13,15,11)
# sumall(12,13,15,11,45)

# keyword arbitrary arguments - **kwargs 
# def keywordArgs(a,b):
#     print(a,b)
# def keywordArgs(**a):
#     print(a)

# keywordArgs(a=10,b=20)
# keywordArgs(a=10,b=20,c=34)
# keywordArgs(a=10,b=20,c=34,d=44)


# lambda functions - anonymous, single line function
# syntax -  a=lambda paramters: statement 
# l= lambda a,b: print(a+b)
# l= lambda a,b: a+b
# print(l(12,13))
# def oddEven(i):
#     if i%2==0:
#         return "Even"
#     else:
#         return "Odd"
# n=int(input("Enter num "))
# print(oddEven(n))
# oddEven = lambda i:"Even" if i%2==0 else "Odd"
# print(oddEven(23))


# map 
# l=[23,45,33,21,10,14]
# def func1(a):
#     return a+2
# k= map(lambda a:a+2, l)
# print(k)
# print(list(k)) 

# h=map(lambda a,b:a+b, [1,2,3,4],[4,3,5,6])
# print(tuple(h))


# Enumerate function 
# l=[1,2,3,2,4,5]
# # for i in l:
# #     print(i)
# # for i in range(len(l)):
# #     print(i, l[i])

# # for i in enumerate(l):
# #     print(i)
# for i,j in enumerate(l):
#     print(i,"-",j)
    

# d={'name':'jaskaran','class':'btech','rollno':12,'isownapet':True} 
# for i,j in enumerate(d.items()):
#     print(i,"-",j)