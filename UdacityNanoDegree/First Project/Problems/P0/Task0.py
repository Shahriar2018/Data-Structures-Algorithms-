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

"""                                 My Solution                          """


"""                      Sequence of operation                

1) Found lenght of list first: len(texts)=9072 and len(calls)= 5213

2) Ran type(texts[0]) and type(calls[0]) and learned that texts and calls are lists of lists


"""
print('First record of texts <incoming number>',texts[0][0],'<answering number>',texts[0][1],
      'at the time',texts[0][2][11:])

print('Last record of calls <incoming number>',calls[5212][0],'<answering number>',calls[5212][1],
      'lasting',calls[5212][3], "seconds")

