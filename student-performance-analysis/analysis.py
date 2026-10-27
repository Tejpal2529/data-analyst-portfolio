
import csv

# Read student data from the CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

# Calculate the average score
scores = [int(student["score"]) for student in students]
average_score = sum(scores) / len(scores)

# Find the student with the highest score
top_student = max(students, key=lambda student: int(student["score"]))

# Display the results
print("STUDENT PERFORMANCE ANALYSIS")
print("-----------------------------")
print("Total students:", len(students))
print("Average score:", round(average_score, 2))
print("Top student:", top_student["name"])
print("Highest score:", top_student["score"])

print("\nStudents scoring 70 or above:")
for student in students:
    if int(student["score"]) >= 70:
        print(student["name"], "-", student["score"])
print("\nStudy Hours vs Student Scores:")
for student in students:
    print(
        student["name"],
        "- Study hours:", student["study_hours"],
        "| Score:", student["score"]
    )