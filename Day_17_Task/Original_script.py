import logging

# Setup error logging
logging.basicConfig(filename='Day_17_Task/error_log.txt', level=logging.ERROR)

# Define functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("You tried to divide by zero!")
        return None
