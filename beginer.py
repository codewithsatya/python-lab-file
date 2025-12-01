# write a Python program to calculate number of days 
# between two dates. Sample dates: (2014, 7, 2), (2014, 7,11) Expected output : 9 days  
from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)


difference = date2 - date1

print(f"{difference.days} days")

# Write a Python program that accepts an integer (n) and 
# computes the value of n+nn+nnn
# Accept input from the user
n = input("Enter an integer: ")

# Compute n + nn + nnn
value = int(n) + int(n*2) + int(n*3)

print("Result:", value)

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an EVEN number.")
else:
    print(f"{num} is an ODD number.")

# Write a Python program which accepts a sequence of 
# comma-separated numbers from user and generate a list 
# and a tuple with those numbers. 
# Accept comma-separated numbers from the user
values = input("Enter comma-separated numbers: ")

# Generate list and tuple
list_values = values.split(",")
tuple_values = tuple(list_values)

print("List:", list_values)
print("Tuple:", tuple_values)

# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def calculate_sum(a, b, c):
    total = a + b + c
    
    if a == b == c:
        return 3 * total
    else:
        return total

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = calculate_sum(a, b, c)
print("Result:", result)

# Write a Python program to test whether a passed letter is a 
# vowel or not 
# Ask the user for a letter
letter = input("Enter a letter: ").lower()

# Check if it's a vowel
if letter in ('a', 'e', 'i', 'o', 'u'):
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")

# Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5. Extras: a) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. b) Write this in one line of Python. c) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
# Original list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Elements less than 5:")
for i in a:
    if i < 5:
        print(i)

# (a) Create a new list of elements < 5
new_list = [i for i in a if i < 5]
print("\n(a) New list with elements less than 5:")
print(new_list)

# (b) One-line Python solution
print("\n(b) One-line solution:")
print([i for i in a if i < 5])

# (c) Ask user for a number and filter
num = int(input("\n(c) Enter a number: "))
result = [i for i in a if i < num]
print("Numbers less than", num, "are:", result)

# Create a program that asks the user for a number and then 
# prints out a list of all the divisors of that number. (If you 
# don’t know what a divisor is, it is a number that divides 
# evenly into another number. For example, 13 is a divisor of 
# 26 because 26 / 13 has no remainder.) 
# Ask the user for a number
num = int(input("Enter a number: "))

divisors = []

# Check all numbers from 1 to num
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

print("Divisors of", num, "are:", divisors)

# Take two lists, say for example these two: 
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
# and write a program that returns a list that contains only the 
# elements that are common between the lists (without 
# duplicates). Make sure your program works on two lists of 
# different sizes.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Find common elements without duplicates
common = []

for i in a:
    if i in b and i not in common:
        common.append(i)

print("Common elements:", common)

# Ask the user for a string and print out whether this string is 
# a palindrome or not. (A palindrome is a string that reads the 
# same forwards and backwards.) 
# Ask the user for a string
text = input("Enter a string: ")

# Check if palindrome
if text == text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 
# 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that 
# takes this list a and makes a new list that has only the even 
# elements of this list in it.  
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = [x for x in a if x % 2 == 0]
print(new_list)

# Generate a random number between 1 and 9 (including 1 
# and 9). Ask the user to guess the number, then tell them 
# whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very 
# first exercise) 
import random

# Generate a random number between 1 and 9
number = random.randint(1, 9)

# Ask the user to guess
guess = int(input("Guess a number between 1 and 9: "))

# Check the guess
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Exactly right!")

# Ask the user for a number and determine whether the 
# number is prime or not. (For those who have forgotten, a 
# prime number is a number that has no divisors.). 
# Ask the user for a number
num = int(input("Enter a number: "))

# Handle numbers less than 2
if num < 2:
    print(f"{num} is not a prime number.")
else:
    # Check for divisors from 2 to sqrt(num)
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# Write a program (function!) that takes a list and returns a 
# new list that contains all the elements of the first list minus 
# all the duplicates. 
def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

# Example
sample_list = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", sample_list)
print("List without duplicates:", remove_duplicates(sample_list))

# Write a function that takes an ordered list of numbers (a list 
# where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not 
# the given number is inside the list and returns (then prints) 
# an appropriate boolean. 
def number_in_list(sorted_list, num):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == num:
            return True
        elif sorted_list[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return False


# Example usage
lst = [1, 3, 5, 7, 9, 11]
number = 7

result = number_in_list(lst, number)
print(result)   # prints: True

# Implement a function that takes as input three variables, and 
# returns the largest of the three. Do this without using the 
# Python max() function! 
def largest_of_three(a, b, c):
    largest = a   # assume a is the largest initially

    if b > largest:
        largest = b
    if c > largest:
        largest = c

    return largest


# Example usage
x, y, z = 12, 25, 9
print("Largest number is:", largest_of_three(x, y, z))
