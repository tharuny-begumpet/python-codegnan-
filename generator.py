def generator(x):
    yield x
    yield x+1
    yield x+2
result = generator(10)
print(result)
# print(next(result))
# print(next(result)) #no of yeilds ==no of print statements
# print(next(result))

for i in result:
    print(i)

#conversion from iterable to iterator
lst_iterator=iter(lst)
print(lst_iterator)
print(next(lst_iterator))

