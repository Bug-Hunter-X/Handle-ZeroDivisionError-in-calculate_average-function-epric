# Python Bug Fix: Handling ZeroDivisionError in Average Calculation

This repository demonstrates a common error in Python and its solution. The original code for calculating the average of a list of numbers fails if the list is empty or contains only zeros, leading to a `ZeroDivisionError`. This improved version handles both cases gracefully, making the function more robust and reliable.

**Bug:** The `calculate_average` function didn't explicitly handle the `ZeroDivisionError` that could occur if the input list is empty or contains only zeros.

**Solution:** The solution implements checks to handle both cases. If the list is empty, 0 is returned. If the sum of the numbers is 0 and the list is not empty, 0 is returned to avoid division by zero. This ensures the function works correctly under various input conditions.

Feel free to explore the code and understand the bug and the implemented solution.