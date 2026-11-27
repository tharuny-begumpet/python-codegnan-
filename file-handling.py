#creating a file
file=open("students.txt","w")
#writing data to the file
file.write("hi students")

file=open("students.txt","r")
data=file.read()
print(data)

#again if we are writing the data which means,previous data will be override/erase and new data will be added
file=open("students.txt","w")
file_data='''hello students how are you'''
file.write(file_data)

file=open("students.txt","r")
data=file.read()
print(data)

#to prevent the data loss we need to open the file in the append mode -"a"
file=open("students.txt","a")
new_data="welcome to python programming"
file.write(new_data)
file.close()

file=open("students.txt","r")
print(file.read())
file.close()

file=open("students.txt","a")
new_data='''\ni can do 
i will definetely achieve this 
i am the best'''
file.write(new_data)

file=open('students.txt','r')
data=file.read()
print(data)
file.close()

# file=open('students.txt','r')
# data=file.read(10)
# print(data)
# file.close()

file=open('students','r')
# print(file.readline())#will read each and every line one by one
# print(file.readline())
# print(file.readline())
# for line in  file:
#     print(line)

print(file.readlines())


#approachable way
with open('students.txt','r') as file:
    for line in file:
        print(line)

    

with open('anualreport.csv','r') as f:
    print(f.read())

# store all prime numbers from 2-1000
# shopping bill generator-poduct name,quantity,price
#calculate individual product cost
#calculate total bill


# Store all prime numbers from 2 - 1000
primes = []
for i in range(2, 1001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)
print(primes)

file = open("primes.txt", "w")
for i in primes:
    file.write(str(i) + "\n")
file.close()


# Shopping bill generator - product_name, quantity, price --> Calculate individual product cost, Calculate total bill
d = {}
total = 0
for i in range(3):
    product_name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    d[product_name] = [quantity, price]
    product_cost = quantity * price
    print(product_cost)
    total += product_cost
print("Total:", total)  



