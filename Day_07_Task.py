
# 🎯 Title: List Analyzer with Sorting and Loop-Based Summaries
# Focus: Use of for/while loops, enumerate, and manual logic to build a numeric dashboard.
# You’ll compute sum, average, min/max without using built-ins like sorted(), sum(), min().

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