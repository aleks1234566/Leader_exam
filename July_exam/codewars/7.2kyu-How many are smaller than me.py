def smaller(arr):
    new_list = []
    for num in range(len(arr)):
        a = 0
        for z in arr[num:]:
            if arr[num] > z:
                a += 1
        new_list.append(a)
    return new_list

print(smaller[5,2,3])