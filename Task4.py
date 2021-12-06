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

calling_out = []
texts_receiver = []
telemarketers = []

# store all number that sending or receiving the texts
for r in texts:
    if r[0] not in texts_receiver:
        texts_receiver.append(r[0])
    if r[1] not in texts_receiver:
        texts_receiver.append(r[1])

# store all calling out number and receiver numbers
for r in calls:
    if r[0] not in calling_out:
        calling_out.append(r[0])
    if r[1] not in texts_receiver:
        calling_out.append(r[1])

# check if number in calling_out not in texts_receiver, save it to telemarketers
for number in calling_out:
    if number not in texts_receiver:
        telemarketers.append(number)

print("These numbers could be telemarketers: \n")
for number in telemarketers:
    print(number)

"""
Big O:
O(n) -- all for loops depend on the size of input files
"""
