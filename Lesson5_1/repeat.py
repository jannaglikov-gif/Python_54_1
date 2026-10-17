import json
import csv
import pathlib

print("___________LIST__________\n" )
# Напишите функцию save_shopping_list(items).
# Функция принимает список строк и создаёт файл shopping.txt и сохраняет в него список покупок.
# Каждый товар должен быть записан с новой строки.
# Пример:
# items = [
# "Milk",
# "Bread",
# "Apples",
# "Coffee"
# ]
# save_shopping_list(items) После выполнения программы файл должен выглядеть так:
# Milk
# Bread
# Apples
# Coffee
# Используйте:
# • with open(...)
# • режим "w"
# • цикл for

#------------------------------------------------------------------
items = ["Milk","Bread","Apples","Coffee"]
def save_shopping_list(items):
    with open("shopping.txt", "w", encoding = "utf-8") as file:
        for item in items:
            file.write(f"{item}\n")
            print(item)
save_shopping_list(items)
#------------------------------------------------------------------

print()
print("___________CSV__________\n" )

# Read data from a CSV file
# Создайте файл students.csv со следующим содержимым:
# name,age
# Anna,21
# Tom,19
# Kate,22
# Напишите функцию read_students(filename)
# которая выводит информацию в виде
# Student: Anna (21)
# Student: Tom (19)
# Student: Kate (22)
# Use csv.DictReader().

#------------------------------------------------------------------
with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["Anna", "21"])
    writer.writerow(["Tom", "19"])
    writer.writerow(["Kate", "22"])

def read_students(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student: {row['name']} ({row['age']})")
read_students("students.csv")
#------------------------------------------------------------------

print()
print("___________JSON__________\n" )

# Save a profile to a JSON file
#
# Напишите функцию save_profile(name, age, city)
# Функция должна создать файл profile.json со следующим содержимым:
# save_profile("Maria", 30, "Haifa")
# Ожидаемое содержимое файла profile.json:
# {
#     "name": "Maria",
#     "age": 30,
#     "city": "Haifa"
# }
# Use a dictionary and json.dump().

#------------------------------------------------------------------
def save_profile(name, age, city):
    person = {"name": name, "age": age, "city": city}
    with open("profile.json", "w", encoding="utf-8") as file:
        json.dump(person, file, indent = 4)
        print(json.dumps(person, indent =4))
save_profile("Maria", 30, "Haifa")
print()
#------------------------------------------------------------------
test_config = {
    "url": "http://127.0.0.1:8000",
    "username": "kristina",
    "password": "Aa123456!",
    "timeout": 20
}
with open("config.json","w",encoding="utf-8") as file:
    json.dump(test_config,file,indent=4,ensure_ascii=False)
    print(json.dumps(test_config, indent=4))
    print()
with open("config.json","r",encoding="utf-8") as file:
    config = json.load(file)
    print(config)
    print()
    print(config["url"])
#------------------------------------------------------------------

print()
print("___________★ PATHLIB ★__________\n" )
# Напишите функцию create_reports_folder()
# Функция должна: Создать папку reports.
# Создать внутри неё файл result.txt.
# Записать в файл строку: Homework completed successfully!
# Use pathlib.Path, mkdir() and with open(...).
# General requirements
# • Use encoding = 'utf-8' when working with text files.
# • Test every function using the examples from the task.

#------------------------------------------------------------------
def create_reports_folder():
    folder_n = pathlib.Path("reports")
    folder_n.mkdir(exist_ok=True)
    file_path = folder_n/"report.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Homework completed successfully!")

    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())
        print()

create_reports_folder()
#------------------------------------------------------------------

folder = pathlib.Path("data_test")
file_path = folder/"test.csv"
print(file_path)
print()
print(file_path.exists())

screen_folder = pathlib.Path("screen")
screen_folder.mkdir(exist_ok=True)
report_folder = pathlib.Path("reports")/("october")
report_folder.mkdir(exist_ok=True, parents=True)



