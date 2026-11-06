#for loops
#N natural numbers that are odd
N=10
for num in range(1,N+1):  #for num in range(1,11,2)
    if(num%2!=0):
        #print(num)
        print(num)

#M even natural statements
M=10
for number in range(1,11):
    if(number%2==0):
        print(number,end=" ")

l=[10,20,30,40,50]
for num in l:
    print(num)
#another approach (for getting elements using index)
#for in in range(len(l))
#   print(l[i])    

name="siri"
# for ch in name:
#     print(ch)
#another approach 
for i in range(len(name)):
    print(name[i])

even_list=[]
odd_list=[]
n=10 
for num in range(1,n):
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

for i in range(10):
    if i==4:
        break
    print(i)

for i in range(10):
    if i==4:
        continue
    print(i,end = " ")

if 10%2==0:
    pass

#while loop
n1=int(input("enter the number: "))
i=n1
while i>=1:
    print(i)
    i-=1

    
        