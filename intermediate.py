# python program to perform read and write operations on a 
# file.  
# Writing to a file
def write_to_file():
    with open("sample.txt", "w") as file:
        file.write("Hello, this is a sample file.\n")
        file.write("We are performing read and write operations.\n")
    print("Data written to file successfully.")

# Reading from a file
def read_from_file():
    with open("sample.txt", "r") as file:
        content = file.read()
    print("\nContent of the file:")
    print(content)

# Main program
write_to_file()
read_from_file()


# python program to copy the contents of a file to another file.
def copy_file(source, destination):
    try:
        with open(source, "r") as src:
            data = src.read()

        with open(destination, "w") as dest:
            dest.write(data)

        print("File copied successfully!")

    except FileNotFoundError:
        print("Source file not found!")

# Example usage
copy_file("source.txt", "destination.txt")

# Python program to count frequency of characters in a given 
# file.
def count_char_frequency(filename):
    freq = {}

    try:
        with open(filename, "r") as file:
            content = file.read()

            for char in content:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1

        # Display character frequencies
        for char, count in freq.items():
            if char == "\n":
                print("\\n :", count)
            elif char == " ":
                print("space :", count)
            else:
                print(f"{char} : {count}")

    except FileNotFoundError:
        print("File not found!")


# Example usage
count_char_frequency("sample.txt")

# Python program to print each line of a file in reverse order.
def reverse_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        print("Reversed lines:\n")
        for line in lines:
            print(line.strip()[::-1])

    except FileNotFoundError:
        print("File not found!")


# Example usage
reverse_lines("sample.txt")

# Python program to compute the number of characters, words 
# and lines in a file.  
def count_file_stats(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        num_lines = len(lines)
        num_words = 0
        num_chars = 0

        for line in lines:
            num_chars += len(line)
            num_words += len(line.split())

        print("Total Lines     :", num_lines)
        print("Total Words     :", num_words)
        print("Total Characters:", num_chars)

    except FileNotFoundError:
        print("File not found!")


# Example usage
count_file_stats("sample.txt")

# Write a program that prompts the user to enter his name. 
# The program then greets the person with his name. But if the 
# person’s name is ‘Rahul’ and exception is thrown and he is 
# asked to quit the program. 
class NameNotAllowedError(Exception):
    pass

try:
    name = input("Enter your name: ")

    if name == "Rahul":
        raise NameNotAllowedError("Access denied! Please quit the program.")

    print("Hello,", name + "! Welcome to the program.")

except NameNotAllowedError as e:
    print(e)

# Write a program that accepts date of birth along with the 
# other personal details of a person. Throw an exception if an 
# invalid date is entered. 
from datetime import datetime

try:
    name = input("Enter your name: ")
    dob = input("Enter your Date of Birth (DD-MM-YYYY): ")   # user input as string

    # Validate date format
    try:
        valid_dob = datetime.strptime(dob, "%d-%m-%Y")
    except ValueError:
        raise Exception("Invalid Date! Please enter a valid date in DD-MM-YYYY format.")

    age = datetime.now().year - valid_dob.year
    print("\nPersonal Details:")
    print("Name:", name)
    print("Date of Birth:", valid_dob.strftime("%d-%m-%Y"))
    print("Age:", age)

except Exception as e:
    print(e)

# Write a Regular Expression to represent all 10 digit mobile 
# numbers. Rules: 1. Every number should contains exactly 10 
# digits. 2. The first digit should be 7 or 8 or 9 Write a Python 
# Program to check whether the given number is valid mobile 
# number or not? 
import re

def is_valid_mobile(number):
    pattern = r'^[789][0-9]{9}$'
    
    if re.match(pattern, number):
        return True
    else:
        return False


# Example usage
mobile = input("Enter a 10-digit mobile number: ")

if is_valid_mobile(mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# A spell checker can be a helpful tool for people who struggle 
# to spell words correctly. In this exercise, you will write a 
# program that reads a file and displays all of the words in it 
# that are misspelled. Misspelled words will be identified by 
# checking each word in the file against a list of known words. 
# Any words in the user’s file that do not appear in the list of 
# known words will be reported as spelling mistakes. The user 
# will provide the name of the file to check for spelling mistakes 
# as a command line parameter. Your program should display 
# an appropriate error message if the command line parameter 
# is missing. An error message should also be displayed if your 
# program is unable to open the user’s file. Words followed by 
# a comma, period or other punctuation mark are not reported 
# as spelling mistakes. Ignore the capitalization of the words 
# when checking their spelling. 
import sys
import string

def main():
    # Known correct words (you can expand this list)
    known_words = {
        "this", "is", "a", "sample", "text", "hello", "world",
        "python", "program", "file", "check", "spelling",
        "mistakes", "the", "and", "of", "to", "in", "it"
    }

    # 1. Check if filename is provided
    if len(sys.argv) < 2:
        print("Error: No filename provided in command line.")
        print("Usage: python spell_checker.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: Unable to open file '{filename}'.")
        return

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = content.translate(translator)

    # Split into words
    words = cleaned_text.split()

    print("\nMisspelled Words:")
    mistakes_found = False

    for word in words:
        word_lower = word.lower()

        if word_lower not in known_words:
            print(word)
            mistakes_found = True

    if not mistakes_found:
        print("No spelling mistakes found!")

if __name__ == "__main__":
    main()
