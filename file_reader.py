f = open('my_file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)


f = open('my_file.txt', 'w')
f.write("Hello there!")
f.close()


with open('my_file.txt', 'r') as f:
    file_data = f.read()
    print(file_data)