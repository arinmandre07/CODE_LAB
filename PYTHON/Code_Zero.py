## THIS IS THE PYTHON PRACTICE LAB FOR PRACTICING, THE CODES SHOULD BE UN-COMMENTED.
## AND RUN IT IN ORDER TO UNDRESTAND THE WORKING.

## CREDITS: "ARIN MANDRE" 25/09/2023

#______________________________________________________________________________________#


# EXCERCISE 1 *BASIC CALCULATOR*

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))


# print("The value of ", "A", "+", "B", "is :", a + b)
# print("The value of ", "A", "-", "B", "is :", a - b)
# print("The value of ", "A", "*", "B", "is :", a * b)
# print("The value of ", "A", "/", "B", "is :", a / b)
# print("The value of ", "A", "**", "B", "is :", a ** b)

#____________________________________________________________________#

# STRINGS

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# print('He said, "I want to eat an apple".')

# name = "Arin\n"
# friend = "Steve"
# Another_friend = "Alex"
# apple = '''He said,
# hey i am doing great
# I want to eat an apple'''

# print("Hello, " + name + apple)


## We can loop through the strings using a for loop

# print("lets use a for loop\n")
# for character in apple:
#     print(character) 
#____________________________________________________________________#

#STRING SLICING

##EXP 1
# name = "Alex,Tellis"
# print(name[0:4])

##EXP 2
# name = "Alex,Tellis"
# print(name[5:])

##EXP 3
# name = "Alex,Tellis"
# print(len(name[0:4]))

##EXP 4
# fruit = "Mango"
# len1 = len(fruit)
# print("Mango is a", len1, "letter word.")

##EXP 5
# fruit = "Mango"
# mangolen = len(fruit)
# print(mangolen)
# print(fruit[0:4])
# print(fruit[1:4])
# print(fruit[:5])

##EXP 6 //Negative Slicing
# fruit = "Mango"
# mangolen = len(fruit)
# print(mangolen) 
# print(fruit[0:4]) # Including 0 but not 4
# print(fruit[1:4]) # Including 1 but not 4
# print(fruit[:5])
# print(fruit[-1:len(fruit)-3])
# print(fruit[-3:-1])


##QUIZ
# nm = "Harry"
# print(nm[-4:-2])

##Output is = ar

#_____________________________________________________________________________#

#STRING METHODS
# // Strings are immutable

# a = "Chikoo!"
# b = "Chikoo!! Chikoo!!"
# c = "chikoo boka chikoo boka chikoo!"
# print(a)

# print(len(a)) #It returns the lenght of the string.

# print(a.upper()) #The upper() method converts a string to upper case.

# print(a.lower()) #The lower() method converts a string to lower case.

# print(a.rstrip("!")) #the rstrip() removes any trailing characters.

# print(a.replace("Chikoo", "Boka")) #The replace() method replaces all occurences of a string with another string.
 
# print(b.split(" ")) #The split() method splits the given string at the specified instance and returns the separated strings as list items.

# blogHeading = "introdUctIon tO jS" #It not only capitalizes the first character but also turns other characters to lower case.
# print(blogHeading.capitalize())

# str1 = "Welcome to the Console!!!" #The center() method aligns the string to the center as per the parameters given by the user.
# print(str1.center(50))

# print(c.count("chikoo")) #The count() method returns the number of times the given value has occurred within the given string.

# str1 = "Welcome to the Console !!!" #The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
# print(str1.endswith("!!!"))

# str1 = "He's name is chikoo. He is an honest man." #The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
# print(str1.find("is"))

# str1 = "He's name is chikoo. chikoo is an honest man." #The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
# #Traceback Err: print(str1.index("boka"))
# print(str1.index("chikoo"))

# str1 = "WelcomeToTheConsole" #The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# print(str1.isalnum())

# str1 = "Welcome" #The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
# print(str1.isalpha())

# str1 = "hello world" #The islower() method returns True if all the characters in the string are lower case, else it returns False.
# print(str1.islower())

# str1 = "Jai Shree Ram"#The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
# str2 = "Jai Shree Ram\n"
# print(str1.isprintable())
# print(str2.isprintable())

# str1 = "        "       #using Spacebar #The isspace() method returns True only and only if the string contains white spaces, else returns False.
# print(str1.isspace())

