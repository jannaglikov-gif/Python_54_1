# MANDATORY
from Lesson2_Refresh.list import new_list

print("___________Task 1__________\n" )
# Task 1. Shopping cart Write a function clean_cart(cart).
# The list contains product names. Remove all occurrences of the string "sold out" and return the updated list.
# print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
# ["milk", "bread", "coffee"]
# Hint: Be careful when removing elements while iterating through a list.

def clean_cart(cart):
    while "sold out" in cart:
        cart.remove("sold out")
    return cart
print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
print()

print("___________Task 2__________\n" )
# Task 2. Temperature report Write a function temperature_report(temperatures).
# Return a NEW list containing only temperatures greater than 25.
# print(temperature_report([21, 28, 19, 31, 25, 27]))
# [28, 31, 27]
# Hint: Create an empty result list and add suitable values with append().

def temperature_report(temperatures):
    res = []
    for temp in temperatures:
        if temp > 25:
            res.append(temp)
    return res
print(temperature_report([21, 28, 19, 31, 25, 27]))
print()

print("___________Task 3__________\n" )
# Task 3. Fix negative balances Write a function fix_balances(balances).
# Replace every negative value in the SAME list with 0.
# Return the list.
# print(fix_balances([120, -30, 50, -5, 0, 200]))
# [120, 0, 50, 0, 0, 200]
# Hint: Here you need indexes because you are changing list elements.

def fix_balances(balances):
    for i in range(len(balances)):
        if balances[i] < 0:
            balances[i] = 0
    return balances
print(fix_balances([120, -30, 50, -5, 0, 200]))
print()

print("___________Task 4__________\n" )
# Task 4. Remove duplicates without set Write a function unique_items(items).
# Return a new list containing each value only once, preserving the original order.
# Do not use set().
# print(unique_items(["red", "blue", "red", "green", "blue"]))
# ["red", "blue", "green"]
# Hint: Before append(), check whether the value is already in the result list.

def unique_items(items):
    new = []
    for u in items:
        if u not in new:
            new.append(u)
    return new
print(unique_items(["red", "blue", "red", "green", "blue"]))
print()

# ADVANCED
print("___________Task 5__________\n" )
# Task 5. Longest word Write a function longest_word(words).
# Find and return the longest word in the list.
# If several words have the same maximum length, return the first one.
# Do not use max().
# print(longest_word(["cat", "elephant", "python", "coffee"]))
# "elephant" Hint:
# Keep the best word found so far and compare len().

def longest_word(words):
    l = ""
    for w in words:
        if len(w) > len(l):
            l = w
    return l
print(longest_word(["cat", "elephant", "python", "coffee"]))