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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# I have chosen set as my data collection because for this case the order does't matter, Set holds unique hashable object like strings.

phones_set = set(texts, calls)
for line in texts:
    phones_set.add(line[0])
    phones_set.add(line[1])

for line in calls:
    phones_set.add(line[0])
    phones_set.add(line[1])

print(len(phones_set))