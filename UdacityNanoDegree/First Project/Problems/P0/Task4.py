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

print("These numbers could be telemarketers: ")


telemarketers=[]

def telemarketers_list(calls): 
    

    
    
    m=len(calls)
    n=len(calls[0])
    
    for row in range(m):
        for column in range(n):
            if '140'in calls[row][0][:4]:
                if calls[row][0] not in telemarketers:
                    telemarketers.append(calls[row][0])
                    
    telemarketers1=sorted(telemarketers)
    for j in range(len(telemarketers1)):
        print(telemarketers1[j])
    
   
    
    return ""


telemarketers_list(calls)
