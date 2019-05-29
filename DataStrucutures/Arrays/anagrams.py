def count_characters(word):
    words = dict()

    word = word.casefold()

    for char in word:
        if char != " ":
            if char in words:
                words[char] = words[char] + 1
            else:
                words[char] = 1
    
    return words

def compare_dictionaries(dict1, dict2):

    result = True

    for element in dict1:
        if element in dict2:
            if dict1[element] == dict2[element]:
                result = True
            else:
                result = False
                break
        else:
            result = False
            break
    
    return result

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: Write your solution here

    str1_dict = count_characters(str1)
    str2_dict = count_characters(str2)

    return compare_dictionaries(str1_dict, str2_dict)




def main(): 

    print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
    print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
    print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
    print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
    print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")    


if __name__ == "__main__":
    main()



# UNIT TESTING 
# count_characters test
assert(count_characters("Hello World Hello World Hello World") == {'h': 3, 'e': 3, 'l': 9, 'o': 6, 'w': 3, 'r': 3, 'd': 3})
assert(count_characters("This is a test") == {'t': 3, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 1})
print("test for count_characters passed")

# compare_dictionaries test
test_dict1 = {'h': 3, 'e': 3, 'l': 9, 'o': 6, 'w': 3, 'r': 3, 'd': 3}
test_dict2 = {'o': 6, 'e': 3, 'l': 9, 'd': 3, 'h': 3, 'r': 3, 'w': 3}
test_dict3 = {'f': 5, 'z': 3, 'r': 4}

# testing the same dictionary
assert(compare_dictionaries(test_dict1, test_dict1) == True)

# testing the same dictionary with different order
assert(compare_dictionaries(test_dict1, test_dict2) == True)

# testing the different dictionaries
assert(compare_dictionaries(test_dict1, test_dict3) == False)
print("test for compare_dictionaries passed")