def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numeric values

    Returns:
        float: The average of the numbers, or 0 if the list is empty
    """
    if not numbers:
        return 0

    total = sum(numbers)
    count = len(numbers)
    return total / count

data = [10,70,30,90]

print(calculate_average(data))