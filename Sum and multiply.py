# Function to calculate sum and multiplication
def calculate_operations(a, b):
    sum_result = a + b
    multiplication_result = a * b
    return sum_result, multiplication_result
num1 = 5
num2 = 3
sum_result, multiplication_result = calculate_operations(num1, num2)

print(f"Sum: {sum_result}")
print(f"Multiplication: {multiplication_result}")
