vowel_count=0
consonent_count=0
str1="project"
for ch in str1:
    if ch in "aeoiuAEIOU":
        vowel_count+=1
    else:
        consonent_count+=1
print(f"no of consonents : {consonent_count},no of vowels : {vowel_count}")

#using functions
def alpa_count(str2):
    vowels=0
    consonent=0
    for ch in str2:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowels+=1
            else:
                consonent+=1
    return[vowels,consonent]
res=alpa_count("honey")
print(res)

#with parameters,with return
def add1(x,y):
    return x+y
z=add1(10,20)
print(z)

#with parameters and with return type:
def div1(a,b):
    if b==0:
        print("division can't be posible,please take another number")
    else:
        return a/b,a//b,a%b
q=div1(15,3)
print(q)

#with parameters and without return type:
def div2(j,k):
    print(j/k)
div2(9,3)


#without parameters and with return type:
def div3():
    u=10
    v=5
    return u/v
result=div3()
print(result)

#without parameters and without return type:
def div4():
    a=10
    b=2
    print(a/b)
res1=div4()

#  Find all prime numbers from 2 to 100
def prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:   
            count += 1 
    if count == 2:  
        return True   
    else:
        return False
for i in range(2, 101):
    if prime(i):
        print(i, end=" ")


#patterns

# 1. SOLID SQUARE STAR

def square_star(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()



# 2. NUMBER SQUARE (1 TO 12)
def number_square(n):
    for i in range(n):
        for j in range(1, n+1):
            print(j, end=" ")
        print()


# 3. ODD EVEN SQUARE
def odd_even_square(n):
    for i in range(n):
        if i % 2 == 0:
            for j in range(1, n+1):
                print(2*j-1, end=" ")
        else:
            for j in range(1, n+1):
                print(2*j, end=" ")
        print()


# 4. DIAGONAL X PATTERN
def diagonal(n):
    for i in range(n):
        for j in range(n):
            if i == j or i+j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# 5. HOLLOW SQUARE
def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# 6. LEFT RIGHT ANGLE TRIANGLE
def left_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()


# 7. LEFT INVERTED TRIANGLE
def left_inverted(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


# 8. RIGHT RIGHT ANGLE TRIANGLE
def right_triangle(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        print()


# 9. RIGHT INVERTED TRIANGLE
def right_inverted(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        print()


# 10. PYRAMID
def pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for j in range(2*i+1):
            print("*", end=" ")
        print()



#11. INVERTED PYRAMID

def inverted_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(2*n-(2*i+1)):
            print("*", end=" ")
        print()


# 12. RHOMBUS / DIAMOND
def rhombus(n):
    # Upper pyramid
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for j in range(2*i+1):
            print("*", end=" ")
        print()

    # Lower inverted pyramid
    for i in range(n-1):
        for j in range(i+1):
            print(" ", end=" ")
        for j in range(2*n-(2*i+3)):
            print("*", end=" ")
        print()


# 13. NUMBER TRIANGLE
def number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()


# 14. CONTINUOUS NUMBER TRIANGLE
def continuous_numbers(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()


# 15. INVERTED NUMBER TRIANGLE
def inverted_numbers(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()


# FUNCTION CALLING

print("\n1. SOLID SQUARE")
square_star(5)

print("\n2. NUMBER SQUARE")
number_square(12)

print("\n3. ODD EVEN SQUARE")
odd_even_square(5)

print("\n4. DIAGONAL X")
diagonal(5)

print("\n5. HOLLOW SQUARE")
hollow_square(5)

print("\n6. LEFT TRIANGLE")
left_triangle(5)

print("\n7. LEFT INVERTED TRIANGLE")
left_inverted(5)

print("\n8. RIGHT TRIANGLE")
right_triangle(5)

print("\n9. RIGHT INVERTED TRIANGLE")
right_inverted(5)

print("\n10. PYRAMID")
pyramid(5)

print("\n11. INVERTED PYRAMID")
inverted_pyramid(5)

print("\n12. RHOMBUS / DIAMOND")
rhombus(5)

print("\n13. NUMBER TRIANGLE")
number_triangle(5)

print("\n14. CONTINUOUS NUMBER TRIANGLE")
continuous_numbers(4)

print("\n15. INVERTED NUMBER TRIANGLE")
inverted_numbers(5)

#  find sum,max,min,avg
d = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

# Function to find sum
def total(d):
    s = 0
    for i in d: # for i in d accesses each key
        s = s + d[i] # d[i] accesses the value corresponding to that key
    return s # Adds all values into s 

# Function to find maximum
def maximum(d):  
    max1 = d["a"] # Initially assumes the first value is maximum
    for i in d: # Compares every value
        if d[i] > max1:
            max1 = d[i]  # Updates maximum whenever a bigger value is found
    return max1

# Function to find minimum
def minimum(d):
    min1 = d["a"]  # Initially assumes the first value is minimum
    for i in d:    
        if d[i] < min1:  # Compares every value
            min1 = d[i]  # Updates minimum whenever a smaller value is found
    return min1

# Function to find average
def average(d):
    s = total(d)
    count = 0
    for i in d:
        count += 1
    return s / count

print("Dictionary:", d)
print("Sum:", total(d))
print("Maximum:", maximum(d))
print("Minimum:", minimum(d))
print("Average:", average(d))

# reverse a string
'''def reverse(s):
    return s[::-1]
s = "python"
print(reverse(s))'''

def reverse(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev
s = "python"
result = reverse(s)
print(result)

#  if target is present return its position otherwise return -1
def search(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1
a = [10, 20, 30, 40, 50]
target = 30
result = search(a, target)
print(result)




