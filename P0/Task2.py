"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def get_unique_numbers_with_total_call_time(calls):
    """
    This function iterates over the list of calls and returns a dictionary with the number and it's total time on phone.

    INPUT:
    calls: a list of calls. 

    RETURN: A dictionary with the phone numbers and the total duration on calling and receiveng calls.
    """

    # Creating an empty dictionary that will hold the information of every number and the time that 
    # have spent making calls and receiving calls.   - O(1)
    calls_data = dict()

    # iterating over the list of calls.  - O(n)
    # this has a complexity of O(n), because it is iterating over the whole list.
    for call in calls:
        if call[0] in calls_data:
            calls_data[call[0]] = calls_data[call[0]] + int(call[3])
        else:
            calls_data[call[0]] = int(call[3])

        if call[1] in calls_data:
            if call[1] != call[0]:
                calls_data[call[1]] = calls_data[call[1]] + int(call[3])
            else:
                continue
        else:
            calls_data[call[1]] = int(call[3])
       
    return calls_data

def get_number_with_highest_time(calls_dictionary):
    """
    This function returns the number with the longest duration by comparing all elements on a dictionary.
    INPUT:
    calls_dictionary: a dictionary of numbers and call time. 
    
    RETURN: a tuple with the number that has the longest duration, and the call time.
    """
    # the duration where we want to start comparing, in this 0.  - O(1)
    duration = 0
    # creating a variable to hold the number with the highest time.  - O(1)
    max_time_number = ""

    # iterating over the dictionary of numbers.  - O(n)
    # this has a complexity of O(n), because it is iterating over the whole dictionary.
    for call in calls_dictionary:
        # True, in case the duration of the call is higher than the previous value.  - O(1)
        if int(calls_dictionary[call]) > duration:
            # storing the number if it has a longer duration.  - O(1)
            max_time_number = call
            # updating the duration.  - O(1)
            duration = calls_dictionary[call]

    # returning the number with the highest call time.  - O(1)
    return (max_time_number, duration)


def main():
    
    # creating a dictionary of unique numbers and adding the total time that they have spend on the phone  - O(n)
    calls_dict = get_unique_numbers_with_total_call_time(calls)

    # getting the number with the highest call time by iterating over the list and finding the longest duration  - O(n)
    highest_time_number = get_number_with_highest_time(calls_dict)

    # printing the output  - O(3)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(highest_time_number[0], highest_time_number[1]))


if __name__ == "__main__":
    main()


'''
# UNIT TESTING 
# get_longest_call test
# test list of records
calls_test_list1 = [["97424 22395", "98453 94494", "01-09-2016 06:01:12", "186"], 
                    ["78298 91466", "(022)28952819", "01-09-2016 06:01:59", "2093"], 
                    ["97424 22395", "78298 91466", "01-09-2016 06:03:51", "1975"], 
                    ["93427 40118", "(022)28952819", "01-09-2016 06:11:23", "1156"]]
calls_dict = get_unique_numbers_with_total_call_time(calls_test_list1)
# testing the length
assert(len(calls_dict) == 5)
# testing the total time of 97424 22395 number
assert(calls_dict["97424 22395"] == 2161)
# testing the total time of (022)28952819 number
assert(calls_dict["(022)28952819"] == 3249)
print("test for get_unique_numbers_with_total_call_time passed")

# get_number_with_highest_time test
# test dictionary
calls_test_dict = {"97424 22395": 2161, 
                    "98453 94494": 186,
                    "78298 91466": 4068,
                    "(022)28952819": 3249,
                    "93427 40118": 1156 }
highest_time_number = get_number_with_highest_time(calls_test_dict)
assert(highest_time_number == ("78298 91466", 4068))
print("test for get_number_with_highest_time passed")
'''