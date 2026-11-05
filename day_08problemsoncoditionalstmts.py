#a user tries to withdraw money from atm.if withdrawal amount is less than the balance.allow it.otherwise,show insuffient balance.display the transaction result.
# balance=50000
# amount=int(input("enter the amount for withdrawal: "))
# if (amount%100==0) or (amount%200==0) or (amount%500==0):
#   if amount<balance:
#     balance=balance-amount
#     print(f"amount withdrawn is: {amount}")
#     print(f"balance remaining is: {balance}")
#     print("withdrawal successfull")
#   else: 
#      print("insuffient balance")
# else:
#     print("please enter correct amount")

# #if total bill is 2000 or more give 20% discount otherwise no disciunt

# total_amount=float(input("enter the bill: "))
# discount=0
# if total_amount>=2000:
#    discount = total_amount*0.2
#    print(f"disciunt amount is: {discount}")
#    amount_after_discount=total_amount-discount
#    print(f"please pay: {amount_after_discount}")
# else:
#    print("no discount applied")

# #a system checks password length .the length is 8 or more ,password accepted.otherwise,rejected.print the result

# password=input("enter the password :")
# #print(len(password))
# if len(password)>=8:
#    print("password accepted")
# else:
#    print("rejected .please enter the password of legth 8 or more characters")

#read time in 24 hour format and covert to 12hr format with am and pm
# hours=int(input("enter the time :"))
# minutes=int(input("minutes : "))
# if hours>=12:
#    hours=hours%12
#    print(f"time in 12hour format is: {hours}:{minutes}")
# else:
#    print(f"{hours} : {minutes}")

# positive even 
# positive odd
# negative even
# negavtive odd
#zero
# number=int(input("enter the number : "))
# if number>0:
#    if(number%2==0):
#       print(f"the {number}is positive even")
#    else:
#       print(f"the {number} is positive odd")
# elif number<0:
#    if(number%2==0):
#       print(f"the {number} is negative even")
#    else:
#       print(f"the {number} is negative odd")
# else:
#    print(f"the {number} is zero")

#another approach
number=int(input("enter the number : "))
if number>0 and number%2==0:
   print("positive even")
elif number>0 and number%2!=0:
   print("negative even")
elif number<0 and number%2!=0:
   print("negative odd")
else:
   print("zero")

#checking if a number is 2-digit number
two_digtinum=int(input("enter the number to be checked: "))
if (two_digtinum>10) and (two_digtinum<99):
   print("the number is two digit number")
   




