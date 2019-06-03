def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    
    numbers_dict = dict()
    result = 0
    for digit in arr:
        if numbers_dict.get(digit, 0) == 0:
            numbers_dict[digit] = 1
        elif numbers_dict[digit] == 1:
            numbers_dict[digit] = 2
            result = digit
            break
        
    return result
    """
    current_sum = 0
    expected_sum = 0
    
    for num in arr:
        current_sum += num

    for i in range(len(arr) - 1):
        expected_sum += i
    
    return current_sum - expected_sum

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
solution = 11

test_case = [arr, solution]
test_function(test_case)