# str2 = "        "       #using Tab
# print(str2.isspace())

# str1 = "To Kill a Mocking Bird"  #The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
# print(str1.istitle())

# str1 = "WORLD HEALTH ORGANIZATION" #The isupper() method returns True if all the characters in the string are upper case, else it returns False.
# print(str1.isupper())

# str1 = "It is not a Language its a Snake"#The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
# str2 = "Python is a Interpreted Language"
# print(str1.startswith("Python"))
# print(str2.startswith("Python"))

# str1 = "Python is a Interpreted Language" #The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
# print(str1.swapcase())

# str1 = "he's name is chikoo. chikoo is an honest cat." #The title() method capitalizes each letter of the word within the string.
# print(str1.title())

#____________________________________________________________________________________________________________________________________________________________________________________________#

#IF-ELSE STATEMENTS

# Sometimes the programmer needs to check the evaluation of certain expression(s),
# whether the expression(s) evaluate to True or False. If the expression evaluates to False,
# then the program execution follows a different path than it would have if the expression had evaluated to True.
# Based on this, the conditional statements are further classified into following types:

# if
# if-else
# if-else-elif
# nested if-else-elif.


##IF - ELSE
# EXP 1

# tomatoesPrice = 50
# budget = int(input("Enter the budget for 1kg tomatoes: "))
# if (tomatoesPrice <= budget):
#     print("Alexa, Add 1kg Tomatoes to the cart!")
# else:
#     print ("Sorry! You can't afford it. LOL!")

# EXP 2

# age = int(input('How old are you? '))
# print("Your age is: ", age)

#Conditional Operators
#[ >, <, >=, <=, ==, != ]
 
# if (age>18):
#     print("You can apply for driving lisence, Congrats!!(^_^)")
# else:
#     print("'Go Ride a Bicycle'")

    
##IF-ELSE-ELIF
# EXP 1

# num = int(input("Enter the value of num: "))
# if (num < 0):
#     print("Number is Negative.")
# elif (num == 0):
#     print("Number is Zero.")
# else:
#     print("Number is positive.")            


## NESTED IF-ELSE-ELIF
#EXP 1 

# num = int(input("Enter the value of num: "))
# if (num < 0):
#     print("Number is Negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than or equal to 20 ")
# else:
#     print("Number is Zero")        
        
#_______________________________________________________________________________________________________#                    

#EXCERSICE 2

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

#________________________________________________________________________________________________________#

## MATCHCASE STATEMENTS (NEW UPDATE *PYTHON 3.10*) 

# x = int(input("Enter the required value: "))
# # x is the variable to match
# match x:
#     #if x is 0
#     case 0:
#         print("x is zero")
#     #case with if-condition
#     case 4 if x % 2 == 0:
#         print("x % 2 == 0 and case is 4")
#     #Empty case with if-condition
#     case _ if x < 10:
#         print("x is < 10")
#     #So it is basically just an else statement:
#     case _:
#         print(x)

#__________________________________________________________________________________________________________#


# THE LEGENDARY LOOPS (INTRODUCTION)
# THE FOR LOOP

# name = 'Arin'
# for i in name:
#     print(i)
#     if (i == "A"):
#         print("This Name is Something Special")



# colors = ["Red", "Green", "Blue", "Yellow"]
# for x in colors:
#     print(x)
# for color in colors:
#         print(color)
#         for i in color:
#             print(i)


# for k in range(100):
#     print(k)   



# for k in range(0, 20, 5):
#     print(k)   

## IN THIS CASE THE COUNT STARTS WITH THE FIRST ARGUMENT ENDS AT SECOND AND INCREMENTS THE FIRST BY THIRD


# count = 5
# while (count > 0):
#   print(count)
#   count = count - 1
# else: 
#   print("I am inside else")  

# i = 0
# while(i<=3):
#     print(i)
#     i = i + 1
# print("Done with the loop")    


# i = int(input("Enter the Number: "))
# while(i<40):
#     i = int(input("Entre the final value: "))
#     print(i)
# print("Done with the loop")    

##  BREAK STATEMENT


# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==500):
#         break
#     else:
#         print("Mississippi")
# print("Thank you")


# for i in range (12):
#     if (i == 10):
#         break
#     print("5 X", i+1, "=", 5 * i)

