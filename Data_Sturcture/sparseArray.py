def matchingStrings(strings, queries):
    countsList=[]
    
    for j in queries:
        count = 0 
        for i in strings:
            if j == i:
                count +=1
        countsList.append(count)
    return(countsList)
