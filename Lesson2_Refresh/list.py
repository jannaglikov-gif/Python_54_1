from audioop import reverse
from cgitb import reset
from idlelib.debugger_r import restart_subprocess_debugger

fruits = ["apple", "banana", "orange"]
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(len(fruits))
fruits[1] = "cat"
print(fruits)

fruits.append("kiwi")
print(fruits)

fruits.append(["car", "trak"])
print(fruits)

fruits.extend(["cat", "dog"])
print(fruits)

fruits.insert(4, "pear")
print(fruits)
print()

e = ["apple", "banana", "orange"]
e.remove("banana")
print(e)
print()

f = ["apple", "banana", "orange"]
popped = f.pop(1)
print(popped, f)
print()

h = ["apple", "banana", "orange"]
del h[0]
print(h)
print()

k = ["apple", "banana", "orange"]
k.clear()
print(k)
print()

m = ["apple", "banana", "cherry", "banana"]
print(m.index("cherry"))
print(m.count("banana"))
print("apple" in m)
print("kiwi" not in m)
print()


numbers = [3, 1, 5, 2, 9, 6]
result = numbers.sort()
print(numbers, result)
print()

numbers_2 = [3, 1, 5, 2, 9, 6]
new_list = sorted(numbers_2)
print(numbers_2, new_list)
print()

numbers_3 = [3, 1, 5, 2, 9, 6]
numbers_3.reverse()
print(numbers_3)
print()

numbers_4 = [3, 1, 5, 2, 9, 6]
print(sorted(numbers_4, reverse=True))
print(numbers_4)
print()

items = ["apple", "banana", "orange"]

for item in items:
    print(item)

for i in range(len(items)):
    print(i,items[i])

print()

numbers_5 = [-2, 3, -1, 5, 0, -9]
result = []
for n in numbers_5:
    if n > 0:
        result.append(n)
print(result)
result2 = [n for n in numbers_5 if n < 0]
print(result2)



