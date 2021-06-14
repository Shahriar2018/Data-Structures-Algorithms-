import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


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

print(telemarketers_list(calls))