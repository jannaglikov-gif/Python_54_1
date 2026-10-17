import json


# print("Hello World")
# result = 10/0
# print(result)
# print("Buy World")

# with open("user.json","w",encoding="utf-8") as file:
#     print(file.read())
#
# def div_int(a,b):
#     return a/b
# print("Start program")
# result = div_int(10,0)
# print(result)
# print("End program")

print("Hello World")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("An error occured: Zero division")
# print("Bye")

try:
    number = int(input("Enter a number!"))
    result = 100/ number
    print("Result: ", result)
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")