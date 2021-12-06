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
# get first record of texts
incoming_number, answering_number, time  = texts[0]
print("First record of texts, {} texts {} at time {}".format(incoming_number, answering_number, time))

# get last record of calls
incoming_number, answering_number, time, duration  = calls[0]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming_number, answering_number, time, duration))

"""
Big O:
O(1) -- no matter how the input change, the execution is constant time
"""
