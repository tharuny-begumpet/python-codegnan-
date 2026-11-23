import addition,division,subtraction,multiplication,square,cube,power,percentage,average,factorial,interest,trigonometry,logarithm
x=addition.addition1(3,5)
y=subtraction.sub1(7,2)
z=multiplication.mul1(10,56)
w=division.division1(9,3)
a=division.division2(10,3)
b=division.division3(10,3)
print(f'summation value is {x} ,difference value is {y}, multiplication value is {z}, division value is {w},modulas is {a}, floorvalue is {b}')
sq=square.square1(5)
sr=square.squareroot(81)
cb=cube.cube1(5)
ex=power.exponent(5,9)
percentage1=percentage.percent(20,750)
average1=average.average1(23,45,35)
print(f'square is {sq},squareroot value is {sr},cube is {cb},power is {ex},percentage is {percentage1},average value is {average1}')
fact=factorial.factorial1(7)
simpleinterest1=interest.simple_interest(10000, 5, 2)
compountinterest1=interest.compound_interest(1000,5,2)

print(f'sin value {trigonometry.sin1(30)}')
print(f'cos value {trigonometry.cos1(60)}')
print(f'tan value {trigonometry.tan1(45)}')

print(f'Natural log value {logarithm.ln1(10)}')
print(f'Common log value {logarithm.log10_1(100)}')
print(f'Log base 2 value {logarithm.log1(8, 2)}')




