def student_result(marks):
  
    for mark in marks:
        if mark < 0 or mark > 100:
            return "Invalid marks"

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return total, average, grade


result = student_result([85, 90, 78, 88, 92])

print("Total:", result[0])
print("Average:", result[1])
print("Grade:", result[2])