def parts_sums(ls):
     sums = [sum(ls)]
     for part in ls:
        sums.append(sums[-1]-part)
     return sums

print(parts_sums([1,2,3,4,5,6,7,8,9,10]))