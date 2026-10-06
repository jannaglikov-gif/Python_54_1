with open("user.txt", "w", encoding = "utf-8") as file:
    file.write("Janna\n")
    file.write("Dimitry\n")

with open("user.txt", "r", encoding = "utf-8") as file:
    content = file.read()
    print(content)
    print(len(content))

#    readLines() - return list where each element is new line

with open("user.txt", "r", encoding = "utf-8") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())
    print()

with open("user.txt", "r", encoding = "utf-8") as file:
    for line in file:
        print(line.strip())