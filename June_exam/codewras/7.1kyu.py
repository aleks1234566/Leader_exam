def capitalize(s):
    s1, s2 = " ", " "  
    for char, letter in enumerate(s):
        if char % 2 == 0:
            s1 += letter.upper()
            s2 += letter
        else:
            s1 += letter
            s2 += letter.upper()
    return [s1, s2]

print(capitalize(input()))