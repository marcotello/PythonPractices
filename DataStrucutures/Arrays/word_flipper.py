def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # New empty string for us to build on
    new_string = ""

    # Iterate over old string
    for i in range(len(our_string)):
        # Grab the charecter from the back of the string and add them to the new string
        new_string += our_string[(len(our_string)-1)-i]

    # Return our solution
    return new_string

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    # TODO: Write your solution here
    our_string_splitted = our_string.split()
    reversed = ""

    for word in our_string_splitted:
        reversed = reversed + " " + string_reverser(word)

    return reversed.strip()


    # Test Cases

print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")