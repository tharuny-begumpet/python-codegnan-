age=90
if age>=18:
    print("eligible for voting")
else:
    print("not eligible")

#marks and grades 
marks=90
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("fail")

#Fizzbuzz problem
number=15
if number%3==0 and number%5==0:
    print("fizz buzz")
elif number%3==0:
    print("fizz")
elif number%5==0:
    print("buzz")

#greatest amoung three numbers
a=int(input())
b=int(input())
c=int(input())
#a,b,c=map(int,input().split())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c) 

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)  


#vowel
alphabets=input("enter any character")
vowels='a','e','i','o','u'
if alphabets == vowels :
    print(vowels)
else:
    print("nothing") 
