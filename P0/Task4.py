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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def get_numbers_without_incoming_calls(calls):
    """
    This function returns a set of numbers that does not have incoming calls.

    INPUT:
    calls: the list of calls

    RETURN: a set of numbers that doesn't have incoming calls.
    """
    # creating the set  - O(1)
    telemarketers = set() 
    # creating the index  - O(1)
    index = 0
    # getting the length of the calls list  - O(1)
    total_calls = len(calls)

    # iterating over the list of calls  - O(n)
    while index < total_calls:
        # creating a second index  - O(1)
        index2 = 0
        # creating a booleand variable to know if the number haven't receive a call  - O(1)
        telemarketer = True

        # iterating the list again to look if the number haven't receive a call  - O(n)
        while index2 < total_calls:
            # checking if the caller number is on the receivers numbers  - O(1)
            if calls[index][0] == calls[index2][1]:
                # if the number is on the receivers numbers then is not a telemarketer  - O(1)
                telemarketer = False
                # breaking the cicle, it's not important to search over the complete list  - O(1)
                break
            # increasing the second index by 1  - O(1)    
            index2 += 1
        
        # if was a telemarketer  - O(1)
        if telemarketer:
            # if was a telemarketer, then add the number to the list  - O(1)
            telemarketers.add(calls[index][0])
        
        # increase the index by 1  - O(1)
        index  += 1
    
    # converting the set to a list, and returning the list of possible telemarketers  - O(n)
    return list(telemarketers)

def get_numbers_without_messages(calls, texts):
    """
    This function given a set of calls and a list of texts, checks if the numbers on the set of calls
    never send texts or receive texts.

    INPUT:
    calls: a set of calls
    texts: a list if numbers that have sent and receive texts.

    RETURN: a set of numbers that never send texts or receive texts.
    """
    # creating an index  - O(1)
    calls_index = 0
    # creating a second index  - O(1)
    text_index = 0

    # iterating the list of calls  - O(n)
    while calls_index < len(calls):
        # iterating the list of texts  - O(n)
        while text_index < len(texts):
            # checking if the number on the list of calls is on the sender text or receiver text  - O(1)
            if calls[calls_index] == texts[text_index][0] or calls[calls_index] == texts[text_index][1]:
                # deleting the number if it's on the list of texts.  - O(1)
                calls.pop(calls_index)
            
            # increasing the second index by 1 - O(1)
            text_index += 1
        
        # increasing the index by 1 - O(1)
        calls_index += 1

    # returning the list of numbers - O(1)
    return calls

def print_lex_ordered_numbers(telemarketers):
    """
    This function sorts a set of numbers in lexicographic order and prints each number.

    INPUT: 
    numbers: a list of numbers. 

    RETURN: None, this function doesn't return anything.
    """
    # sorting the list - O(nlogn) 
    telemarketers.sort()
    # iterating the list to print the numbers - O(n)
    for number in telemarketers:
        # printing the numbers
        print(number)

def main():
    # getting a list of calls without numbers that receive a call - O(n^2)
    set_calls = get_numbers_without_incoming_calls(calls)
    # getting numbers that have never send or receive a text  - O(n^2)
    telemarketers = get_numbers_without_messages(set_calls, texts)
    # printing the message of the solution.  - O(1)
    print("These numbers could be telemarketers: ")
    # printing those numbers.  - O(nlogn) 
    print_lex_ordered_numbers(telemarketers)

if __name__ == "__main__":
    main()


"""
# UNIT TESTING
# get_numbers_without_incoming_calls test
# four numbers with one caller frget_numbers_called_by_same_area_codeom Bangalore
calls_test_list1 = [["1408371942", "98440 65896"], ["90087 42537", "(044)30727085"], 
                    ["(044)30727085", "92414 22596"], ["1408371942", "90087 42537"]]
assert(get_numbers_without_incoming_calls(calls_test_list1) == ["1408371942"])
# print("test for get_numbers_without_incoming_calls passed")

# get_numbers_without_messages test
# one number at the end
calls_test_list2 = ["1408371942"]
text_test_list2 = [["87146 31956", "98440 65896"], ["90087 42537", "(044)30727085"], 
                    ["93435 21961", "92414 22596"], ["1408371944", "90087 42537"]]
assert(get_numbers_without_messages(calls_test_list2, text_test_list2) == ["1408371942"])
# two numbers at the end
calls_test_list3 = ["1408371942", "1408409918"]
text_test_list3 = [["87146 31956", "98440 65896"], ["90087 42537", "(044)30727085"], 
                    ["93435 21961", "92414 22596"], ["1408371944", "90087 42537"]]
assert(get_numbers_without_messages(calls_test_list3, text_test_list3) == ["1408371942", "1408409918"])
#print("test for get_numbers_without_messages passed")
"""