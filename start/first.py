
'''
First program
'''

# age =  int(input("enter your age"))

# if age >= 18 :
#     print("eligible")
# else :
#     print("not eligible")


'''
Second program
'''

# number = int (input("enter a number : "))

# if number % 2 == 0 :
#     print("even")
# else : 
#     print("odd")
    


'''
Third program
'''


# number = int (input("enter a number : ")) 

# if number > 0 :
#     print("positive number")
# elif number == 0:
#     print("you entered zero please enter another number")
# else: 
#     print("negative number")


'''
3. Largest of Two Numbers

Ask the user for two numbers and print the larger number.
'''

# fNumber = int(input("Enter first Number :"))
# sNumber = int(input("Enter second Number :"))

# if fNumber == sNumber:
#     print("Both number are equals")
# elif fNumber > sNumber :
#     print("first num is largest")
# elif fNumber < sNumber:
#     print("second is laeger") 


'''
Grade Checker

Take marks (0–100) as input and print the grade:

90–100 → A

80–89 → B

70–79 → C

60–69 → D

Below 60 → F
'''

# marks = float(input("enter your marks : "))

# if marks >= 90 :
#     print("A")
# elif marks >=80 :
#     print("B")
# elif marks >=70 :
#     print("C")
# elif marks >= 60 :
#     print("D")
# else :
#     print("F")
    
    
    
'''
5. Leap Year Checker

Ask the user for a year and check if it is a leap year or not.
(Hint: A year is leap if divisible by 4 but not by 100, except if divisible by 400.)
'''

# LP = int(input("Enter a year :"))

# calulate_leap_year = (LP % 4 == 0 and LP % 100 != 0) or (LP % 400 == 0)

# if calulate_leap_year :
#     print("Leap year")
# else :
#     print("Not") 
    
    
'''
Password Validation

Ask the user to enter a password.

If it matches a predefined password, print “Access Granted.”

Else, print “Access Denied.
'''

# password = str(input("enter passowrd : "))


# if password == "pass" :
#     print("Access granted.")
# else :
#     print("check pass")


# --------------------------------- FOR LOOP --------------------------------- #

'''
Print numbers 1 to 10 using a for loop.
'''

# for i in range (1, 10):
#     print(i, end=" ")
    


'''
Print numbers 10 to 1 using a while loop.
'''
 
# i = 10

# while i>1 :
#     print(i)
#     i = i-1
    
'''
Sum of first N numbers: Ask the user for a number N and print the sum of 1+2+…+N.
'''
# ! in range works onlu on " int "


# num = int(input("enter n number : "))

# total = 0

# for i in range(1 , num+1) :
#     total = total + i

# print("The sum of first ", num, "number is :", total )


'''
Even numbers only: Print all even numbers from 1 to 50.
'''

# n = int (input("enter n :"))

# -------------------------------- approach 1 -------------------------------- #
# for i in range(1, n+1,3 ): 
#     print(i)
    
# -------------------------------- approach 2 -------------------------------- #

# for i in range (1,n+1) :
#     if i%2 == 0 :
#         print(i)


'''
Multiplication Table: Ask the user for a number and print its multiplication table up to 10.
'''

# n = int(input("enter table number :"))

# for i in range (1,11): 
#     i = n * i
#     print (i)

'''
Factorial of a number: Ask the user for a number and calculate its factorial.
'''
# n = int(input("enter factorial number :"))

# fact = 1

# for i in range (1, n+1):
#     fact = fact * i
    
# print(fact)


'''
Reverse a string: Ask the user for a string and print it backwards.
'''

# string = input("enter a string")

# -------------------------------- Appraoch 1 -------------------------------- #
# python slicing
# reversed_string = string[::-1]
# print(reversed_string)

# -------------------------------- approach 2 -------------------------------- #
# for loop

# reversed_string = ""

# for i in range(len(string)-1, -1, -1) :
#     reversed_string += string[i]

# print(reversed_string)

# -------------------------------- approach 3 -------------------------------- #
# reversed function

# reversed_string = "".join(reversed(string))
# print(reversed_string)

'''
Count digits: Ask the user for a number and count how many digits it has.
'''
 
# num = int(input("enter a number :"))

# -------------------------------- approach 1 -------------------------------- #
# count = str(num)
# print("total digit in num :" , len(count))


# -------------------------------- approach 2 -------------------------------- #
# count = 0 
# temp = num

# while temp != 0 :
#     temp = temp // 10 
#     count += 1

# print(count)

# ---------------------------------------------------------------------------- #
# ! FUNCTIONS
# ---------------------------------------------------------------------------- #

# ? Wihout prameter
# def greeting() :
#     print("hello")
# greeting()


# ? with parameter
# def greeting(name):
#     print(f"hello, {name}")

# greeting("pranay")

# ? with return value
# def sum(a,b):   
#     add = a+b
#     return add
# result = sum(5,8)
# print(result)


# ?