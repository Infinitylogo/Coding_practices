# count digits of a number
# two ways to do that, either using mathematics or converting in string and check the total char.


# string one is simple will do mathematics one >>


def count_digits(num):
    res = 0
    while num > 0 :
        num = num//10 
        res +=1
    return res 

#checking 
print(count_digits(100987))

## time complexity :-- O(d) # d is the number of diglits 
## space :-- O(1)



