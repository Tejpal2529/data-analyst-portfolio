
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
import matplotlib.pyplot as plt

# Get study hours and scores
study_hours = [int(student["study_hours"]) for student in students]
student_scores = [int(student["score"]) for student in students]

# Create a chart
plt.scatter(study_hours, student_scores)

plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

# Show the chart
plt.show()


print("\nStudent Pass/Fail Analysis")

pass_mark = 50

for student in students:
    score = int(student["score"])

    if score >= pass_mark:
        result = "Pass"
    else:
        result = "Fail"

    print(student["name"], "-", result)
