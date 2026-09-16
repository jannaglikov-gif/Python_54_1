from fileinput import filename

print("___________Task 1__________\n" )
#Task 1. Clean a Name
#        Write a function clean_name(name).
#        Remove spaces from the beginning and end of the string.
#        Return the name in title case.

name = " yume nox "
clean_name = name.strip().title()
print(clean_name)

name = "AROREE FOX"
clean_name = name.title()
print(clean_name)

print("___________Task 2__________\n" )

#Task 2. Normalize an Email
#        Write a function normalize_email(email).
#        Remove spaces from the beginning and end.
#        Convert all letters to lowercase.
#        Return the cleaned email.

email = " YumeNox@Gmail.COM "
normalize_email = email.strip().lower()
print(normalize_email)

print("___________Task 3__________\n" )

#Task 3. Check a File Name
#        Write a function is_python_file(filename).
#        Return True if the file name ends with .py.
#        The check must work for .py, .PY, .Py, etc.

def is_python_file(filename):
    return filename.lower().endswith(".py")

print(is_python_file("test.txt"))
print(is_python_file("hw.Py"))
print(is_python_file("homework.PY"))
print(is_python_file("sun.jpg"))

print("___________Task 4__________\n" )

#Task 4. Replace Words
#        Write a function fix_message(message).
#        Replace every occurrence of the word "bad" with "good".
#        Return the new string.
#        Remember: strings are immutable, so the original string itself is not changed.

def fix_message(message):
    return message
message = fix_message("This is sunny day")
print(message.replace("sunny", "rainy"))
message = message.replace("rainy", "sunny")
print(message)

print("___________Task 5__________\n" )

#Task 5. Count a Letter
#        Write a function count_letter(text, letter).
#        Count how many times letter appears in text.
#        The check must be case-insensitive.

def count_letter(text, letter):
    return text.strip().lower().count(letter.strip().lower())

print(count_letter("Programming", "R"))
print(count_letter("Mississippi", "S"))

print("___________Task 6__________\n" )

#Task 6. Create a Short Login
#        Write a function create_login(first_name, last_name).
#        Remove unnecessary spaces from both names.
#        Convert both names to lowercase.
#        Create a login in the format: first_name.last_name Return the result.

def create_login(first_name, last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    return first_name + "." + last_name

print(create_login("  Yume ", " noX  "))

print("___________Bonus 1__________\n" )

#Bonus 1. Split Full Name
#         Write a function split_name(full_name).
#         Assume the string contains exactly a first name and a last name separated by spaces.

def split_name(full_name):
    return full_name.strip().split()

print(split_name("  Aroree   Fox  "))

print("___________Bonus 2__________\n" )

#Bonus 2. Simple Password Check
#         Write a function check_password(password).
#         Return True only if all conditions are met:
#         the password has at least 8 characters;
#         it contains no spaces;
#         it is not made only of letters;

def check_password(password):
#1.Checking that the password contains at least 8 characters.
    if len(password) <= 8:
        return False
#2.Checking that the password contains no spaces.
    for char in password:
        if char.isspace():
            return False
#3.Checking that the password consists not only of letters.
    if password.isalpha():
        return False
    return True
print(check_password("qwerty123"))
print(check_password("qwerty"))
print(check_password("qwerty 123"))