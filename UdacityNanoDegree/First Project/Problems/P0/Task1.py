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


"""                        My Thought precess

--> There are two columns,both in texts and calls, that contain the number.So if I multiply 
the length of lists by two I should get total of the phone numbers in every record.

-- > so,  number of telepone numbers:
    
    in texts-file = 2*len(texts)
    in calls-file = 2* len(calls)
    
-- > Adding the above outputs should provide the total

"""

print('there are ',2*len(texts)+2*len(calls),'different telephone numbers in the records')

