# =========================
# Q1 — Online Food Delivery System
# =========================

foods = ["Burger", "Pizza", "Fries", "Broast", "Sandwich"]

print("First Food:", foods[0])
print("Last Food:", foods[-1])

foods[2] = "Pasta"
foods.append("Zinger")
foods.insert(2, "Shawarma")
foods.remove("Pizza")
foods.pop()

print("Total Items:", len(foods))
print("First 3 Items:", foods[:3])
print("Last 2 Items:", foods[-2:])

foods.reverse()
print("After Reverse:", foods)

foods.sort()
print("After Sort:", foods)

print("Final List:", foods)


# =========================
# Q2 — Student Attendance Management
# =========================

students = ["Ali", "Sara", "Ahmed", "Zoha Khan", "Hira"]

print("Second Student:", students[1])
print("Last Student:", students[-1])

students[2] = "Hamza"
students.append("Fatima")
students.insert(1, "Ayesha")
students.remove("Sara")
students.pop(3)

print("Total Students:", len(students))
print("Students (1 to 4):", students[1:5])

students.reverse()
print("Final List:", students)


# =========================
# Q3 — Mobile Prices Analysis
# =========================

prices = [45000, 120000, 30000, 85000, 60000]

prices.sort()
print("Highest Price:", prices[-1])
print("Lowest Price:", prices[0])

print("Ascending:", prices)

prices.sort(reverse=True)
print("Descending:", prices)

prices.append(75000)
prices.remove(60000)
prices.pop()

print("First 3 Prices:", prices[:3])
print("Last 2 Prices:", prices[-2:])
print("Total Prices:", len(prices))


# =========================
# Q4 — Cricket Team Management
# =========================

players = ["Babar", "Rizwan", "Shaheen", "Naseem", "Shadab"]

print("Captain:", players[0])
print("Last Player:", players[-1])

players[4] = "Imad"
players.append("Haris")
players.insert(2, "Fakhar")
players.remove("Naseem")

print("First 4 Players:", players[:4])
print("Last 3 Players:", players[-3:])

players.reverse()
print("Final Squad:", players)


# =========================
# Q5 — Shopping Cart System
# =========================

cart = ["Shoes", "Watch", "Bag", "Laptop", "Bottle"]

print("First Item:", cart[0])
print("Last Item:", cart[-1])

cart[4] = "Headphones"
cart.append("Keyboard")
cart.insert(1, "Mouse")
cart.remove("Bag")
cart.pop()

print("Total Items:", len(cart))
print("Middle 3 Items:", cart[1:4])

cart.reverse()
print("Updated Cart:", cart)


# =========================
# Q6 — Employee Salary Records
# =========================

salaries = [25000, 40000, 70000, 55000, 90000]

print("Highest Salary:", max(salaries))
print("Lowest Salary:", min(salaries))

salaries.sort()
print("Ascending:", salaries)

salaries.sort(reverse=True)
print("Descending:", salaries)

salaries.append(65000)
salaries.remove(40000)

print("Second Highest Salary:", salaries[1])
print("First 3 Salaries:", salaries[:3])
print("Total Salaries:", len(salaries))
print("Final Salary List:", salaries)


# =========================
# Q7 — Movie Collection System
# =========================

movies = ["Avatar", "Inception", "Joker", "Titanic", "Interstellar"]

print("First Movie:", movies[0])
print("Last Movie:", movies[-1])

movies[2] = "Batman"
movies.append("Frozen")
movies.insert(3, "Spider-Man")
movies.remove("Titanic")
movies.pop()

print("First 4 Movies:", movies[:4])

movies.reverse()
print("Final Movie Collection:", movies)


# =========================
# Q8 — Exam Marks Analysis
# =========================

marks = [78, 45, 90, 66, 82]

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

marks.sort()
print("Ascending:", marks)

marks.sort(reverse=True)
print("Descending:", marks)

marks.append(88)
marks.remove(45)

print("Top 3 Marks:", marks[:3])
print("Last 2 Marks:", marks[-2:])
print("Total Subjects:", len(marks))
print("Final Marks:", marks)


# =========================
# Q9 — Website Visitors Record
# =========================

visitors = ["Ali", "Sara", "Ahmed", "Zoha Khan", "Hira"]

print("First Visitor:", visitors[0])
print("Last Visitor:", visitors[-1])

visitors.append("Fatima")
visitors.insert(2, "Ayesha")
visitors.remove("Ahmed")
visitors.pop()

print("First 3 Visitors:", visitors[:3])
print("Last 3 Visitors:", visitors[-3:])

visitors.reverse()

print("Total Visitors:", len(visitors))
print("Final Visitors List:", visitors)


# =========================
# Q10 — Programming Languages System
# =========================

languages = ["Python", "JavaScript", "Java", "C++", "PHP"]

print("First Language:", languages[0])
print("Last Language:", languages[-1])

languages[4] = "TypeScript"
languages.append("Go")
languages.insert(2, "Rust")
languages.remove("Java")

print("First 4 Languages:", languages[:4])
print("Last 2 Languages:", languages[-2:])

languages.sort()
print("Alphabetical:", languages)

languages.reverse()
print("Final Updated Languages:", languages)
