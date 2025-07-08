# Day 6 

# Function to evaluate grade from score
def evaluate_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score < 50:
        return "F"
    else:
        return "Invalid Score"

# Function to print grade summary
def print_grade_summary(student_name = 'Unnamed', score = 0.0):
    grade = evaluate_grade(score)
    if grade == "Invalid Score":
        print(f"Error: The score {score} is not within the valid range (0–100).")
    else:
        print(f"Student {student_name} scored {score} → Grade: {grade}")

# Example usage
print_grade_summary(student_name='Zara', score=87.5)
print_grade_summary(student_name='Ali', score=45)
print_grade_summary(student_name='Khizar', score=102)  # Invalid case
