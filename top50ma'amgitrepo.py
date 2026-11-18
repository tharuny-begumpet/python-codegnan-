#sum of all elements in the list
list1=[1,2,3,4,5,678]
#print(sum(list1))
sum=0
for i in list1:
    sum+=i
print(sum)

#largest element
maxx=list1[0]
for i in list1:
    if maxx<i:
        maxx=i
print(maxx)

#smallest element
minn=list1[0]
for i in list1:
    if minn>i:
        minn=i
print(minn)

#count even and odd numbers
numbers=[67,89,45,3,33,66,78,43,42]
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)

#reverse a list
list2 = [9, 5, 6, 4, 3]
l = 0
r = len(list2) - 1
while l < r:
    list2[l], list2[r] = list2[r], list2[l]
    l += 1
    r -= 1
print(list2)








    

