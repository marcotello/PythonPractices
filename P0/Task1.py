"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def get_unique_numbers(numbers, numbers_set):
    """
    This function returns a set of unique numbers

    INPUT:
    numbers: a list of numbers with the following format on each element ["number1", "number 2" ... more elements].
    numbers_set: the set where the unique numbers are stored.

    RETURN: a set with unique numbers.
    """
    
    for number in numbers:
        numbers_set.add(number[0])
        numbers_set.add(number[1])    
    
    return numbers_set


def main():
    # I have chosen set as my data collection because for this problem the order doesn't matter. Set holds unique hashable object like strings.
    # Creating the set - O(1)
    numbers_set = set()

    # calling get_unique_numbers function - O(n)
    numbers_set = get_unique_numbers(calls, numbers_set)
    
    # calling get_unique_numbers function - O(n)
    numbers_set = get_unique_numbers(texts, numbers_set)
    
    # printing the len of the set - O(3)
    print("There are {} different telephone numbers in the records.".format(len(numbers_set)))


if __name__ == "__main__":
    main()


"""
# UNIT TESTING
# get_unique_numbers test
test_list1 = [["(022)39006198", "98440 65896"], ["90087 42537", "(080)35121497"], 
                    ["(044)30727085", "90087 42537"], ["90087 42537", "(022)39006198"]]
assert(len(get_unique_numbers(test_list1, set())) == 5)

test_list2 = [["(022)39006198", "98440 65896"], ["(022)39006198", "98440 65896"], 
                    ["98440 65896", "(022)39006198"], ["98440 65896", "(022)39006198"]]
assert(len(get_unique_numbers(test_list2, set())) == 2)
print("test for get_unique_numbers passed")
"""