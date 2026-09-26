from Lesson2_Refresh.list import result

print("___________Task 1__________\n" )
# 1. Написать функцию print_list_reverse(lst)
# Функция принимает список и выводит этот список в консоль в обратном порядке.
# Если lst равен None, пустой список, или если аргумент не является объектом типа list, функция должна вывести: Wrong list
# Пример: print_list_reverse([1, 2, 3, 4, 5])
# Вывод в консоль: [5, 4, 3, 2, 1]
def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong list")
        return
    print(lst[::-1])
print_list_reverse([1, 2, 3, 4, 5])
print()

print("___________Task 2__________\n" )
# 2. Написать функцию is_valid_point(point)
# Функция принимает кортеж и проверяет, является ли он корректной точкой на плоскости.
# Условия корректной точки:
# • аргумент должен быть кортежем (tuple), а не списком или другим типом;
# • кортеж состоит ровно из 2 элементов;
# • оба элемента являются числами (int или float).
# Если кортеж соответствует всем условиям, функция возвращает True.
# Если аргумент не соответствует условиям, функция возвращает False.
# Если point равен None или является пустым кортежем, функция возвращает None.
# Примеры:
# is_valid_point((3, 5))      # True
# is_valid_point((3, "5"))    # False
# is_valid_point([3, 5])      # False
# is_valid_point((1, 2, 3))   # False
# is_valid_point(())          # None
# is_valid_point(None)        # None
def is_valid_point(point):
    if point is None or len(point) == 0:
        return None
    if (not isinstance(point, tuple)
            or len(point) != 2
            or not all(isinstance(i, (int, float)) for i in point)):
        return False
    return True
print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))

print()

print("___________Task 3__________\n" )
# 3. Написать функцию print_sublist_reverse(lst, start, finish)
# Функция принимает список, стартовый индекс и финишный индекс.
# Нужно вывести в консоль список, в котором элементы от индекса start до индекса finish включительно расположены
# в обратном порядке, а остальные элементы остаются в обычном порядке.
# Пример: print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
# Исходный список: [10, 20, 30, 40, 50, 60] Часть списка от индекса 1 до индекса 3 включительно: [20, 30, 40]
# После реверса: [40, 30, 20]
# Вывод в консоль: [10, 40, 30, 20, 50, 60]
# Если lst равен None, пустой список, не является списком,
# если start / finish не являются целыми числами,
# если индексы start / finish выходят за пределы списка, или start > finish, функция должна вывести: Wrong args
# Пример:print_sublist_reverse([1, 2, 3], "0", 2)  # Wrong args (start не является целым числом)
def print_sublist_reverse(lst1, start, finish):
    if (lst1 is None
            or not isinstance(lst1, list)
            or len(lst1) == 0
            or not all(isinstance((i), int) for i in (start, finish))
            or not 0 <= start <= finish < len(lst1)):
        print("Wrong args")
        return
    lst1[start:finish + 1] = lst1[start:finish + 1][::-1]
    print(lst1)
print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print()

print("___________Task 4__________\n" )
# 4. Advanced — Написать функцию get_students_by_grade(students)
# Функция принимает словарь, где ключ — имя студента, а значение — его оценка.
# Нужно вернуть новый словарь, где ключ — оценка, а значение — список имён студентов, получивших эту оценку.
# Пример: get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85})
# Результат: {90: ["Alice", "Diana"], 85: ["Bob", "Charlie"]}
# Если students равен None, является пустым словарём или аргумент не является словарём, функция должна вернуть пустой словарь: {}
def get_students_by_grade(students):
    if not students or not isinstance(students, dict):
        return {}
    res = {}
    for name, grade in students.items():
        if grade in res:
            res[grade].append(name)
        else:
            res[grade] = [name]
    return res
result1 = get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85})
print(result1)