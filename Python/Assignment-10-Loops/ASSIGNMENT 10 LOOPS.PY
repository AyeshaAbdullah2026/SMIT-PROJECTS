# ==========================================
# Python Loops Assignment
# Name:
# Roll No:
# ==========================================

# ===============================
# Using While Loop
# ===============================

print("===== While Loop Question 1 =====")
# 1. Print numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1

print("\n===== While Loop Question 2 =====")
# 2. Print numbers from 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1

print("\n===== While Loop Question 3 =====")
# 3. Print the multiplication table of a number n.
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

print("\n===== While Loop Question 4 =====")
# 4. Print the elements of the list using a loop.
numbers = [12, 45, 8, 23, 67, 34, 90, 15, 56, 78]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print("\n===== While Loop Question 5 =====")
# 5. Search for a number x in this tuple using loop.
numbers = (18, 45, 72, 91, 34, 56, 29, 83, 67, 10)

x = int(input("Enter number to search: "))

i = 0
while i < len(numbers):
    if numbers[i] == x:
        print("Number Found at index", i)
        break
    i += 1
else:
    print("Number Not Found")

print("\n===== While Loop Question 6 =====")
# 6. Find the sum of first n natural numbers.
n = int(input("Enter a number: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)


# ===============================
# Using For Loop
# ===============================

print("\n===== For Loop Question 1 =====")
# 1. Print the elements of the list using a loop.
fruits = [
    'Apple',
    'Banana',
    'Mango',
    'Orange',
    'Grapes',
    'Peach',
    'Cherry',
    'Guava',
    'Pineapple',
    'Watermelon'
]

for fruit in fruits:
    print(fruit)

print("\n===== For Loop Question 2 =====")
# 2. Search for a string x in this tuple using loop.
cities = (
    'Karachi',
    'Lahore',
    'Islamabad',
    'Peshawar',
    'Quetta',
    'Multan',
    'Hyderabad',
    'Faisalabad',
    'Sialkot',
    'Sukkur'
)

x = input("Enter city name: ")

for city in cities:
    if city == x:
        print("City Found")
        break
else:
    print("City Not Found")

print("\n===== For Loop Question 3 =====")
# 3. Find the factorial of a number.
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)


# ===============================
# Using range()
# ===============================

print("\n===== Range Question 1 =====")
# 1. Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)

print("\n===== Range Question 2 =====")
# 2. Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)

print("\n===== Range Question 3 =====")
# 3. Print the multiplication table of a number n.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print("\n===== Assignment Completed Successfully =====")
