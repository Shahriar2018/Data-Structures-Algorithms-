

matrix=[[12,9,10,5],[3,7,18,6],[1,2,3,3],[4,5,6,2]]
emp=[]

def mcl(matrix): 
    
    
    m=len(matrix)
    n=len(matrix[0])
    
    for row in range(m):
        for column in range(n):
            emp.append(matrix[row][column])
            
    return emp

print(mcl(matrix))
m=max(emp)
print(m)
print(emp.index(m))

    

