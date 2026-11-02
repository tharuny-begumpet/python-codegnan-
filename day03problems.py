#3 user enter their walking time in N minutes .task:covert the minutes into seconds (int)
N = int(input("Enter your walking time in minutes: "))
seconds = N * 60
print(f"Your walking time in seconds is: {seconds}")

#1 area and perimeter calculation for a house 
# took the shape of the house as a rectangle 
length=float(input("enter the length of the house "))
breadth=float(input("enter the breadth of the house"))
area=length*breadth 
print(f"the area is : {area}")
perimeter=2*(length+breadth)
print(f"the perimeter is : {perimeter}")

#2 volume of a water tank 
#considering the tank to be cuboid 
length1=float(input("enter the length of the water tank"))
breadth1=float(input("enter the breadth of the tank"))
height1=float(input("enter the height of the tank"))
volume=length1*breadth1*height1
print(f"the volume of the tank is:{volume}")

#4 a student plans to read T pages of a book. on day1 she reads p1 pages, on day2 she reads p2 write a expression more how many pages still she has to read to finish the book 
#  pages . write an expression to calculate the number of pages left to read after 3 days.

T=int(input("Enter the pages that you want to read:"))
p1=int(input("Enter the pages completed on day1:"))
p2=int(input("Enter the pages completed on day2:"))

remaining_pages=T-(p1+p2)
print(f"the remaining pages the students neeeds to read to complete the book is :{remaining_pages}")

#5 find the square of a number given number 

number=float(input("Enter a number: "))
square=number**2
print(f"The square of {number} is {square}")

#6 u have D GB a day, u use u1 GB in the morning  , and u2 GB in the evening.write an expression to find how much data is still reamining for the day.
D=float(input("enter the data plan for the day in GB: "))
u1=float(input("enter the the data used int  the morning in GB: "))
u2=float(input("enter the data used int the evening in GB: "))
leftout_data=D-(u1+u2)
print(f"the remaining data for the day is: {leftout_data} GB")

#7 you bought 3 items costing a,b,c. find the total amount you have to pay
a=float(input("enter the price of item a: "))
b=float(input("enter the price of item b: "))
c=float(input("enter the price of item c: "))
total_amount=a+b+c
print(f"the total amount you have to pay is: {total_amount}")

#8 Without using built-in functions ,find the last digit of a 4 digit number 
number1=int(input("enter the 4 digit number"))
last_digit=number1%10
print(f"the last digit of the number is: {last_digit}")

#9 find the average of three numbers 
num1=float(input("enter the first number for average: "))
num2=float(input("enter the second number for average: "))
num3=float(input("enter the third number for average: "))
average=(num1+num2+num3)/3
print(f"the average of {num1},{num2},{num3} is: {average}")

#15 swap two numbers
x=int(input("enter the first number for swapping: "))
y=int(input("enter the second number for swapping: ")) 
print(f"the numbers before swapping are: x={x},y={y}")
temp=x
x=y
y=temp
print(f"the numbers after swapping are: x={x},y={y}")

#16 swap two numbers without using a third variable 
x1=int(input("enter the first number for swapping "))
y1=int(input("enter the second number for swapping "))
print(f"the numbers before swapping are: x1={x1},y1={y1}")
x1,y1=y1,x1
print(f"the numbers after swapping are: x1={x1},y1={y1}")