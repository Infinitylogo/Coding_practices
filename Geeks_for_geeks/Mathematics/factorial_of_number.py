# finding factorial of a number

"""
5  = 5*4*3*2*1

Edge case:-- 
if 1 = 1
#should number start from 1>>
"""
# Two approch either iterate from 2 to end and multipy each one 
# or use recursion for that case 
# using iteration method saves space but time complexity will be same>>

# first approach >>
# iteration appraoch time complexity O(n) and space is O(1)
def fact(num):
    res = 1

    for i in range(2, num+1):
        res *= i

    return res

# recursion approach :-- O(n) and O(n) (requires stack space for each calls)

def fact_recursion(num):
    if num == 0: # base conditon 
        return 1
    return num*fact_recursion(num-1)

# print(fact(5))
# print(fact(10))
print(fact_recursion(5))
print(fact_recursion(10))