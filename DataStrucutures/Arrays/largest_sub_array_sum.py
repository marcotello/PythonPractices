def calculating_iterations(array_size):
    iterations = 0
    for i in range(array_size):
        iterations += i

    return iterations

def sum_array_elements(arr):
    result = 0
    for number in arr:
        result += number
    
    return result

def get_maximun(arr):
    result = 0
    for item in arr:
        if item > result:
            result = item

    return result


def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    index = 2
    limit = len(arr) + 1
    second_index = len(arr) - 1
    iterations = calculating_iterations(len(arr))
    sums = []

    for i in range(iterations):
        while index < limit:
            for x in range(second_index):
                init = x
                end = x + index
                temp_arr = arr[init:end]
                sums.append(sum_array_elements(temp_arr))  
            
            index = index + 1
            second_index = second_index - 1

    maximun = get_maximun(sums)
    return maximun

'''
# Solution
def max_sum_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum
'''
            

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)

###########
# TESTING

# calculating_iterations Test
assert(calculating_iterations(2) == 1)
assert(calculating_iterations(3) == 3)
assert(calculating_iterations(4) == 6)
assert(calculating_iterations(5) == 10)
assert(calculating_iterations(6) == 15)
print("calculating_iterations PASSED")
# calculating_iterations Test end

# sum_array_elements Test
test_arr1 = [0, 0, 0]
assert(sum_array_elements(test_arr1) == 0)

test_arr2 = [-2, 1, 3]
assert(sum_array_elements(test_arr2) == 2)

test_arr3 = [4, 5, 6]
assert(sum_array_elements(test_arr3) == 15)

test_arr4 = [-2, -1, 3]
assert(sum_array_elements(test_arr4) == 0)

test_arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert(sum_array_elements(test_arr5) == 45)

print("sum_array_elements PASSED")
# sum_array_elements Test end