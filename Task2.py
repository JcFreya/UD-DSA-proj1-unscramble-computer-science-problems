"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# create a dictionary to store the phone number and total time
time_spent = {}
for r in calls:
    # store the caller info
    number = r[0]
    time = int(r[3])
    if number in time_spent:
        time_spent[number] += time
    else:
        time_spent[number] = time

    # store the receiver info
    number = r[1]
    time = int(r[3])
    if number in time_spent:
        time_spent[number] += time
    else:
        time_spent[number] = time

# print(time_spent)
# print(time_spent.items())
sorted_time = sorted(time_spent.items(), key=lambda item: item[1], reverse=True)
# print(sorted_time)

longest_number = sorted_time[0][0]
longest_time = sorted_time[0][1]

print("{} spent the longest time, {} seconds, on the phone during\
September 2016.".format(longest_number, longest_time))

"""
Suggestion:
can utilize the .get() method to optimize code.
To get the longest/maximum time spent, can also use the max() built-in function instead of sorted().
This will reduce the overall worst-case time complexity to O(n).

for call in calls:
    time_spent[call[0]] = time_spent.get(call[0],0) + int(call[3])
    time_spent[call[1]] = time_spent.get(call[1],0) + int(call[3])

longest_number = max(time_spent, key=lambda k: time_spent[k])
longest_time =time_spent[longest_number]
"""
