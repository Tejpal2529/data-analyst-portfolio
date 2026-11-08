import pandas as pd

# Read student data from CSV
df = pd.read_csv("students.csv")

# Display all student data
print("STUDENT DATA")
print(df)

# Display first 5 rows
print("\nFIRST FIVE STUDENTS")
print(df.head())

# Display basic information
print("\nDATA INFORMATION")
print(df.info())

# Display statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())
# Filter students who scored 70 or above

print("\nSTUDENTS WHO PASSED WITH 70 OR ABOVE")

passed_students = df[df["score"] >= 70]

print(passed_students)
# Sort students by score (highest to lowest)

print("\nSTUDENTS RANKED BY SCORE")

sorted_students = df.sort_values(
    by="score",
    ascending=False
)

print(sorted_students)
# Data Cleaning

print("\nCHECKING MISSING VALUES")

print(df.isnull().sum())

print("\nCHECKING DUPLICATE ROWS")

print(df.duplicated().sum())
# Handling Missing Values

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Create a cleaned copy
df_clean = df.copy()

# Fill missing study hours with the median
df_clean["study_hours"] = df_clean["study_hours"].fillna(
    df_clean["study_hours"].median()
)

# Fill missing scores with the median
df_clean["score"] = df_clean["score"].fillna(
    df_clean["score"].median()
)

print("\nDATA AFTER CLEANING")
print(df_clean)

print("\nMISSING VALUES AFTER CLEANING")
print(df_clean.isnull().sum())