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
phone_number=dict()

def longest_call(calls):
    
    
    
    global phone_number
    
    for row in range(len(calls)):
        
        key1=calls[row][0] #calling numbers
        key2=calls[row][1] #Receiving numbers
        value=int(calls[row][3])
        
        if key1  in phone_number and key2 not in phone_number:
            phone_number[key1]=phone_number[key1]+value
            
        if key2 in phone_number and key1 not in phone_number:
            phone_number[key2]=phone_number[key2]+value 
            
        if key1 in phone_number and key2  in phone_number:
            phone_number[key1]=phone_number[key1]+value
            phone_number[key2]=phone_number[key2]+value 
            
        if key1 not in phone_number and key2 not in phone_number:
            phone_number[key1]=value
            phone_number[key2]=value
        
                      
    return phone_number

longest_call(calls)

max=sorted(phone_number.values(),reverse=True)[0]

def get_key (value):
    for key,value in phone_number.items():
        if value==max:
            return key


max_phone=get_key(max)

print(max_phone,"spent the longest time,",max,"seconds,"+
      "on the phone during September 2016."
      )

