#1Print the first character of a string
str1=input("enter the string: ")
print(f"the first character of the string is : {str1[0]}")
#2Print the last character of a string
print(f"the last character of the string is : {str1[-1]}")
#3Print the third character of a string
print(f"the third character of the string is: {str1[2]}")
#4Print the second last character of a string
print(f"the second last character is :{str1[-2]}")
#5Print the length of a string
print(f"the length of the string is :{len(str1)}")
#6Print the first 3 characters of a string
print(f"the first 3 characters are:{str1[0:3]}")
#7Print the last 4 characters of a string
print(f"the last four characters of string is:{str1[-4:-1]}")
#reverse of a string 
print(f"the reverse of the strng is :{str1[-1::-1]}")
#8Print every alternative character of a string
print(f"every alternative character of string:{str1[0::2]}")

str2=input("enter the string: ")
#concatenation
print(f"concating {str1},{str2}:{str1+str2}")
#repeatition
print(f"repeat the string :{str1*3}")
#check whether a string is present in another string
character1=input("enter the character to be checked : ")
if character1 in str1:
    print(f"{character1} is present in {str1}")
#Print only the middle character of a string with an odd length
name="tharuny"
if len(name) % 2 == 1:
    middle_index = len(name) // 2
    print(f"the middle character of the string is : {name[middle_index]}")

#split
str3=input("enter the string to be splited: ")
print(f"the string after split is :{str3.split( )}")

#list problems
#creating and printing 

lst1=list(map(int,input("enter the elemnets in the list: ").split( )))
print(lst1)

#1st element 
print(f"the first element from the list is :{lst1[0]}")

#last element
print(f"last element of thestring is:{lst1[-1]}")

#third element
print(f"the third element of the list is :{lst1[2]}")

#length 
print(f"the length of the list is :{len(lst1)}")

#first three elements of the list
print(f"the first three elements of list: {lst1[0:3]}")

#last four elements of the list 
print(f"the last four elements of the list:{lst1[-4::-1]}")

#list in reverse 
lst1.reverse()
print(f"the list in reverse order is :{lst1}")

#alternate elememts
print(f"every alternative element :{lst1[0::2]}")

lst2=list(map(int,input("enter the elements in the list:").split(',')))
lst3=list(map(int,input("enter the elements in the list:").split(',')))
#concatenation
print(f"the concatenation of the two lists is :{lst2+lst3}")

lst4=lst2.append(lst3)
print(f"the list after appending is :{lst4}")

lst5=lst2.extend(lst3)
print(f"the list after extending is :{lst5}")

#insert
lst2.insert(0,100)

#remove
lst2.remove(100)
print(f"the list after removing the element is :{lst2}")

#pop
lst2.pop(0)
print(f"the list after popping the element is :{lst2}")

#clear
lst2.clear()
print(f"the list after clearing the elements is :{lst2}")

#del
del lst2[0]
print(f"the list after deleting the element is :{lst2}")

#sort
lst1.sort()
print(f"the list after sorting is :{lst1}")

#sorted
lst6=sorted(lst3)
print(f"the list after sorting is :{lst6}")

#challengs 

text="Python Programming"
text1=text.split()[1]
print(f"the second word in the string is :{text1}")

text3="codegnan hyderabad"
text4=text3.split()[1]
print(text4)

text5="Artificial Intelligence"
text6=text5.split()[0]
print(text6)

s="this is python class from morning to evening"
words=s.split()
largest_word=max(words,key=len)
print(f"the largest word in the string is :{largest_word}")



