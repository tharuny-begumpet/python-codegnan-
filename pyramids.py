for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()
print("____________________________")
print("another approach")
for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
print("____________________________")

n=1
for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print(n,end=" ")
            n+=1
        else:
            print(' ',end=" ")
    print()

print("____________________________")

for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print(i,end=" ")
        else:
            print(' ',end=" ")
    print()
print("____________________________")
for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print(j,end=" ")
        else:
            print(' ',end=" ")
    print()

print("-----------------")

n=5
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    print()
print("___________________")
for i in range(4):
    for j in range(4):
        if (i+j)<=(n-1):
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()

print("pyramids")

n=5
for i in range(n):
    for j in range(n-i):
        print(' ',end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

print("_________________________________")

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*n-(2*i+1)):
        print("*",end=" ")
    print()

print("rohmbus")
n=5
for i in range(n):
    for j in range(n-i):
        print(' ',end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(2*n-(2*i+1)):
        print("*",end=" ")
    print()


for i in range(1,5):
    for j in range(i):
        print(i,end=' ')
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
        j+=1
    print()


n=5
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n-i):
        print(' ',end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()