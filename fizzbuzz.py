def fizzbuzz(n: int) -> str:
    """Return FizzBuzz output for a given integer.

    Args:
        n: The integer to evaluate.

    Returns:
        "FizzBuzz" if n is divisible by both 3 and 5,
        "Fizz" if divisible by 3 only,
        "Buzz" if divisible by 5 only,
        or the string representation of n otherwise.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

if __name__ == '__main__':
    for i in range(1, 10):
        print(fizzbuzz(i))
