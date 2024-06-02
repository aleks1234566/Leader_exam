def nearest_sq(n):
      for num in range(n + 1):
            if(num+ 1) ** 2 >= n:
                break
      return  int(n ** (0.5)) ** 2

print(nearest_sq(int(input())))