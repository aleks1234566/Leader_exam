def isValid(formula):
   if 1 in formula and 2 not in formula:
      return True
   if 2 in formula and 1 not in formula:
      return True
   if 1 in formula and 2 in formula:
      return False
   if 3 and 4 in formula:
      return False
   if 3 in formula and 4 not in formula:
      return False
   if 3 not in formula and 4 in formula:
      return True
   if 5 in formula and 6 in formula:
      return True
   if 5 in formula and 6 not in formula:
      return False
   if 6 in formula and 5 not in formula:
      return False
   if 7 in formula or 8 in formula:
      return True
   
print(isValid([1,2,3,4]))