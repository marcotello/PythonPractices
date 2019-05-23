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

def get_longest_call(calls, duration=0):
    """
    This function returns the call with the longest duration by comparing all elements on a list.

    INPUT:
    calls: a list of calls. 
    duration: the duration where we want to start comparing. 0 by default.

    RETURN: the call that has the longest duration.
    """

    # creating an empty list that will hold the longest call.  - O(1)
    call_data = list()

    # iterating over the list of calls.  - O(n)
    # this has a complexity of O(n), because it is iterating over the whole list.
    for call in calls:

        # True, in case the duration of the call is longer than the previous value.  - O(1)
        if int(call[3]) > duration:
            # storing the call if it has a longer duration.  - O(1)
            call_data = call
            # updating the duration.  - O(1)
            duration = int(call[3])

    # returning the longest call.  - O(1)
    return call_data

def get_month_name(month):
    """
    This function returns the month name given the number.

    INPUT:
    month: the number of the month.

    RETURN: the name of the month.
    """

    # creating a month dictionary
    months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May',
              '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', 
              '11': 'November', '12': 'December'}

    # returning the month name by it's key.
    return months[month]


def main():
    # getting the longest call by iterating over the list and finding the longest duration - O(n)
    call = get_longest_call(calls)

    # splitting the date-time string - O(1)
    day, month, year = call[2].split('-')

    # printing the output - O(6)
    print("{} spent the longest time, {} seconds, on the phone during {} {}.".format(call[0], call[3], get_month_name(month), year[:year.find(' ')]))


if __name__ == "__main__":
    main()


"""
# UNIT TESTING
# get_longest_call test
# two calls with different duration time
calls_test_list1 = [["(0821)6141380", "90366 69257", "01-09-2016 06:54:44", "2147"], ["(022)47410783", "93412 26084", "01-09-2016 07:50:38", "96"]]
assert(get_longest_call(calls_test_list1) == ["(0821)6141380", "90366 69257", "01-09-2016 06:54:44", "2147"])
# two calls with the same duration
calls_test_list2= [["(0821)6141380", "90366 69257", "01-09-2016 06:54:44", "2147"], ["(080)47459867", "98440 65896", "01-09-2016 08:08:59", "2147"]]
assert(get_longest_call(calls_test_list2) == ["(0821)6141380", "90366 69257", "01-09-2016 06:54:44", "2147"])
# four calls with different duration time
calls_test_list3 = [["(0821)6141380", "90366 69257", "01-09-2016 06:54:44", "2147"], ["(022)47410783", "93412 26084", "01-09-2016 07:50:38", "96"],
                    ["92423 51078", "78134 03625", "04-09-2016 09:31:44", "7036"], ["99003 88572", "(080)46304537", "01-09-2016 16:17:01", "3348"]]
assert(get_longest_call(calls_test_list3) == ["92423 51078", "78134 03625", "04-09-2016 09:31:44", "7036"])

# get_month_name test
# should return January
assert(get_month_name('01') == "January")
# should return February
assert(get_month_name('02') == "February")
# should return December
assert(get_month_name('12') == "December")
# should return May
assert(get_month_name('05') == "May")
"""