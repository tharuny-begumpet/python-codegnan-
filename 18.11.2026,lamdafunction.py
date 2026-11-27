l=[1,2,3,4,5]
squares=map(lambda x:x*x,l)
print(list(squares))

#map 
l = [1,2,3,4,5]
result = map(lambda x: x*x, l)
print(list(result))

#reduce
from functools import reduce
l = [1,2,3,4,5]
result = reduce(lambda x,y:x+y,l)
print(result)

addition=lambda x,y :x+y
print(addition(10,20))

#filter
nums=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,nums)
print(tuple(even))

nums1=[1,2,3,4,5]
even_odd=map(lambda x:'even' if x%2==0 else 'odd' ,nums1)
print(list(even_odd))

numbers=[1,2,3,4,5]
sum_of_squares=sum(map(lambda x:x*x,numbers))
print(sum_of_squares)



