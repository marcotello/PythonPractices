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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_numbers_called_by_area_code(area_code, calls):
    """
    This function returns a list of area codes calles by an specific area code.

    INPUT:
    area_code: the area code where we want to filter the list
    calls: the list of calls

    RETURN: a list of numbers called by an specific area code.
    """

    # I have chosen set as my data collection because for this problem the order doesn't matter. Set holds unique hashable object like strings.
    # Creating the set - O(1)
    called_numbers = set()
    
    # the index for iterating the list of calls. It starts on 0 - O(1)
    index = 0

    # iterating over the list of calls - O(n)
    while index < len(calls):
        # compare if the caller number starts with the area code - O(1)
        if calls[index][0].startswith(area_code):
            # if the caller number starts with the area code, then the reciever number is add to the set - O(4)
            # Also, the filter_area_codes function is calledx to filter just the area code of the receiver number. 
            called_numbers.add(filter_area_codes(calls[index][1]))
        
        # increasing the index by 1 - O(1)
        index += 1

    # returning a list of area codes based on the set - O(1)
    return list(called_numbers)

def filter_area_codes(number):
    if number.startswith('('):
        return number[:number.find(')')+1]
    elif number.find(' ') > 0:
        if number.startswith('7') or number.startswith('8') or number.startswith('9'):
            return number[:4]
            
def print_lex_ordered_numbers(numbers):
    numbers.sort()
    for number in numbers:
        print(number)

def get_numbers_called_by_area_code_to_area_code(area_code, area_code2, calls):
    called_numbers = set()
    index = 0
    while index < len(calls):
        if calls[index][0].startswith(area_code) and calls[index][1].startswith(area_code2):
            called_numbers.add(calls[index][0])
        index += 1
    
    return len(called_numbers)

def get_percentage_from_fixed_lines(number_of_calls_from_Bangalore, number_of_calls_from_Bangalore_to_Bangalore):
    return (number_of_calls_from_Bangalore_to_Bangalore * 100) / number_of_calls_from_Bangalore

def main():
    # Part A solution
    print("The numbers called by people in Bangalore have codes:")
    calls_from_Bangalore = get_numbers_called_by_area_code('(080)', calls)
    print_lex_ordered_numbers(calls_from_Bangalore)

    # Part B solution
    print("{:.2f}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
        .format(get_percentage_from_fixed_lines(len(calls_from_Bangalore), 
            get_numbers_called_by_area_code_to_area_code('(080)', '(080)', calls))))

if __name__ == "__main__":
    main()


"""
# UNIT TESTING
# get_numbers_called_by_area_code test
# four numbers with one caller from Bangalore
calls_test_list1 = [["(080)47459867", "98440 65896"], ["90087 42537", "(080)35121497"], 
                    ["(044)30727085", "92414 22596"], ["97447 92655", "(022)39006198"]]
#assert(get_numbers_called_by_area_code("(080)", calls_test_list1) == ["98440 65896"])
# four numbers with two callers from Bangalore
calls_test_list2 = [["(080)47459867", "98440 65896"], ["90087 42537", "(080)35121497"], 
                    ["(044)30727085", "92414 22596"], ["(080)23802940", "98445 71741"]]
#assert(get_numbers_called_by_area_code("(080)", calls_test_list2) == ["98445 71741", "98440 65896"])
# six numbers with three callers in Bangalore and two are duplicated
calls_test_list3 = [["(080)47459867", "98440 65896"], ["90087 42537", "(080)35121497"], 
                    ["(044)30727085", "92414 22596"], ["(080)23802940", "98445 71741"],
                    ["78130 00821", "98453 94494"], ["(080)23802940", "90352 50054"]]
#assert(get_numbers_called_by_area_code("(080)", calls_test_list3) == ["90352 50054", "98445 71741", "98440 65896"])
# six numbers with three callers from Bangalore and two receivers are duplicated
calls_test_list4 = [["(080)47459867", "98440 65896"], ["90087 42537", "(080)35121497"], 
                    ["(044)30727085", "92414 22596"], ["(080)23802940", "98445 71741"],
                    ["78130 00821", "98453 94494"], ["(080)67362492", "98440 65896"]]
#assert(get_numbers_called_by_area_code("(080)", calls_test_list4) == ["98445 71741", "98440 65896"])
# four numbers with none caller from Bangalore
calls_test_list5 = [["98440 65896", "(080)47459867"], ["90087 42537", "(080)35121497"], 
                    ["(044)30727085", "92414 22596"], ["97447 92655", "(022)39006198"]]
#assert(get_numbers_called_by_area_code("(080)", calls_test_list5) == [])
print("test for get_numbers_called_by_area_code passed")

# print_lex_ordered_numbers test
# test with eigth numbers on the list
order_test_list1 = ["(080)47459867", "98440 65896", "90087 42537", "(080)35121497", 
                    "(044)30727085", "92414get_numbers_called_by_area_code 22596", "97447 92655", "(022)39006198"]
print_lex_ordered_numbers(order_test_list1)
print("test for print_lex_ordered_numbers passed")

# get_numbers_called_by_area_code_to_area_code test
# test with eigth numbers on the list two callers from Bangalore and one receiver from Bancalore
bangalore_calls_test_list1 = [["(080)47459867", "98440 65896"], ["90087 42537", "(0471)6537077"], 
                    ["(044)30727085", "92414 22596"], ["(080)23802940", "(080)35121497"],
                    ["78130 00821", "98453 94494"], ["98453 46196", "90352 50054"]]
#assert(get_numbers_called_by_area_code_to_area_code("(080)", "(080)", bangalore_calls_test_list1) == 1)
# test with eigth numbers on the list one caller from Bangalore and two receivers from Bancalore
bangalore_calls_test_list2 = [["98440 65896", "(080)47459867"], ["90087 42537", "(0471)6537077"], 
                    ["(044)30727085", "92414 22596"], ["(080)23802940", "(080)35121497"],
                    ["78130 00821", "98453 94494"], ["98453 46196", "90352 50054"]]
assert(get_numbers_called_by_area_code_to_area_code("(080)", "(080)", bangalore_calls_test_list1) == 1)
# four numbers with none caller from Bangalore
bangalore_calls_test_list3 = [["98440 65896", "(080)47459867"], ["90087 42537", "(080)35121497"], 
                    ["(044)30727085", "92414 22596"], ["97447 92655", "(022)39006198"]]
assert(get_numbers_called_by_area_code_to_area_code("(080)", "(080)", bangalore_calls_test_list3) == 0)
print("test for get_numbers_called_by_area_code_to_area_code passed")

# test filter_area_codes
# test with a fixed number
assert(filter_area_codes("(044)30727085") == "(044)")
# test with a celphone
assert(filter_area_codes("98440 65896") == "9844")
# test with a telemarketing number
assert(filter_area_codes("1409994233") == None)
print("test for filter_area_codes passed")

# test get_percentage_from_fixed_lines
assert(get_percentage_from_fixed_lines(8, 4) == 50)
assert(get_percentage_from_fixed_lines(10, 2) == 20)
assert(get_percentage_from_fixed_lines(10, 3) == 30)
assert(get_percentage_from_fixed_lines(10, 0) == 0)
print("test for get_percentage_from_fixed_lines passed")
"""