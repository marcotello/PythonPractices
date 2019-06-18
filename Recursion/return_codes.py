'''
def get_letter_by_number(number):
    letter = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h",
        9: "i",
        10: "j",
        11: "k",
        12: "l",
        13: "m",
        14: "n",
        15: "o",
        16: "p",
        17: "q",
        18: "r",
        19: "s",
        20: "t",
        21: "u",
        22: "v",
        23: "w",
        24: "x",
        25: "y",
        26: "z"
    }

    return letter.get(number, "")

def divide_number(number, items, codes_list):
    right_code = ""
    left_code = ""
    if items > len(number):
        return
    else:
        index = 0
        while index < len(number):
            right_index = index + items
            value = number[index:right_index]
            letter = get_letter_by_number(int(value))
            if letter != "":
                right_code = right_code + letter
                
            index += items
        
        codes_list.append(right_code)

        second_index = len(number)
        while second_index > 0 :
            left_index = second_index - items
            
            if left_index < 0:
                left_index = 0

            value = number[left_index:second_index]
            letter = get_letter_by_number(int(value))
            if letter != "":
                left_code = left_code + letter
                
            second_index -= items
        
        codes_list.append(left_code)
        
        divide_number(number, items + 1, codes_list)

def all_codes(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    codes_list = list()
    items = 1

    divide_number(str(number), items, codes_list)

    print(codes_list)

    return codes_list

'''
# Solution

def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember: 
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)

def all_codes(number):
    if number == 0:
        return [""]
    
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    if remainder <= 26 and number > 9 :
        
        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)
        
        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet
    
    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10
    
    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)
    
    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet
        
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    
    return output


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    
    output = all_codes(number)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)

number = 145
solution =  ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)

number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)

number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)

'''
# *******************************
# Unit Testing
print("test for get_letter_by_number")
assert(get_letter_by_number(1) == "a")
assert(get_letter_by_number(2) == "b")
assert(get_letter_by_number(26) == "z")
assert(get_letter_by_number(14) == "n")
assert(get_letter_by_number(13) == "m")
assert(get_letter_by_number(50) == "Invalid letter")
print("get_letter_by_number passed")
'''