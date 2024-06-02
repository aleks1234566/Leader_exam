def repeats(arr):
     
    for i in arr[:]:
        if i == 1:
            arr.remove(i)
            return sum(arr)
            
print(repeats([1,1,2,3,45,344]))