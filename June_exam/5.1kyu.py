def solution(array_a, array_b):
     new_list = []
     for x in range(len(array_a)):
        new_list.append(abs(array_a[x] - array_b[x]))
     new_list = list(map(lambda x : x ** 2, new_list))
     finished = sum(new_list) // len(new_list)
     return finished


print(solution([1, 2, 3], [4, 5, 6] ))