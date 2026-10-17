def calculator(a:float,b:float,operator:str):
    if operator == "+":
        return a+b
    if operator == "/":
        return a/b
    if operator == "*":
        return a*b
    if operator == "-":
        return a-b

def pars(a_str:str,b_str:str,operator:str):
    a = float(a_str)
    b = float(b_str)
    return calculator(a,b,operator)

def run():
    try:
        a = input("Enter first number:")
        b = input("Enter second number:")
        operator = input("Enter action operator: [+] [-] [*] [/]")
        result = pars(a,b, operator)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
run()

def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False
print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Dem"))
print(is_number(None))
print()

try:
    value = int("%%%%%")
except ValueError:
    print("An error occurred: ")
else:
    print("An error eccurred: ", value)
finally:
    print("End of try")







