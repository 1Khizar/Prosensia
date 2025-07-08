
# 🔹 Define function: read_marks_file(filepath: str) -> dict
# - Read file with lines like: Zara,87 / Ali, / Rida,91
# - Handle missing or non-numeric scores using try/except
# - Return a dictionary of valid student → marks

# 🔹 Define function: print_summary(marks_dict: dict)
# - Loop through dict and print student scores
# - Calculate and display average
# - Handle empty file with ZeroDivisionError gracefully

# - Track and count skipped/invalid entries
# - Prompt user for file name
# - Use with open() context manager
# - Store and optionally print skipped lines

# File: marks.txt
# Zara,87 | Ali, | Rida,91 | Ahmed,abc
# Output:
# Zara → 87 | Rida → 91 | Average: 89.0
# Skipped 2 invalid entries.


def read_marks_file(input_file):
    
    student_marks_dict = {}
    skipped_lines = 0
    
    with open(input_file, "r") as file:
        content = file.read()
    
    content_split = content.split('|')

    for i in content_split:
        info = i.split(',')
        student = info[0].strip()
        student_marks = info[1]
        
        try: 
            marks = int(student_marks)   
            student !=' ' and type(marks) == int 
            student_marks_dict[student] = marks
        except:
            skipped_lines+=1
            continue
    
    return student_marks_dict, skipped_lines


def print_summary(marks_dict, skipped_lines):
    sum = 0
    
    print("Name Marks")
    for name, marks in marks_dict.items():
        sum +=marks
        print(name, marks)
        
    try:
        average = sum / len(marks_dict)
    except ZeroDivisionError:
        print("Not valid marks to calcaulte average.")
        
    print(f"Average : {average}")
    print(f"Skipped lines : {skipped_lines}")
    

file = input("Enter the  file name : ")
marks_dict, skipped_lines = read_marks_file(file)
print_summary(marks_dict, skipped_lines)