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

# create a list to save unique number
numbers = []

# check each recors if the number is in numbers list
for r in texts:
    if r[0] not in numbers:
        numbers.append(r[0])
    if r[1] not in numbers:
        numbers.append(r[1])

for r in calls:
    if r[0] not in numbers:
        numbers.append(r[0])
    if r[1] not in numbers:
        numbers.append(r[1])

cnt = len(numbers)

print("There are {} different telephone numbers in the records.".format(str(cnt)))

"""
Option2:
Using sets
unique_tele_nums = set()
for call in calls:
    unique_tele_nums.add(call[0])
    unique_tele_nums.add(call[1])
for call in texts:
    unique_tele_nums.add(call[0])
    unique_tele_nums.add(call[1])
cnt = len(unique_tele_nums)
"""
