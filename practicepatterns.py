for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()
print("_______________________________")
#borders  
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(' ',end=" ")

    print()
print("_______________________________")

n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
print("_________________________________")
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()
print("___________________________")
num=1
for i in range(n):
    for i in range(n):
        print(num,end=" ")
        num+=1
    print()

print("_____________________")
odd=1
even=2
for i in range(1,n):
    for j in range(1,n):
        if i%2!=0:
            print(odd,end=" ")
            odd+=2
        else:
            print(even,end=" ")
            even+=2
    print()

print("__________________")
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()

print("___________________")
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
print("________________")
n=5
for i in range(n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    





