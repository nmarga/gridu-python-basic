"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""


def read_numbers(n: int) -> str:
    """
    Awaits user input to enter a string of numbers,
    then computes the average of those numbers.
    """

    # Await user input and clean trailing white spaces
    processed_str = ''.join(input().split())

    # Split the input string into n words/numbers
    nums_str = processed_str.split(',', n)

    # Store the numbers
    nums = []

    # Parse each number into a float
    for num_str in nums_str:
        if len(nums) == n:
            break

        try:
            nums.append(float(num_str))
        except ValueError:
            pass

    # Get the total count of valid numbers
    nums_count = len(nums)

    # Compute the result
    if nums_count == 0:
        return "No numbers entered"
    else:
        nums_avg = sum(nums) / nums_count

        return f"Avg: {round(nums_avg, 2)}"
