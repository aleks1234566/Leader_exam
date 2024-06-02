def nearest_sq(n):
    root = int(n ** 0.5)
    lower_square = root * root
    upper_square = (root + 1) * (root + 1)
    
    if (n - lower_square) <= (upper_square - n):
        return lower_square
    return upper_square

print(nearest_sq(int(input())))