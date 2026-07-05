print("PERSONAL POCKET CGPA CALCULATOR")

courses = int(input("How many courses did you offer? "))

total_points = 0
total_units = 0

for i in range(courses):
    print("\nCourse", i + 1)

    unit = int(input("Course Unit: "))
    score = int(input("Course Score: "))

    if score >= 70:
        point = 5
    elif score >= 60:
        point = 4
    elif score >= 50:
        point = 3
    elif score >= 45:
        point = 2
    elif score >= 40:
        point = 1
    else:
        point = 0

    total_points = total_points + (point * unit)
    total_units = total_units + unit

cgpa = total_points / total_units

print("\nYour CGPA is:", round(cgpa, 2))
