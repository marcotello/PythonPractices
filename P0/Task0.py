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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# printing first record of texts
# Getting the data from the frist record in the texts list by fixed position. 
# This code has O(4) complexity because the code is executing approximately 4 instructions
print("First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2]))

# printing last record of calls
# Getting the data from the frist record in the calls list by accesisng the last item in the list (the pythonic way).
# This code has O(4) complexity because the code is executing approximately 4 instructions
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))
