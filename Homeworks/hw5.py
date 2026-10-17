import csv
import json
import pathlib


print("___________Task 1__________\n")
# 1.Напишите три функции
# 1.1 save_test_ids(test_ids) — принимает список ID тестов и сохраняет их в tests.txt.
#     Каждый ID должен находиться на отдельной строке.
# 1.2 add_test_id(test_id) — добавляет один новый ID в конец существующего файла, не удаляя предыдущие записи.
# 1.3 load_test_ids(filename) — читает файл и возвращает список ID.
#      Пустые строки нужно пропускать, пробелы по краям удалять.
# Пример исходного списка->["QA-1001", "QA-1002", "QA-1003"]
# После вызова add_test_id("QA-1004") функция load_test_ids("tests.txt") должна вернуть:
# ["QA-1001", "QA-1002", "QA-1003", "QA-1004"]
# Используйте: def, return, for, list, append(), with open(), режимы w, a, r, strip().
# Проверьте пустой список, повторное добавление записи и чтение файла с пустыми строками.

#------------------------------------------------------------------
def save_test_ids(test_ids):
    with open("tests.txt","w",encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(f"{test_id}\n")

save_test_ids(["QA-1001", "QA-1002", "QA-1003"])

def add_test_id(test_id):
    with open("tests.txt","a",encoding="utf-8") as file:
        file.write(f"{test_id}\n")

add_test_id("QA-1004")

def load_test_ids(filename):
    test_ids = []

    with open(filename,"r",encoding="utf-8") as file:
        for line in file:
            test_id = line.strip()
            if test_id != "":
                test_ids.append(test_id)
    return test_ids

print(load_test_ids("tests.txt"))

save_test_ids([])
print(load_test_ids("tests.txt"))

add_test_id("QA-1004")
add_test_id("QA-1004")
print(load_test_ids("tests.txt"))

with open("tests.txt", "w", encoding="utf-8") as file:
    file.write("  QA-1001  \n\n   \n  QA-1002  \n")

print(load_test_ids("tests.txt"))
# ------------------------------------------------------------------
print()
print("___________Task 2__________\n")
# 2.Создайте файл results.csv
# test_id,status,duration_ms
# QA-1001,PASSED,120
# QA-1002,FAILED,230
# QA-1003,PASSED,150
# Напишите функцию get_test_statistics(filename)
#
# Функция должна:
# 1.Прочитать данные из CSV.
# 2.Посчитать общее количество тестов.
# 3.Посчитать количество PASSED и FAILED.
# 4.Найти суммарное время выполнения тестов в миллисекундах.
# 5.Собрать в список ID всех проваленных тестов.
# 6.Вернуть словарь с результатом
#   Ожидаемый резальт->
# {
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500,
#     "failed_ids": ["QA-1002"]
# }
# Используйте: csv.DictReader(), for, if, dict, list, int(), append(), return.
# Считайте, что в корректном входном файле статусы могут быть только PASSED и FAILED, а время — целое неотрицательное число.
# Дополнительно проверьте файл, содержащий только заголовки. Все счётчики должны быть равны нулю, список ошибок — пустой.

#------------------------------------------------------------------
def get_test_statistics(filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])

            if row ["status"] == "PASSED":
                passed += 1

            if row ["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms,
        "failed_ids": failed_ids
    }

with open("results.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id", "status", "duration_ms"])
    writer.writerow(["QA-1001", "PASSED", 120])
    writer.writerow(["QA-1002", "FAILED", 230])
    writer.writerow(["QA-1003", "PASSED", 150])

statistics = get_test_statistics("results.csv")

for key, value in statistics.items():
    print(f"{key}: {value}")

with open("headers_only.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id", "status", "duration_ms"])

assert get_test_statistics("headers_only.csv") == {
    "total": 0,
    "passed": 0,
    "failed": 0,
    "total_duration_ms": 0,
    "failed_ids": []
}

print("Проверка файла только с заголовками пройдена!")
# ------------------------------------------------------------------
print()
print("___________Task 3__________\n")
# 3. Напишите две функции:
# •save_test_config(environment, base_url, timeout) — создаёт config.json и сохраняет параметры тестового окружения.
# •load_test_config(filename) — читает JSON и возвращает словарь с настройками.
# Пример вызова
# save_test_config(
#     "staging",
#     "https://example.com",
#     30
# )
# Ожидаемый JSON {
#     "environment": "staging",
#     "base_url": "https://example.com",
#     "timeout": 30
# }
# —-----------
# 1.Для сохранения используйте json.dump().
# 2.Для чтения используйте json.load().
# 3.Сохраняйте данные с отступами для удобного чтения.
# 4.Проверьте, что после загрузки тип timeout остаётся int.
# 5.Проверьте, что повторное сохранение заменяет старую конфигурацию.
#   Используйте: dict, json.dump(), json.load(), with open(), type(), assert.

