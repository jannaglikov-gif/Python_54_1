import json
import csv
import pathlib

print("___________Практика Python • Файлы, CSV, JSON, pathlib 1__________\n")
# Python: 5 задач для практики
# Закрепляем работу с текстовыми файлами, CSV, JSON и папками.
# Без готовых решений.
# Во всех задачах используй encoding="utf-8".
# После запуска проверяй содержимое созданных файлов.


print("___________Task 1: Сохраняем покупки__________\n")
# Напиши функцию save_shopping_list(items), которая принимает список строк и сохраняет их
# в shopping.txt: каждый товар с новой строки.
# Пример вызова:
# save_shopping_list(["Хлеб", "Молоко", "Яблоки"])
# Ожидаемое содержимое файла:
#   Хлеб
#   Молоко
#   Яблоки
# Используй with open(...), режим "w", цикл for и write().

#------------------------------------------------------------------
items = ["Хлеб","Молоко","Яблоки"]
def save_shopping_list(items):
    with open("shopping.txt", "w", encoding = "utf-8") as file:
        for item in items:
            file.write(f"{item}\n")
            print(item)
save_shopping_list(items)
#------------------------------------------------------------------

print()
print("___________Task 2: Читаем покупки__________\n")
# Напиши функцию show_shopping_list(filename), которая читает файл из первой задачи и
# выводит его содержимое в консоль.
# Пример вызова:
# show_shopping_list("shopping.txt")
# Используй параметр filename, режим "r" и read().

#------------------------------------------------------------------
def show_shopping_list(filename):
    with open(filename, "r", encoding = "utf-8") as file:
        print(file.read())
show_shopping_list("shopping.txt")
#------------------------------------------------------------------

print()
print("___________Task 3: Читаем CSV со студентами__________\n")
# Создай файл students.csv со следующим содержимым:
# name,grade
# Anna,90
# Dima,85
# Maria,95
# Напиши функцию show_students(filename), которая выводит:
# Student: Anna — grade: 90
# Student: Dima — grade: 85
# Student: Maria — grade: 95
# Используй csv.DictReader(), цикл и f-строку.
# Файл можешь подготовить вручную или через csv.writer().

#------------------------------------------------------------------
with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "grade"])
    writer.writerow(["Anna", "90"])
    writer.writerow(["Dima", "85"])
    writer.writerow(["Maria", "95"])

def show_students(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student: {row['name']} - grade: {row['grade']}")
show_students("students.csv")
#------------------------------------------------------------------

print()
print("___________Task 4: Сохраняем сведения о книге__________\n")
# Напиши функцию save_book(title, author, year).
# Она должна собрать данные в словарь и сохранить его в book.json.
# Пример вызова:
# save_book("The Hobbit", "J. R. R. Tolkien", 1937)
# Ожидаемое содержимое файла:
# {
# "title": "The Hobbit",
# "author": "J. R. R. Tolkien",
# "year": 1937
# }
# Используй json.dump() и indent=4.
# Значения должны браться из параметров функции.

#------------------------------------------------------------------
def save_book(title, author, year):
    book = {"title": title, "author": author, "year": year}
    with open("book.json", "w", encoding="utf-8") as file:
        json.dump(book, file, indent = 4)
        print(json.dumps(book, indent =4))
save_book("The Hobbit", "J. R. R. Tolkien", 1937)
#------------------------------------------------------------------

print()
print("___________Task 5: Создаём папку и читаем файл из неё__________\n")
# Напиши функцию create_notes_folder(), которая:
# 1. Создаёт папку notes.
# 2. Создаёт внутри неё файл message.txt.
# 3. Записывает текст Today I practiced Python!
# 4. Закрывает файл после записи.
# 5. Снова открывает его для чтения и выводит прочитанное в консоль.
# Используй pathlib.Path, mkdir(exist_ok=True) и два блока with open(...).
# Проверь, что повторный вызов работает без ошибки.
# Как проверить свою работу
# • Вызови каждую функцию: одного определения через def недостаточно.
# • Проверь, что файлы созданы с указанными именами.
# • Сравни содержимое и вывод с примерами.
# • Для пятой задачи убедись, что message.txt находится внутри notes.

#------------------------------------------------------------------
def create_notes_folder():
    folder = pathlib.Path("notes")
    folder.mkdir(exist_ok = True)
    file_path = folder / "message.txt"

    with open(file_path, "w", encoding = "utf-8") as file:
        file.write("Today I practiced Python!")

    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())

create_notes_folder()
# ------------------------------------------------------------------
print()
# Решай по одной задаче. Если возникнет ошибка, сохрани её текст и попробуй объяснить, на
# каком шаге она появилась