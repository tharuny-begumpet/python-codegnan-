# num=int(input("enter the number: "))
# print(f"The factors of {num} are:")
# for i in range(1,num+1):
#     if num%i==0:
#         print(i,end=' ')
#         print()

# #printing the number of odd numbers in a range 
# odd_number=int(input("enter the number: "))
# print("the number of odd number are: ")
# count=0
# for i in range(1,odd_number+1):
#     if i%2!=0:
#         count+=1
# print(count)

#checking if it is a prime number
# n=int(input("enter the number to be checked"))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print("f the number {n} is prime")
# else:
#     print("not prime")

#checking if the number is perfect
# perfect_number=int(input("enter the number: "))
# list1=[]
# for i in range(1,perfect_number):
#     if perfect_number%i==0:
#        list1.append(i) 
# sum1=sum(list1)
# if sum1==perfect_number:
#     print(f"{perfect_number} is a perect_number")   
# else:
#     print("not a perfect number")     

# #another approach
# number2=int(input("enter the number:"))
# summ=0
# for i in range(1,number2):
#     if number2%i==0:
#         summ+=i
# if summ==number2:
#     print("perfect number")
# else:
#     print("not perfect")

# l=list(map(int,input().split(",")))
# #print(min(l))
# mini=l[0]
# for i in l:
#     if i<mini:
#         mini=i
# print(i)

# list1=list(map(int,input("enter the elements in the list: ").split(",")))
# maxi=list1[0]
# mini=list1[0]
# sum1=0
# length=0
# for i in list1:
#     if i>maxi:
#         maxi=i
#     if i<mini:
#         mini=i
#     sum1+=i
#     length+=1
# print(maxi)
# print(mini)
# print(sum1)
# print(length)

#1. Sum of all elements
# Find the sum of all elements in a list.
list_1=list(map(int,input("enter the values of list: ").split(",")))
suml=0
for i in list_1:
    suml+=i
print(suml)


