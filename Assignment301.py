#  Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

list = (8,2,3,0,7)

def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total    
result = sum_numbers(list)
print("Expected Output:",result)








