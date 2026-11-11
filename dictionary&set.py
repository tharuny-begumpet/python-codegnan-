#set
s={1,2,3,5}
#add
s.add(10)
print(s)
#remove
s.remove(10)
print(s)
#reemove the element that is not present in the set
#s.remove(10)
#print(s)
#remove the element using discard method
s.discard(10)
print(s)

#set operations
s3={10,20,30,40}
s4={40,50,60}
print(s3)
print(s4)
#union
print(s3.union(s4))
print(s3|s4)
#intersections
print(s3.intersection(s4))
print(s3&s4)
#differnce 
s5=s3.difference(s4)
s5=s3-s4
print(s5)
#symmetric difference
s6=s3.symmetric_difference(s4)
s6=s3^s4
print(s6)

#is subset and superset
s7={26,45,18,1,4}
s8={26}
print(s7.issuperset(s8))
print(s8.issubset(s7))

#Dictionary
d={}
d1=dict()
d2={'a':1,
    'b':2,
    'c':3}
print(d2['a'])

print(d2.values())
print(d2.keys())
print(d2.items())
d2['c']=5
print(d2)
d2['d']=4
print(d2)
#update
d2.update({'e':6})
print(d2)
d2.update(f=6)
print(d2)
d2.pop('b')
print(d2)
d2.pop('b',None)
print(d2)
#popitem
d2.popitem()
print(d2)

#find the missing numbers
s1={10,45,62,75,43}
s2={45,10,1}
missing_numbers=s1^s2
print(f"the missing numbers are :{missing_numbers}")

#find unique characters 
word="innovation"
unique_characters=set(word)
print(f"the unique characters are :{unique_characters}")

#create a dictionary from two lists 
std_names=["vishal","siri","swathi"]
std_marks=[90,80,70]
student_dict=dict(zip(std_names,std_marks))
print(f"the student dictionary is :{student_dict}")

#calculate total marks
marks={"python":85,"aptitude":90,"soft_skills":95}
total_marks=sum(marks.values())
print(f"the total marks are :{total_marks}")

#counter
from collections import Counter
string3="engineering"
result=Counter(string3)
print(f"the character frequencies are :{result}")

print("swapping two numbers using ^ operator")
a=20
b=60
print(f"the values of a and b before swapping are : {a} and {b}")
a=a^b
b=a^b
a=a^b
print(f"the value of a is :{a}")
print(f"the value of b is :{b}")




