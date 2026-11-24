#random password generation
import random
characters="ABCDEFGHIJKLMOPQRSTUVWXYZ"
characters += "abcdefghijklmnopqrstuvwxyz"
characters +="0123456789"
characters +="@#$&*!?^%"
password="" 
password_length=int(input())
for i in range(password_length):
    password += random.choice(characters)
print(password)

characters="abcd1234ABCD"
print(random.choice(characters))


#to ensure that all the upper,lower,digits and special characters are present
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
special_characters="@#$&*!?^%"
all_characters=upper_case+lower_case+digits+special_characters
password=[]  #""
password.append(random.choice(upper_case))  #password+=random.choice(upper_case)
password.append(random.choice(lower_case))  #password+=random.choice(lower_case)  
password.append(random.choice(digits))      #password+=random.choice(digits)
password.append(random.choice(special_characters)) #password+=random.choice(special_characters)
length=8
for i in range(length-4):
    password.append(random.choice(all_characters)) #password+=random.choice(upper_case)
random.shuffle(password)
random_password="".join(password)
print(random_password)

#find the frequency or occurence of each and every character in a given string 
s="nandini"
d={}
for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)

#builtin function
from collections import Counter
f=Counter(s)
print(f)

print(d)
print(f)
#print(d['z'])  #keyerror would occur
print(f['z'])  # error won't occur if the element is not present (usefull for mathematical calculations)

#snake and ladder
import random
count=0
rolls=0
while True:
    input("click enter to roll the dice")
    dice=random.randint(1,6)
    if count+dice<=100:
        count+=dice #count=count+dice
    print(f"your dice value is {dice}")
    print(f"you are at {count} position")
    rolls+=1
    if count==100:
        print(f"you win at {rolls} rolls")
        break


import random
snakes = {
    27: 5,
    40: 3,
    54: 31,
    66: 45,
    76: 58,
    99: 41
}
ladders = {
    4: 25,
    13: 46,
    33: 49,
    42: 63,
    50: 69,
    62: 81,
    74: 92
}
player1 = 0
player2 = 0

rolls1 = 0
rolls2 = 0

turn = 1

while True:

    if turn == 1:
        input("\nPlayer 1 - Press Enter to roll the dice...")
        dice = random.randint(1, 6)

        print(f"Player 1 rolled: {dice}")

        if player1 + dice <= 100:
            player1 += dice

        if player1 in ladders:
            print(f" Ladder! {player1} -> {ladders[player1]}")
            player1 = ladders[player1]

        if player1 in snakes:
            print(f" Snake! {player1} -> {snakes[player1]}")
            player1 = snakes[player1]

        print(f"Player 1 Position: {player1}")

        rolls1 += 1

        if player1 == 100:
            print(f"\n Player 1 Wins in {rolls1} rolls!")
            break

        turn = 2

    else:

        input("\nPlayer 2 - Press Enter to roll the dice...")
        dice = random.randint(1, 6)

        print(f"Player 2 rolled: {dice}")

        if player2 + dice <= 100:
            player2 += dice

        if player2 in ladders:
            print(f" Ladder! {player2} -> {ladders[player2]}")
            player2 = ladders[player2]

        if player2 in snakes:
            print(f" Snake! {player2} -> {snakes[player2]}")
            player2 = snakes[player2]

        print(f"Player 2 Position: {player2}")

        rolls2 += 1

        if player2 == 100:
            print(f"\n Player 2 Wins in {rolls2} rolls!")
            break

        turn = 1

#py audio
#py text
#py speech recognition
