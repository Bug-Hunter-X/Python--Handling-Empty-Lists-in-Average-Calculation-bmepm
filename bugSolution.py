def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Example with non-numeric values
my_mixed_list = [10, 20, 'a', 40, 50]
try:
    average_mixed = calculate_average(my_mixed_list)
    print(f"The average of mixed list is: {average_mixed}")
except TypeError as e:
    print(f"Error: {e}") #This will handle type error if non-numeric values are present