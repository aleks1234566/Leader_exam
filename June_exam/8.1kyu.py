def divisible_by(numbers, divisor):
    return [n for n in numbers if n % divisor == 0]



print(divisible_by([1,2,3,4,5,6], int(input())))