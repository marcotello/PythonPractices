def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    number_str = ""

    for digit in arr:
        number_str = number_str + str(digit)

    number = int(number_str) + 1

    arr = []

    for digit in str(number):
        arr.append(int(digit))

    return arr
    

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")   

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

