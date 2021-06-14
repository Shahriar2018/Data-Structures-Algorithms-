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
receiving_numbers=[]
code=[]

# =============================================================================
# Function That returns the area codes
# =============================================================================


def return_sorted(data):


    for i in range(len(data)):
        if '('  in data[i]:
            s1=data[i].split('(')
            s2=s1[1].split(')')
            if s2[0] not in code:
                code.append(s2[0])
        elif data[i][:3]=='140' and '140' not in code:
            code.append('140')
        else :
            s1=data[i].split()
            if s1[0] not in code:
                code.append(s1[0])
                
    area_code=sorted(code)
    
    for j in range(len(area_code)):
         print(area_code[j])
        
        
                
    return ''
                
      
# =============================================================================
#  Functions that list all the phone numbers that received a call from bangalor (areacode (080))
#     
# =============================================================================

def mcl(calls): 
    

    
    
    m=len(calls)
    n=len(calls[0])
    
    for row in range(m):
        for column in range(n):
            if '(080)'in calls[row][0]:
                if calls[row][1] not in receiving_numbers:
                    receiving_numbers.append(calls[row][1])
    
    
    return return_sorted(receiving_numbers)

print("The numbers called by people in Bangalore have codes:")

mcl(calls)





"""
                            PART B

"""

# =============================================================================
# Function that return percentage
# 
# =============================================================================
def return_percentage(data):
    denominator=len(data)
    numerator=0

    for i in range(len(data)):
        if '('  in data[i]:
            if data[i][1:4]=='080':          
                numerator=numerator+1
    
    result=float((numerator/denominator)*100)        
    
                
    return "{:.2f}".format(result)
# =============================================================================
# Functions that list all the phone numbers that received a call from bangalore (areacode (080))
# =============================================================================
bangalore_numbers=[]

def make_list(calls): 
    

    
    
    m=len(calls)
    n=len(calls[0])
    
    for row in range(m):
        for column in range(n):
            if '(080)'in calls[row][0]:
                if calls[row][1] not in bangalore_numbers:
                    bangalore_numbers.append(calls[row][1])  
    
    return return_percentage(bangalore_numbers)


print('\n',make_list(calls),"percent of calls from fixed lines in Bangalore are calls"+
" to other fixed lines in Bangalore.")