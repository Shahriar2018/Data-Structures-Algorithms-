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

"""                             PART A                                        """

#  Set of calls receieved from Bangalore
denominator=0
numerator=0
#Bangalore numbers that received calls from bangalore

area_code=list()
receiving_numbers=list()




# =============================================================================
#  Functions that list all the phone numbers that received a call from bangalor (areacode (080))
#     
# =============================================================================

def mcl(calls): 
    m=len(calls)
    global denominator
    global receiving_numbers
    
    for row in range(m):      
            if '(080)'in calls[row][0]:
                receiving_numbers.append(calls[row][1])
                
    denominator=len(receiving_numbers)
    #Total number of calls  made from bangalore 
    
    return return_sorted(receiving_numbers)

# =============================================================================
# Function That returns the area codes
# =============================================================================


def return_sorted(data):
    global area_code
    global numerator


    for i in range(len(data)):
        
        if '('  in data[i]:
            area_code.append(data[i][data[i].index('('):data[i].index(')')+1])
            
        elif '140'in data[i][:3]:
            area_code.append('140')
        
        
        elif '7'or '8' or '9'== data[i][0][:1]:
            area_code.append(data[i][:4])
            
    numerator=area_code.count('(080)')
    # Number calls  made to a number also starting with "(080)"
            
        
        
    area_code=set(area_code)
    area_code=sorted(list(area_code))
    
    for i in range(len(area_code)):
        print(area_code[i])
        
                
    return ''
                
      


print("The numbers called by people in Bangalore have codes:")

mcl(calls)





"""
                            PART B

"""
fraction=float((numerator/denominator)*100)
percent="{:.2f}".format(fraction)




print('\n',percent,"percent of calls from fixed lines in Bangalore are calls"+
" to other fixed lines in Bangalore.")