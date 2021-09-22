def again(x, value = 0):
        if x<=0:
            return value
        value = value*10 + (x%10) 
        return again(x//10, value)
def reverse(x: int) -> int:
    if x>-10 and x<10:      #if x is 1 digit number
        return x

    else:
        sign = True         #to retain sign of the number
        if x<0:
            sign = False    #False means it's negative
            x*=-1   

        x = again(x)   #calling recursive function

        if x>=(2**-31) and x<(2**31):       #SIGNED INTEGER Condition
            return x if sign else -1*x

        else:
            return 0
