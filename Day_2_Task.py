# Simple Calculator
name = input("Enter your full name : ").split()

first_name = name[0]
last_name = name[1]

print(f"Welcome {first_name}")

num_1 = float(input("Enter the first number : "))
num_2 = float(input("Enter the second number : "))

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

addition = num_1 + num_2
subtraction = num_1 - num_2
multiplication = num_1 * num_2
division = num_1 / num_2 

print(f"Addition : {num_1} + {num_2} = {addition}")
print(f"subtraction : {num_1} - {num_2} =  {subtraction}")
print(f"Multiplication : {num_1} * {num_2} =  {multiplication}")
print(f"Division : {num_1} / {num_2} =  {division}")
