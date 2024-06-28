def min_sum(arr):
    sum = 0
    arr.sort()
    
    for i in range(len(arr) // 2):
        sum += arr[i] * arr[-(i + 1)]
    return sum


print(min_sum([1,2,3,4,5,6,7]))
