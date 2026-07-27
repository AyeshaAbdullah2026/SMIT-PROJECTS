# =========================
# Q1 — Student Profile System
# =========================

student = {
    "name": "Ayesha",
    "age": 18,
    "city": "Karachi",
    "hobbies": ["Reading", "Coding", "Painting"],
    "skills": ["Python", "HTML", "CSS"]
}

print("Student Name:", student["name"])
print("First Hobby:", student["hobbies"][0])
print("Total Skills:", len(student["skills"]))


# =========================
# Q2 — Student Marks System
# =========================

marks = {
    "math": 85,
    "english": 78,
    "science": 80,
    "computer": 90
}

print("Math:", marks["math"])
print("English:", marks["english"])
print("Science:", marks["science"])
print("Computer:", marks["computer"])

total = marks["math"] + marks["english"] + marks["science"] + marks["computer"]
average = total / 4

print("Total Marks:", total)
print("Average Marks:", average)


# =========================
# Q3 — Grade Checking System
# =========================

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Final Grade:", grade)

if average >= 60:
    print("Passed")
else:
    print("Failed")


# =========================
# Q4 — Attendance Management System
# =========================

attendance = {
    "total_classes": 100,
    "attended_classes": 80
}

attendance_percentage = (attendance["attended_classes"] / attendance["total_classes"]) * 100

print("Attendance Percentage:", attendance_percentage)

if attendance_percentage < 75:
    print("Short Attendance")
else:
    print("Eligible For Exam")


# =========================
# Q5 — Fee Management System
# =========================

student["fee_paid"] = True

if student["fee_paid"]:
    print("Fee Cleared")
else:
    print("Fee Pending")


# =========================
# Q6 — Skills Management System
# =========================

student["skills"].append("JavaScript")
student["skills"].remove("HTML")

print("Updated Skills:", student["skills"])
print("Total Skills:", len(student["skills"]))


# =========================
# Q7 — Login Authentication System
# =========================

login = {
    "username": "admin",
    "password": "12345"
}

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == login["username"] and password == login["password"]:
    print("Login Successful")
else:
    print("Invalid Credentials")


# =========================
# Q8 — Address Management System
# =========================

student["address"] = {
    "area": "Gulshan",
    "street": "Street 10",
    "house_number": 25
}

print("Complete Address:")
print(student["address"]["house_number"])
print(student["address"]["street"])
print(student["address"]["area"])

student["address"]["area"] = "North Nazimabad"
student["address"]["zip_code"] = "74700"

print("Updated Address:", student["address"])


# =========================
# Q9 — Multiple Students Database
# =========================

students = {
    "student1": {
        "name": "Ayesha",
        "city": "Karachi",
        "marks": 88
    },
    "student2": {
        "name": "Ali",
        "city": "Lahore",
        "marks": 92
    }
}

print("Student1 Name:", students["student1"]["name"])
print("Student2 Marks:", students["student2"]["marks"])

students["student2"]["city"] = "Islamabad"

print("Updated Student2 City:", students["student2"]["city"])


# =========================
# Q10 — Final Student Report Card System
# =========================

report_card = {
    "profile": {
        "name": "Ayesha",
        "age": 18,
        "city": "Karachi"
    },
    "marks": marks,
    "total": total,
    "average": average,
    "grade": grade,
    "attendance": attendance_percentage,
    "fee_status": "Fee Cleared",
    "skills": student["skills"],
    "address": student["address"]
}

print("\n========== REPORT CARD ==========")

print("Name:", report_card["profile"]["name"])
print("Age:", report_card["profile"]["age"])
print("City:", report_card["profile"]["city"])

print("\nMarks")
print("Math:", report_card["marks"]["math"])
print("English:", report_card["marks"]["english"])
print("Science:", report_card["marks"]["science"])
print("Computer:", report_card["marks"]["computer"])

print("\nTotal:", report_card["total"])
print("Average:", report_card["average"])
print("Grade:", report_card["grade"])
print("Attendance:", report_card["attendance"], "%")
print("Fee Status:", report_card["fee_status"])
print("Skills:", report_card["skills"])
print("Address:", report_card["address"])

print("================================")