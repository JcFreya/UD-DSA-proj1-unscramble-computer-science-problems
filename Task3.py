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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
# create list to save codes
import re
codes = []

for r in calls:
    # check if the caller is from Bangalore
    if '(080)' in r[0]:
        # check if the receiver is fixed number
        if "(" in r[1]:
            receiver_number = r[1]
            # print(receiver_number)
            start = receiver_number.find("(") + len("(")
            end = receiver_number.find(")")
            code = receiver_number[start:end]

            if code not in codes:
                codes.append(code)
        # check if the receiver is mobile number
        elif r[1][0] in ['7','8','9']:
            prefix = r[1][0:4]
            if prefix not in codes:
                codes.append(prefix)

# sort the list
codes.sort()
print("The numbers called by people in Bangalore have codes:\n ")
for code in codes:
    print(code)

"""
Big O:
O(nlogn) -- since using sort() function which makes the complexity to nlogn
"""

# Part B
cnt_caller = 0
cnt_receiver = 0
# check if caller from Bangalore has receiver from Bangalore
for r in calls:
    # check if the caller is from Bangalore
    if '(080)' in r[0]:
        cnt_caller += 1
        if '(080)' in r[1]:
            cnt_receiver += 1

pct = round(cnt_receiver/cnt_caller*100.00, 2)
print("{} percent of calls from fixed lines in Bangalore are calls\
to other fixed lines in Bangalore.".format(str(pct)))

"""
Big O:
O(n) -- the complexity depends on length of input files
"""