#------------------------------------------------------------------
def save_test_config(environment, base_url, timeout):
    config = {"environment": environment,"base_url": base_url,"timeout": timeout}

    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4, ensure_ascii=False)

def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        config = json.load(file)
    return config

save_test_config("staging", "https://example.com", 30)
settings = load_test_config("config.json")
print(json.dumps(settings, indent=4, ensure_ascii=False))

assert settings == {"environment": "staging","base_url": "https://example.com","timeout": 30}
assert type(settings["timeout"]) is int

save_test_config("production", "https://example.org", 60)
settings = load_test_config("config.json")

assert settings == {"environment": "production","base_url": "https://example.org","timeout": 60}
assert type(settings["timeout"]) is int
print("Все проверки пройдены!")
# ------------------------------------------------------------------
print()
print("___________★ Advanced ★__________\n")
# 4.Advanced
# Вы работаете QA Engineer. После запуска автоматизированных тестов необходимо создать отчёт для команды.
# Напишите функцию build_run_report(project_name, csv_filename)
# Функция получает название проекта и путь к CSV-файлу в формате из Task 2.
# Она должна
# 1.Прочитать все результаты тестирования.
# 2.Посчитать total, passed, failed, total_duration_ms.
# 3.Создать папку reports.
# 4.Внутри неё создать папку с названием проекта.
# 5.Создать файл summary.json с общей статистикой.
# 6.Создать файл failed_tests.txt, в который записать ID всех тестов со статусом FAILED.
# 7.Вернуть словарь с итоговой статистикой.
#   Пример
#      build_run_report("Shop", "results.csv")
#           reports/
#           Shop/
#               summary.json
#               failed_tests.txt
# Содержимое summary.json:
# {
#     "project": "Shop",
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500
# }
# Содержимое failed_tests.txt QA-1002
# Если папки ещё нет, она должна создаваться автоматически.
# •Если папка уже существует, программа должна работать без ошибки.
# •Если проваленных тестов нет, failed_tests.txt должен существовать, но оставаться пустым.
# •При повторном запуске файлы должны обновляться, а не дублировать старые результаты.
# Используйте: pathlib.Path, mkdir(parents=True, exist_ok=True), csv.DictReader(), json.dump(), with open(), циклы, условия, списки и словари.

#------------------------------------------------------------------
def build_run_report(project_name, csv_filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(csv_filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])

            if row["status"] == "PASSED":
                passed += 1

            if row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])
    statistics = {
        "project": project_name,
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms
    }

    project_folder = pathlib.Path("reports") / project_name
    project_folder.mkdir(parents=True, exist_ok=True)
    summary_path = project_folder / "summary.json"
    with open(summary_path, "w", encoding="utf-8") as file:
        json.dump(statistics, file, indent=4, ensure_ascii=False)

    failed_path = project_folder / "failed_tests.txt"
    with open(failed_path, "w", encoding="utf-8") as file:
        for test_id in failed_ids:
            file.write(f"{test_id}\n")
    return statistics

result = build_run_report("Shop", "results.csv")
print(json.dumps(result, indent=4, ensure_ascii=False))

assert build_run_report("Shop", "results.csv") == result
folder = pathlib.Path("reports") / "Shop"

with open(folder / "summary.json", "r", encoding="utf-8") as file:
    assert json.load(file) == result

with open(folder / "failed_tests.txt", "r", encoding="utf-8") as file:
    assert file.read().splitlines() == ["QA-1002"]

with open("all_passed.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id", "status", "duration_ms"])
    writer.writerow(["QA-1001", "PASSED", 120])
    writer.writerow(["QA-1002", "PASSED", 230])
result = build_run_report("Shop", "all_passed.csv")

assert result == {
    "project": "Shop",
    "total": 2,
    "passed": 2,
    "failed": 0,
    "total_duration_ms": 350
}

with open(folder / "failed_tests.txt", "r", encoding="utf-8") as file:
    assert file.read() == ""
print("Все проверки пройдены!")
build_run_report("Shop", "results.csv")
# ------------------------------------------------------------------