# print("left the loop")    
    

# count = 5
# while (count > 0):
#     print (count)
#     count = count - 1
# else:
#     print("I'm Inside else")



## EXAMPLE TO EMMULATE DO WHILE LOOP IN C
## Do While loop runs to check condition is true or not if true print else exit the loop

# do {
#     #LOOP BODY

# } while (condition);

## EXAMPLE
# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if (i%100 == 0):
#         break


# for i in range (1,1000,1):
#     print(i)
#     if(i == 100):
#         break


#______________________________________________________________________________#


## FUNCTIONS IN PYTHON
## Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
#User Defined

# def name(fname, lname):
#     print("Hello, My first name is ", fname,", And My last name is ", lname )

# name("Bhupendra", "Jogi")
# name("Puneet", "Superstar")
# name("Abdul", "Shinde")

# def name(fname, mname, lname):
#     print("Hello!", fname, mname, lname)    

# name("A", "B", "C")


# def gmean(fnum, Snum):
#     if (fnum > Snum):
#         print("First number is greater")
#     else:
#         print("Second number is greater")    

# gmean( 20, 10)


# def reverse_string(input_str):
#     reversed_str = ""
#     index = len(input_str) - 1
    
#     while index >= 0:
#         reversed_str += input_str[index]
#         index -= 1
    
#     return reversed_str

# # Example usage:
# user_input = input("Enter a string: ")
# reversed_input = reverse_string(user_input)
# print(f"Reversed string: {reversed_input}")



##TO FIND THE AVERAGE USING FUNCTIONS INCLUDING LOOP
# def average(*numbers):
#     sum = 0 
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum/ len(numbers))


# average (5, 6)


##EXAMPLES OF CALLING FUNCTION

##EX1
# def name(fname, mname, lname):
#     # print(type(name))
#     print("Hello,", fname, mname, lname)

# name("Vinayak", "Damodar", "Savarkar")

##EX2
# def name(*name):
#     # print(type(name))
#     print("Hello,", name[0], name[1], name[2])

# name("Vinayak","Damodar","Savarkar")   

##EX3
# def name(**name):
#     # print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Damodar", lname = "Savarkar", fname = "Vinayak")

##EX4
# def name(fname, mname, lname):
#     # print(type(name))
#     return "Hello, " + fname + " " + mname + " " + lname

# print(name("Vinayak", "Damodar", "Savarkar"))


#*__________________________________________________________________________#

## THUMB RULE OF AUTOMATION
# Time_to_automate < (time_to_perform * amount_of_times_done)

# eg. 

# time_to_automate = 10 hours

# time_to_perform = 40 minutes

# Amount_of_times_done = x 

#___________________________________________________________________________*#

## LISTS ##

# lst1 = [1,2,3,4,5,6]
# lst2 = ["Apple", "Grapes", "Orange"]
#          [0]        [1]       [2]
# print(lst1)
# print(lst2)
# print(lst2[1])



# marks = [50,70,90,"Chikoo",80,60]

# if "Chikoo" in marks:
#     print("Yes")
# else:
#     print("NO")    

# if "koo" in "Chikoo":
#     print("Yes")
# else: 
#     print("No")   


#LIST COMPREHENSION

# lst = [i for i in range (1,11)]
# print(lst)
# #WORKING WITH A CONDITION WHENB A CONDITION IS TRUE
# lst = [i*i for i in range (10)if i%2==0]
# print(lst) 

##_______________________ LIST METHODS__________________________ ##

# l = [6,7,8,9,1,2,3,4,5,1]

# l.append(6) # Inserts a value in the list

# l.sort() #Accending Order

# l.sort(reverse=True) #Decending Order

# l.reverse() # Just Reverses the whole list

# print(l.index(7)) # Gives the position value of the number

# print(l.count(1)) # Counts how many times the number appears in the list

# m = l.copy() # Return a copy of the original list

# l.insert(1, 10) #  Insert a value at any given position

# m = [10,11,12,13,14,15] 
# l.extend(m) # Add values from one list to another

# CONCATINATING LISTS
# print(l+m)

# print(l)


##________________________ TUPLES ____________________________________##




# tuple1 = (1)
# print (type(tuple1),tuple)

# tup  = (1,2,3,"Hello", "World")
# print(type(tup), tup)



