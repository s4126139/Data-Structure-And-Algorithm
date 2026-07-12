def sum_of_two_digits(first_digit, second_digit):
    # Returns the sum of the two input numbers
    return first_digit + second_digit


if __name__ == '__main__':
    # Read one line from input, for example: "2 3"
    # split() separates the string by spaces, and map(int, ...) converts both values to integers
    a, b = map(int, input().split())

    # Call the function and print the result
    print(sum_of_two_digits(a, b))