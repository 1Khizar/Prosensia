grade_point_map = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "F": 0.0
}

# Part 1 – Function to calculate weighted GPA
def calculate_weighted_gpa(grades):
    total_points = 0
    total_credits = 0

    for grade, credit in grades:
        grade_point = grade_point_map.get(grade.upper(), 0)
        total_points += grade_point * credit
        total_credits += credit

    if total_credits == 0:
        return 0.0

    gpa = total_points / total_credits
    return round(gpa, 2)

# Function to print summary
def print_gpa_summary(student_name, gpa):
    print(f"Student {student_name} has GPA: {gpa:.2f}")

# Example Run
grades_input = [('A', 3), ('B+', 4), ('C', 2)]
student = "Rania"
gpa = calculate_weighted_gpa(grades_input)

# Using named arguments
print_gpa_summary(student_name=student, gpa=gpa)
