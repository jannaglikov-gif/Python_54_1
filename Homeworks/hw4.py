import json
import csv
import pathlib

print("___________Task 1__________\n")
# 1. Save a book list
# Напишите функцию save_books(books).
# Функция принимает список строк и создаёт файл books.txt, в который сохраняет названия книг. Каждая книга должна быть записана с новой строки.
# Пример:
# books = [
# "Harry Potter",
# "The Hobbit",
# "1984",
# "The Little Prince"
# ]
#
# save_books(books)
# После выполнения программы файл books.txt должен выглядеть так:
# Harry Potter
# The Hobbit
# 1984
# The Little Prince
# Используйте:
# ·       with open(...)
# ·       режим "w"
# ·       цикл for

#------------------------------------------------------------------
books = ["Harry Potter", "The Hobbit", "1984", "The Little Prince"]
def save_books(books):
    with open("books.txt", "w", encoding = "utf-8") as file:
        for line in books:
            file.write(f"{line}\n")
            print(line)
save_books(books)
#------------------------------------------------------------------

print()
print("___________Task 2__________\n" )
# 2. Read data from a CSV file
# Создайте файл products.csv со следующим содержимым:
# product,price
# Coffee,25
# Tea,18
# Chocolate,12
# Напишите функцию: read_products(filename)
# Функция должна прочитать данные из файла и вывести информацию в следующем формате:
# Product: Coffee (25)
# Product: Tea (18)
# Product: Chocolate (12)
# Используйте:
# csv.DictReader()

#------------------------------------------------------------------
with open("products.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["product", "price"])
    writer.writerow(["Coffee", "25"])
    writer.writerow(["Tea", "18"])
    writer.writerow(["Chocolate", "12"])

def read_products(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")
read_products("products.csv")
#------------------------------------------------------------------

print()
print("___________Task 3__________\n" )
# 3. Save user information to a JSON file
# Напишите функцию: save_user(username, email, country)
# Функция должна создать файл user.json и сохранить в него информацию о пользователе.
# Пример вызова:
# save_user("anna21", "anna@example.com", "Israel")
# Ожидаемое содержимое файла user.json:
# {
#  	"username": "anna21",
#  	"email": "anna@example.com",
#  	"country": "Israel"
#  }
# Используйте:
# ·       словарь dict
# ·       json.dump()

#------------------------------------------------------------------
def save_user(username, email, country):
    user = {"username": username, "email": email, "country": country}
    with open("user.json", "w", encoding="utf-8") as file:
        json.dump(user, file, indent = 4)
        print(json.dumps(user, indent =4))
save_user("anna21", "anna@example.com", "Israel")
#------------------------------------------------------------------

print()
print("___________★ Advanced ★__________\n" )
# 4. Advanced ★
# Напишите функцию: create_logs_folder()
# Функция должна:
# 1.     Создать папку logs.
# 2.     Создать внутри неё файл app.txt.
# 3.     Записать в файл строку:
# Application started successfully!
# Используйте:
# ·       pathlib.Path
# ·       mkdir()
# ·       with open(...)
# General Requirements
# ·       Используйте encoding='utf-8' при работе с текстовыми файлами.
# ·       Проверьте работу каждой функции на примерах из задания.
# ·       Используйте названия функций, указанные в задании.
# ·       Код должен быть читаемым и аккуратно оформленным.
# ·       После выполнения программы проверьте содержимое созданных файлов.

#------------------------------------------------------------------
def create_logs_folder():
    folder = pathlib.Path("logs")
    folder.mkdir(exist_ok = True)
    file_path = folder / "app.txt"

    with open(file_path, "w", encoding = "utf-8") as file:
        file.write("Application started successfully!")

    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())

create_logs_folder()
# ------------------------------------------------------------------
print()
print("___________★★ Advanced ★★__________\n" )
# create_test_report(project_name, tester_name, passed, failed)
# 1.⁠ ⁠Создать папку reports.
# 2.⁠ ⁠Внутри папки reports создать папку с названием проекта, которое передано в project_name.
# 3.⁠ ⁠Внутри папки проекта создать файл report.txt.
# 4.⁠ ⁠Записать в файл следующую информаци
# Project: Phonebook
# Tester: Anna
# Passed tests: 18
# Failed tests: 2
# Total tests: 20
# Значение Total tests функция должна посчитать самостоятельно:
# passed + failed
# create_test_report("Phonebook", "Anna", 18, 2)
# reports/
#    Phonebook/
#        report.txt
# Project: Phonebook
# Tester: Anna
# Passed tests: 18
# Failed tests: 2
# Total tests: 20
# from pathlib import Path
# Path
# mkdir()
# with open(...)
# "w"
# encoding="utf-8"
# file.write()
#------------------------------------------------------------------
def create_test_report(project_name, tester_name, passed, failed):
    project_folder = pathlib.Path("reports") / project_name
    project_folder.mkdir(exist_ok=True, parents=True)
    total = passed + failed

    file_path = project_folder/"report.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Project: {project_name}\n")
        file.write(f"Tester: {tester_name}\n")
        file.write(f"Passed tests: {passed}\n")
        file.write(f"Failed tests: {failed}\n")
        file.write(f"Total tests: {total}\n")

    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())

create_test_report("Phonebook", "Anna", 18, 2)
#------------------------------------------------------------------
