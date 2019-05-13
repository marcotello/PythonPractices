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


def get_numbers_without_incoming_calls(calls):
    telemarketers = set() 
    index = 0
    total_calls = len(calls)

    while index < total_calls:
        index2 = 0
        telemarketer = True
        while index2 < total_calls:
            if calls[index][0] == calls[index2][1]:
                telemarketer = False
                break    
            index2 += 1
        
        if telemarketer:
            telemarketers.add(calls[index][0])
        
        index  += 1
    
    return telemarketers

def get_numbers_without_messages(calls, texts):
    calls_list = list(calls)
    calls_index = 0
    text_index = 0

    while calls_index < len(calls_list):
        while text_index < len(texts):
            if calls_list[calls_index] == texts[text_index][0] or calls_list[calls_index] == texts[text_index][1]:
                calls_list.pop(calls_index)
            
            text_index += 1
        
        calls_index += 1

    return set(calls_list)

def print_lex_ordered_numbers(telemarketers):
    numbers = list(telemarketers)
    numbers.sort()
    for number in numbers:
        print(number)

def print_list_of_telemarketers(calls, texts):

    calls = get_numbers_without_incoming_calls(calls)
    telemarketers = get_numbers_without_messages(calls, texts)
    print_lex_ordered_numbers(telemarketers)


# TEST FOR get_numbers_without_incoming_calls
# four numbers with one caller from Bangalore
calls_test_list1 = [["1408371942", "98440 65896"], ["90087 42537", "(044)30727085"], 
                    ["(044)30727085", "92414 22596"], ["1408371942", "90087 42537"]]
assert(get_numbers_without_incoming_calls(calls_test_list1) == {"1408371942"})
#print("test for get_numbers_without_incoming_calls passed")

# TEST FOR get_numbers_without_messages
# one number at the end
calls_test_list2 = ["1408371942"]
text_test_list2 = [["87146 31956", "98440 65896"], ["90087 42537", "(044)30727085"], 
                    ["93435 21961", "92414 22596"], ["1408371944", "90087 42537"]]
assert(get_numbers_without_messages(calls_test_list2, text_test_list2) == {"1408371942"})
# two numbers at the end
calls_test_list3 = ["1408371942", "1408409918"]
text_test_list3 = [["87146 31956", "98440 65896"], ["90087 42537", "(044)30727085"], 
                    ["93435 21961", "92414 22596"], ["1408371944", "90087 42537"]]
assert(get_numbers_without_messages(calls_test_list3, text_test_list3) == {"1408371942", "1408409918"})
#print("test for get_numbers_without_messages passed")


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
print("These numbers could be telemarketers: ")
print_list_of_telemarketers(calls, texts)
