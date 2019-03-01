def hourglassSum(arr):
    result = 0
    list_totals = []
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            result = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            list_totals.append(result) # list of all the hourglassSum 
            
    return max(list_totals)    # largest hourglassSum in arr
