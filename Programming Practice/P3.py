import csv


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
receiving_numbers=[]

def mcl(calls): 
    

    
    
    m=len(calls)
    n=len(calls[0])
    
    for row in range(m):
        for column in range(n):
            if '(080)'in calls[row][0]:
                if calls[row][1] not in receiving_numbers:
                    receiving_numbers.append(calls[row][1])
    
    # sorted_number=sorted(receiving_numbers,key=len)
    
    # for i in range(len(sorted_number)):
    #     print(sorted_number[i])
    
    return receiving_numbers



    
    
            

print(mcl(calls))
