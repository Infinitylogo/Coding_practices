class Soluton:

    def get_factorial(self, n):
        if n == 0:
            return 1
        
        return n * self.get_factorial(n-1)
    
    def count_digits(self, n):
        count =0
        while n > 0:
            n //= 10 # quotient
            count +=1

        return count 
    
    def digits_of_factorial(self, n):
        digits = self.count_digits(self.get_factorial(n))
        return digits
    
# v = Soluton()
# print(v.digits_of_factorial(5))




# time limit issue in above cases >>
# further optimsed solution using the math lib

import math

def factdigits(n):
    if n==0 or n ==1:
        return 1
    log_sum =0
    for i in range(2, n+1):
        log_sum += math.log10(i)

    print(math.floor(log_sum)+1)

# factdigits(5)

# More optimised solution here is :-- Kamenetsky’s formula (calculating the digits of factorial integer)

import math

def usign_formula(n):
    if n < 2:
        return 1
    
    x = n* math.log10(n/math.e) +math.log10(2*math.pi*n) /2
    return math.floor(x)+1


print(usign_formula(5))