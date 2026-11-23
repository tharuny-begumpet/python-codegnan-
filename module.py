#builtin modules
import math
print(math.sqrt(16))

print(math.factorial(9))
print(math.pi)

#another approach
from math import sqrt
print(sqrt(9))

#alias
import math as m
m.sqrt(36)

from math import factorial as f
print(f(6))


import math as m
print(m.sqrt(25))
print(m.factorial(6))
r=m.pi
print(r)

from math import sqrt as square_root
print(square_root(36))
print("pi",math.pi)
print("power",math.pow(2,3))
print("ceil",math.ceil(4.8))
print("floor",math.floor(4.9))
print("factorial",math.factorial(5))
print("log value",math.log(10))
print("sin",math.sin(30))
print("cos",math.cos(30))
print("tan",math.tan(100))

import math
radius=5
area=math.pi*math.pow(radius,2)
print(area)


print("random builtin module")

import random
print(random.randint(1,6))#6 would also be included unlike range function

import random
print(random.random())#0 to 1

print(random.randrange(1,10))# last number excluded 

rakhis=["designed","home_made","silver_rakhi","thread"]
print(random.choice(rakhis))#choice - any iterable accepted (any datatype in the iterable)

print(random.choices(rakhis,k=3))  #choices may result in duplicates or may result uniquely

numbers=[10,20,30,40,50]
print(random.sample(numbers,3))#no duplicates would occure only unique values

random.shuffle(numbers)
print(numbers)

print("sys builtin module")
import sys   # hardware related information for the computer
print(sys.version)
print(sys.platform)

age=15
if age<18:
    print("not eligible")
    sys.exit()  #to stop the execution 
print("eligible")


print(sys.path)   #path where we are
#platform module
import platform
print(platform.system())
print(platform.release())
print(platform.machine())
print(platform.processor())
print(platform.python_version())



from collections import defaultdict
d = defaultdict(int)
d["apple"] = 1
print(d["name"])
# dic = {'a':2,'b':5,'c':10}
# print(dic['x'])
# d = {}
# print(d["name"])


from collections import deque
d = deque([1,2,3])
d.append(4)
d.appendleft(10)
d.pop()
d.popleft()
print(d)

from itertools import permutations   #the way in which the data present is arranged
numbers=[1,2,3,5]
print(list(permutations(numbers)))

from itertools import combinations  #the way in which data is arranged in a unique uniques i.e ., if (1,2) is there , there wont be (2,1)
numbers=[1,2,3,4]
print(list(combination(numbers,3)))

from datetime import datetime
now=datetime.now()
print(now)
print()
print(now.time)



