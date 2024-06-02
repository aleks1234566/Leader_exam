def repeats(arr):
    sum = 0
    
    for num in arr:
        if arr.count(num) == 1:
            sum += num
    
    return sum

print(repeats([1,1,1,33,4,5]))