# country = ("Spain", "Italy", "India", "England", "Germany")
# #            [0]      [1]      [2]       [3]        [4]
# print(country[-1]) # Similar to print(country[len(country) - 1])
# print(country[-3])
# print(country[-4])


# county = ("Israel","Italy","France","Russia","Bharat","Germany")

# if "Russia" in county:
#     print("Congrats! President Putin for winning the Elections of",county[3])
# else:
#     print("Thats Obvio")    


## Tuple[start : end : jumpIndex]

#animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[3:7])     #using positive indexes
# print(animals[-7:-2])   #using negative indexes

# print(animals[::2])     #using positive indexes
# print(animals[-7:-1:2]) #using negative indexes

# print(animals[1:8:3])

## TUPLES METHODS ##

# countries = ("Spain", "Italy", "Bharat", "USA", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[0] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

##Count Method
# Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# num = Tuple.count(3)
# print('Count of 3 in Tuple1 is:', num)

#Give the first Index
# res = Tuple.index(3)
# print('First occurrence of 3 is', res)


##________________________EXERCISE 3__________________________##


# Question = ["1. Who is the captain of Team India? ","2. Who is the Prime Minister of India? ",
#             "3. 5th Largest Economy in the world? ","4. What is a two wheeler also called? "]

# Answers = ["Rohit Sharma","Narendra Modi","Bharat","Motorcycle"]

# ans = ["yes","no"]

# x = str(input("Start the game KAUN BANEGA CROREPATI (yes/no): "))

# if (x == ans[0]):

#     for question in Question:

#         Q1 = str(input(Question[0]))
#         if (Q1 == Answers[0]):
#             print("SAHI JAWAB!, AAPKI DHAN RASHI 5000/-","\n")
#         else:
#             print("APSOS YEH GALAT JAWAB")
#             break

#         Q2 = str(input(Question[1]))
#         if (Q2 == Answers[1]):
#             print("SAHI JAWAB!, AAPKI DHAN RASHI 10000/-","\n")
#         else:
#             print("APSOS YEH GALAT JAWAB")
#             break

#         Q3 = str(input(Question[2]))
#         if (Q3 == Answers[2]):
#             print("SAHI JAWAB!, AAPKI DHAN RASHI 15000/-","\n")
#         else:
#             print("APSOS YEH GALAT JAWAB")
#             break

#         Q4 = str(input(Question[3]))
#         if (Q4 == Answers[3]):
#             print("SAHI JAWAB!, AAPKI DHAN RASHI 20000/-","\n")

#             print("MEHENAT KAR AISE PAISE NHI MILTE! Thanks For Playing.")
#             break

#         else:
#             print("APSOS YEH GALAT JAWAB")
#             break

# else:
#     print("NIKAL BHIKARI")



##___________________________________________________________________________________________________________##
    


## STRING FORMATTING ##
## F_STRING


# sentence = "Hey my name is {} and i am from {}"
# country = "India"
# name = "Arin"

# print(sentence.format(name, country)) # Considerably confusing

# print(f"Hey my name is {name} and i am from {country}") # f-string makes it easier


# val = 'Geeks'  
# print(f"{val}for{val} is a portal for {val}.")  


# name = 'Arin'  
# age = 19  
# print(f"Hello, My name is {name} and I'm {age} years old.")


# price = 49.09999
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))


##___________________________________________________________________##

## DocStrings ##

# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     print(n**2)
# square(5)

# print(square.__doc__)


##__________________________________________________________________##


## RECCURSION ##


# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(4))


##  WORKING OF THE PROGRAM
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1  


##___________________________________SETS_____________________________________________##


## USED TO AVOID REPEATATIVE ENTRIES

# reg = {"Alex","Rohit","Yash","Max","Rohit"}
# print(reg)

# Creating a Empty Set (If set is not defined in this case it is taken as a dictionary by the compiler)
# S = set{}
# print type(S)

## SET MANIPULATION ##

# teams1 = {"Mumbai Indians","Royals Banglore","Chennai Kings"}
# teams2 = {"Kolkata Riders","Rajastan Royals","Pune Giants"}

# print(teams1.union(teams2))  #Used to join two sets
# teams1.update(teams2)

# print(teams1, teams2)


##___________________________________DICTIONARY________________________________________________##

















































