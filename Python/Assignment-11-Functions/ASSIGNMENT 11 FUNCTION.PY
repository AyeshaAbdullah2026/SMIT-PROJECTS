# ==========================
# Python Functions Assignment
# ==========================

# Q1: Print the length of a list
def list_length(my_list):
    print("Length of the list is:", len(my_list))

numbers = [10, 20, 30, 40, 50]
list_length(numbers)


# Q2: Print all elements of a list in a single line
def print_list(my_list):
    print(*my_list)

fruits = ["Apple", "Banana", "Mango", "Orange"]
print_list(fruits)


# Q3: Find the factorial of a given number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial =", fact)

num = int(input("Enter a number: "))
factorial(num)


# Q4: Convert Pakistani Rupees (PKR) into US Dollars (USD)
def pkr_to_usd(pkr):
    usd = pkr / 285
    print("USD =", usd)

amount = float(input("Enter PKR: "))
pkr_to_usd(amount)


# Q5: Check whether a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

number = int(input("Enter a number: "))
even_odd(number)
