name="codegnan"
location="Hyderabad"
branch="python"
print(name,location,branch)

#swapping
x=10
y=20
print(x,y)
x,y=y,x
print(x,y)

x=100
y=200
temp=x
x=y
y=temp
print(x,y)

#Write a Python program to display your name, age, qualification, college name and city using separate print statements.
print("my name is tharuny")
print(21)
print("graduation")
print("Vishwa Vishwani institute of system and management")
print("hyderabad")

#Write a Python program to calculate the total marks and average marks of a student in five subjects. Display the student name, individual subject marks, total marks and average marks. 
# student_name=input("enter your name: ")
# subject1=int(input("enter the marks in subject1 :"))
# subject2=int(input("enter the marks in subject2 :"))
# subject3=int(input("enter the marks in subject3 :"))
# subject4=int(input("enter the marks in subject4 :"))
# subject5=int(input("enter the marks in subject5 :"))
# total_marks=subject1+subject2+subject3+subject4+subject5
# average_marks=total_marks/5
# print(f"the student name is: {student_name}")
# print(f"marks in subject1 {subject1}")
# print(f"marks in subject2 {subject2}")
# print(f"marks in subject3 {subject3}")
# print(f"marks in subject4 {subject4}")
# print(f"marks in subject5 {subject5}")
# print(f"the total marks are {total_marks}")
# print(f"average of the 5subjects: {average_marks}")

# #Question: Write a Python program to collect personal details from a user and display them in a properly formatted profile. 
# name=input("enter the nam of the user :")
# percentage=float(input("enter the percenatage of: "))
# passedout_year=int(input("enter the year o passedout :"))
# print(f"the name of the user is {name}")
# print(f"the percenatage of the user is {percentage}")
# print(f"their passedout year is: {passedout_year}")

#Question: Write a Python program to generate a shopping bill for five products. Accept the product names, quantities and prices from the user. Calculate the individual product costs and display the final bill amount. 
# total_bill=0
# for i in range(1,6):
#     product=input(f"enter the product name : ")
#     quantity=int(input(f"enter the quantity: "))
#     price=float(input("price: "))

#     cost=quantity*price
#     total_bill+=cost


#print(f"Final Bill Amount : {total_bill}")


# Write a Python program to collect employee ID, name, department and basic salary. Calculate HRA (20% of basic salary), DA (10% of basic salary) and gross salary. Display the complete employee salary details.
emp_name=input("enter the employee name: ")
emp_id=int(input("enter your id"))
emp_dpt=input("enter your department")
basic_salary=int(input("enter the salary : "))
hra=basic_salary*0.2
da=basic_salary*0.1
gross_salary=basic_salary+hra+da
print(f"basic_salary is {basic_salary} ,hra {hra} , da {da},gross salary {gross_salary}")


