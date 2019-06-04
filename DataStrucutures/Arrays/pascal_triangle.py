def factorial(number):
    result = 1
    if number == 0 or number == 1:
        return result
    elif number > 1:
        index = 1
        while index <= number:
            result = result * index
            index += 1
        
        return result

def nth_term_pascal(row, term):
    number = factorial(row) / (factorial(term) * factorial(row-term))
    return number


def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    row = []
    for i in range(n+1):
        row.append(nth_term_pascal(n, i))

    return row

'''
def nth_row_pascal(n):
    if n == 0:
        return [1]
    current_row = [1]
    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            next_number = previous_row[j] + previous_row[j - 1]
            current_row.append(next_number)
        current_row.append(1)
    return current_row
'''


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")

n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)


###########
# TEST
# factorial test
assert(factorial(0) == 1)
assert(factorial(1) == 1)
assert(factorial(2) == 2)
assert(factorial(3) == 6)
assert(factorial(4) == 24)
assert(factorial(5) == 120)
print("factorial test passed")
# factorial test end

# nth_term_pascal test
assert(nth_term_pascal(0,0) == 1)
assert(nth_term_pascal(1,0) == 1)
assert(nth_term_pascal(1,1) == 1)
assert(nth_term_pascal(2,0) == 1)
assert(nth_term_pascal(2,1) == 2)
assert(nth_term_pascal(2,2) == 1)
assert(nth_term_pascal(4,2) == 6)
assert(nth_term_pascal(4,3) == 4)
print("nth_term_pascal test passed")
# nth_term_pascal test end