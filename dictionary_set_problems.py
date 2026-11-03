details={"name":"tharuny",
         "age":21,
         "gender":"female"}
print(details)

#accessing the values
print(details["name"])

print(details.values())
print(details.keys())
print(details.items())

from collections import Counter
dict1="banana"
print(Counter(dict1))

stud_names=["nani","vinay","swathi"]
stud_marks=[90,80,70]
dictionary2=dict(zip(stud_names,stud_marks))
print(dictionary2)
print(max(dictionary2.values()))

print(details | dictionary2)

#set
set1={10,20,40,58}
print(set1)

set1.add(20)
print(set1)
set1.update({58,98,89})
print(set1)

set2={67,89,39}
set2=set1.union(set2)
print(set2)

set3=set2.intersection(set1)
print(set3)

a = {10,20,30,40}
b = {20,40}
c=a-b
print(c)
c=a^b
print(c)

python = {"Arrays","Strings","Dictionary","Set"}

java = {"Loops","Strings","Set","Oops"}
common_sub=python.intersection(java)
print(common_sub)

list_3=["Rahul","Ravi","Rahul","Sneha","Ravi","Amit"]
print(set(list_3))

dictionary_3={"employee_iD":89,
"name":"usha",
"Department":"cse",
"Salary":50000}
print(dictionary_3)
dictionary_3.update({"Salary":55000})
print(dictionary_3)

phone_dict={"abhi":9867598846,"hari":8947368279,"usha":9084927834}
print(phone_dict.get("abhi"))

super_market={"soup":98,"sugar":57,"salt":90}
print(sum(super_market.values()))

key = ["A","B","C","D"]
value = [10,20,30,40]
dict_09=dict(zip(key,value))
print(dict_09.values())
print(dict_09.keys())
dict_09["C"]=100
print(dict_09)
dict_09.pop("A")
print(dict_09)
dict_09["E"]=50
print(dict_09)
