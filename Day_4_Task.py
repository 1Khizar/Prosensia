# Student Record System using Tuples & Sets

student_ids = (200, 132, 103, 104)  # Tuple of student IDs - immutable
print("Student IDs : ", student_ids)

courses = {"Python", "AI", "ML"}  # Set to store unique course names
print("\nInitial Courses :", courses)

courses.add("Data Science")  # Adds 'Data Science' to the set
print("\nAfter Adding 'Data Science':", courses)

courses.add("Python")  # 'Python' already exists, won't be added again
print("\nAfter Trying to Add Duplicate 'Python':", courses)

courses.remove("AI")  # Removes 'AI' from the set
print("\nAfter Removing 'AI':", courses)

print("\nFinal List of Unique Courses:")
for course in courses:
    print(course)
