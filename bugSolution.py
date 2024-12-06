def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    if total == 0:
        return 0  # Handle list with only zeros
    return total / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1, 0, 3, 4, 5]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average with zero is: {average_with_zero}")

my_zero_list = [0,0,0]
average_zero_list = calculate_average(my_zero_list)
print(f"The average of a zero list is: {average_zero_list}")