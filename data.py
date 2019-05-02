def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    number = None
    for item in sorted(in_list):
        if item > 0:
            number = item
            break
   
    return number

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-46.41, -55.11, 40.64]))
# Correct output: 40.64

print(smallest_positive([-33.04, 48.83, 75.33, 39.82, 76.38, 98.41, 71.27, 67.84, -16.58]))
# Correct output: 39.82

print(smallest_positive([-3.53, -56.3, 11.17, -25.21, 96.21, -44.62, 94.95, 65.85, 26.79, -88.16]))
# Correct output: 11.17

print(smallest_positive([-98.35]))
# Correct output: None