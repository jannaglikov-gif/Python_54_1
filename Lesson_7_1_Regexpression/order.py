import re

def is_valid_id(order_id):
    return bool(re.search("^ORD-...$",order_id))
print(is_valid_id("ORD-123"))
print(is_valid_id("ORD-12"))
print(is_valid_id("OOO-123"))

print(re.search("gr[ae]y","grey"))
print(re.search("gr[ae]y","groy"))
print(re.search("gr[ae]y","green"))

print(re.search("[a-z]","Kristina"))
print(re.search("[0-9]","Order #34"))
print(re.search("[A-Z]","kristina"))
print(re.search("[A-Za-z]","kristina"))

print(re.search("[^0-9]","123456a"))
print(re.search("[^0-9]","123456"))
#
# \s подменяет любой пробельный символ.
# К пробельным символам относятся:
# Обычный пробел ( )
# Знак табуляции (\t)
# Перевод строки (\n)
# Возврат каретки (\r)
# Вертикальная табуляция и другие подобные символы.

print(re.search(r'\d',"Order #34"))
print(re.search(r'\w',"!!!Kristina"))
print(re.search(r"\s","Kristina QA 54"))

def has_digits(password):
    return bool(re.search(r"\d",password))

print(has_digits("dr123456"))
print(has_digits("qwerty"))

print(re.search(r"ab+c","ac"))
print(re.search(r"ab+c","abc"))
print(re.search(r"ab+c","abc"))