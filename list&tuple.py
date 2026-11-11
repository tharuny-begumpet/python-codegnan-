lst=[]

#list append
lst.append(20)
lst.append(30)
lst.append(40)
lst.append(50)
print(lst)
lst.append([1,2,3])
print(lst)

#list extend
lst.extend([1,2,3,4])
print(lst)

#list insert
lst.insert(0,100)
print(lst)

#remove
lst.remove(100)
print(lst)

element=100
if element in lst:
    lst.remove(element)
    print(lst)

#indexing    
lst1=lst[0:6:2]
print(lst1)
print(lst)

#sort method
lst2=[7,2,5,90,5,8,1,2,5,6]
print(lst2)
#lst2.sort() #lst2 is mutated permanently

#buildin function sorted
lst3=sorted(lst2)
print(lst2)#lst2 can be accessed 

#copy 
#shallow copy
import copy
l1=[10,20,30,[1,2]]
l2=copy.copy(l1)
print(l1)
print(l2)
l1[0]=100
l2[3][1]=1000
print(l2)

#deep copy
import copy
l1=[10,20,30,[1,2]]
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l1[0]=100
l2[3][1]=1000
print(l2)
print(l2)


