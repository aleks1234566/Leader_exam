def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower()) 


print(is_anagram(input(), input()))