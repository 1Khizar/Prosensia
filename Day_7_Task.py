
# 🎯 Title: List Analyzer with Sorting and Loop-Based Summaries
# Focus: Use of for/while loops, enumerate, and manual logic to build a numeric dashboard.
# You’ll compute sum, average, min/max without using built-ins like sorted(), sum(), min().

# 🔹 Define function: analyze_numbers(numbers: list[float]) -> dict
# - Manually sort list using loops
# - Calculate total, average, min, max without built-in methods
# - Return result in dictionary format

# 🔹 Define function: print_dashboard(data: dict)
# - Uses for loop with enumerate()
# - Prints each key/value in formatted order
# → Example: 1. sorted → [2.3, 3.1, 4.5]

# - Ask user how many numbers to input
# - Take float inputs in a loop
# - Validate numeric input
# - Avoid using built-ins: sorted(), sum(), min(), max()

# Input: 3 values → 4.5, 2.3, 3.1
# Output:
# 1. sorted → [2.3, 3.1, 4.5]
# 2. sum → 9.9
# 3. average → 3.3
# 4. min → 2.3
# 5. max → 4.5

def analyze_numbers(numbers):
    sum_num = 0
    sorted_list = numbers[:]
    n = len(numbers)
    
    for i in range(n):
        for j in range(n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                 sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                 
    min_number = sorted_list[0]
    max_number = sorted_list[-1]
    
    for i in range(n):
        sum_num+=sorted_list[i]
    
    average_num = round(sum_num/n, 1)
    
    return {"sorted_list":sorted_list, "sum":sum_num,  "average":average_num, "min":min_number, "max":max_number}

def print_dashboard(data):
    for key, value in data.items():
        print(key, value)

user_input= []
total_numbers = int(input("How many values you want to enter : "))
for i in range(total_numbers):
    input_user = float(input(f"Enter the number {i+1} : "))
    user_input.append(input_user)
    
number_list = analyze_numbers(user_input)
print_dashboard(number_list)