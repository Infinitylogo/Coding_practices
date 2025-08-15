# checking the number is palindrome or not ??
# approach ::--

"""
121>>

last_digit = 121 % 10   → 1  (remainder)
rev = (0 * 10) + 1      → 1
num = 121 // 10         → 12 (quotient)

AGAIN >>

last_digit = 12 % 10    → 2
rev = (1 * 10) + 2      → 12
num = 12 // 10          → 1

AGAIN>>

last_digit = 1 % 10     → 1
rev = (12 * 10) + 1     → 121
num = 1 // 10           → 0

"""

def palindrome(num):
    temp = num 
    pal = 0

    while temp != 0:
        # get the 
        ld = temp %10
        pal = pal *10 +ld
        temp //= 10

    if num == pal :
        return True 
    else:
        return False
    
print(palindrome(121))
print(palindrome(1221))
print(palindrome(12128))
