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

make_calls = []
send_receive_texts = []
receive_calls = []
telemarketers = []

# store all number that sending or receiving the texts

for r in texts:
    if r[0] not in send_receive_texts:
        send_receive_texts.append(r[0])
    if r[1] not in send_receive_texts:
        send_receive_texts.append(r[1])

# store all calling out number and receiver numbers
for r in calls:
    if r[0] not in make_calls:
        make_calls.append(r[0])
    if r[1] not in receive_calls:
        receive_calls.append(r[1])

# check if number in calling_out not in texts_receiver, save it to telemarketers
for number in make_calls:
    if (number not in send_receive_texts) & (number not in receive_calls):
        telemarketers.append(number)

telemarketers.sort()

print("These numbers could be telemarketers: \n")
for number in telemarketers:
    print(number)

"""
Suggestion:
outgoing = set()
non_tele = set()

for call in calls:
    outgoing.add(call[0])
    non_tele.add(call[1])

for call in texts:
    non_tele.add(call[0])
    non_tele.add(call[1])

# subtract all non_tele number from outgoing
tele = outgoing.difference(non_tele)

# display the result line by line in sorted order

"""
