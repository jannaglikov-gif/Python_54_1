from pickletools import string1

s = "cat"
s.upper()
print(s)

s1 = 'Hello'
s2 = "Hello"
s3 = """Line one, 
line two"""

print(s1)
print(s2)
print(s3)

#len
s = "Hello my group!"
print(len(s))

print(s[0])
print(s[4])
print(s[14])
print(s[-1])
# print(s[100])
print()
# len()1 2 3 4 5 6
s1 = "P y t h o n"
# ind  0 1 2 3 4 5 -> Index of last element = len()-1 or -1
# slicing -> my_string[start:end:step]
text = "automation"

print(s1[2:6])
print(s1[:4]) #from start to index 4 exclusive
print(s1[4:]) #from index 4 to end of string
print(s1[:])
print(s1[::2]) #every 2nd symbol
print(s1[::-1]) #reverse
print(s1[5:100])
print()

name = "Maria"
last_name = "Ivanova"
age = 25
print(name + "" + last_name + "" + str(age))
print(f"Hi, my name is {name}, my last name is {last_name} and i am {age}" )
print()

#upper()/lower()
raw = "Automation QA"
print(raw.upper())
print(raw.lower())

#strip()
print(raw.strip().upper())

#split()/join()
cvs_line = "Login: Cart, Checkout, Mama, Papa"
parts =  cvs_line.split(",")
print(parts)
print(" - ".join(parts))

msg ="Test failed: element not found"
print(msg.replace("failed", "passed"))
print()

#find() and index()
#find()-->-1 if substring is not found
#index()-->ValueError if substring is not found
s = "banana"
print(s.find("na"))
print(s.index("na"))

print(s.find("xyz"))
#print(s.index("xyz"))

#count()
print(s.count("na"))



