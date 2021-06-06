
a=[45,39,40,23,21,21,14,90,78,100,90,54]

def mylist(a) :
    for i in range(len(a)):
        j=i+1
        for j in range(len(a)):
            if a[i]>a[j]:
                temp=a[j]
                a[j]=a[i]
                a[i]=temp
    return(a)
    
print(mylist(a))
                
