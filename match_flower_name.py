# Write your code here
# HINT: create a dictionary from flowers.txt

def create_flowers_dictionary(filename):
    flowers_dictionary = {}
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename, 'r') as f:
        for line in f:
            flowers_dictionary[line[:line.find(':')]] = line[line.find(' ') + 1:line.find('\n')]
            
    return flowers_dictionary
def main():
    flowers_dictionary = create_flowers_dictionary('flowers.txt')

    name = input("Enter your First [space] Last name only: ")

    if name[:1] in flowers_dictionary:
        print("Unique flower name with the first letter: {}".format(flowers_dictionary[name[:1]]))

if __name__ == "__main__":
    main()