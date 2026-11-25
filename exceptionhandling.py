# a = int(input())
# b=int(input())
# print(a/b)
# try:
#     a = int(input())
#     b=int(input())
#     print(a/b)
# except:
#     print("code has zero division error")
# else:
#     print("code doesn't have any error")

# finally:
#     print("code executed")

# a = int(input())
# b=int(input())
# print(a/b)
# try:
#     a = int(input())
#     b=int(input())
#     print(a/b)
# except ZeroDivisionError as e:
#     print(e)
#     #print("code has zero division error")
# else:
#     print("code doesn't have any error")

# finally:
#     print("code executed")



# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except ZeroDivisionError as e:
#     print(e)
#     # print("Your code has some error")
# except ValueError as e:
#     print(e)
# else:
#     print("Code doesn't have any error")
# finally:
    #print("Code executed")

#raise keyword
# def div(x,y):
#     if x==0:
#         raise ZeroDivisionError()
#     return x/y
# #div(3,0)
# #exception handling
# try:
#     div(10,0)  #error code
# except:
#     print("division with zero")

#CUSTOM EXCEPTION
#if user want to create an exception,we can call it custom exception
class NegativeBlanaceError(Exception):
    pass

def withdraw(amount):
    balance=10000
    if amount<0:
        raise NegativeBlanaceError()
    balance=balance-amount
    return f'{amount}withdraw,current balance is {balance}'
#withdraw(500)
try:
    a=withdraw(-300)
    print(a)
except:
    print('amount is negative')


#ANOTEHR ERROR
class InvalidAgeError(Exception):
    pass

def vote(age):
    if age < 18:
        raise InvalidAgeError()
    return "You can vote"

try:
    print(vote(16))
except InvalidAgeError:
    print("Age should be 18 or above")

#out of stock error

class OutOfStockError(Exception):
    pass

def buy(quantity):
    stock = 10
    if quantity > stock:
        raise OutOfStockError("the item is out of stock")
    stock = stock - quantity
    return f"{quantity} items purchased. Remaining stock is {stock}"
try:
    result = buy(15)
    print(result)
except OutOfStockError:
    print("Product is out of stock")


#exsisting username error
def check(username):
    username1=["varsha@12","nisha@34","usha@54"]
    if username in username1:
        raise check(f'the {username}already exsists')
    else:
        return f'{username} available'
try:
    print(check("varsha@13"))
except check:
    print("username already exsists")




    



