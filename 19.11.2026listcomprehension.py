nums=[10,2,3,4,-2,6]
r=[x for x in nums]
print(r)       #[10, 2, 3, 4, -2, 6]
name="tharuny"
#s=[x for x in name]      ['t', 'h', 'a', 'r', 'u', 'n', 'y']
s=[x.upper() for x in name]
print(s)       #['T', 'H', 'A', 'R', 'U', 'N', 'Y']

#conditional statement in list comprehension
l=[14,78,54,78,54,34,25,76,79,99]
even=[x for x in l if x%2==0]
print(even)

#range
# n=int(input("enter the range"))
# numbers=[i for i in range(1,n+1)]
# print(numbers)

#get all the even positioned elements in a tuple 
t=(-2,45,72,11,1,3,38,14,61)
even_positioned=[t[x] for x in range(len(t)) if x%2!=0]
print(even_positioned)  #[45, 11, 3, 14]

#get all the even index elements in a tuple
even_indexed=[t[x] for x in range(len(t)) if x%2==0]
print(even_indexed)   #[-2, 72, 1, 38, 61]

#if -else
numbers=[1,4,2,5,6,4,6,33,89,45]
even_odd=['even' if num%2==0 else 'odd' for num in numbers]
print(even_odd)  #['odd', 'even', 'even', 'odd', 'even', 'even', 'even', 'odd', 'odd', 'odd']

#generate sqaures of the sequence from 1 to 10
num1=10
squares=[i**2 for i in range(1,num1+1)]
print(squares)

#length of the strings in a string 
list1=['python','code','program']
lengthof_strings=[len(i) for i in list1]
print(lengthof_strings)

#extract the numbers divisible by 3 and 5
number_limit=20
divisibility_check=[x for x in range(1,number_limit+1) if x%3==0 and x%5==0]
print(divisibility_check)

#extract all the words having more than 5 characters 
words=["vishnuva","uday","yuvan","shreya","varsha"]
limit_5=[ch for ch in words if len(ch)>5]
print(limit_5)
#s="comprehenssion" get all the vowels from the given string
s="comprehenssion"
v=("aeiouAEIOU")
vowels1=[x for x in s if x in v]
print(vowels1)

#find all the prime numbers from 1 to 100
prime = [n for n in range(2, 101) if all(n % i != 0 for i in range(2, n))]
print(prime)

#another approach
prime_number=[n for n in range(2,101) if len([factor for factor in range(1,n+1) if n%factor==0])==2]
print(prime_number)

#nested loops 
l = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print(l)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#matrix[1][2]
diagonal=[matrix[i][j] for i in range(3) for j in range(len(matrix[i])) if i==j]
print(diagonal)




