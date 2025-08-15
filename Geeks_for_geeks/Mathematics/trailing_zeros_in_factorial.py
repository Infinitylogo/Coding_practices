### count all the trailing zeros in factorial case 
"""
Such as 

for 5 == 120 is the factorial, and the trailing zero is 1

so for other cases need to calculate the trailing zeros here >>

# Approach >>

use 5 :: divide the number by 5 and keep counting it, will give the overall count 

"""


def count_trailing_zeros(n):

    if n < 0: # case for negative number
        return -1
    
    count = 0

    i = 5

    while n//i >=1:
        count += n//i
        i *=5

    return count 

n =100
print(count_trailing_zeros(n))


    
