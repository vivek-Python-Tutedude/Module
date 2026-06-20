'''
recursion is a process in which a function call itself till a certain condition is not met

There are 2 parts to any recursive function
1. Base /terminal condition
2. recrsive condition

'''
# factorial = n ==> n * (n - 1) * (n - 1) * ..... * (2 * 1)
# 4! ==> 4 * 3 *  2 * 1

# without recursion
  
def fact(n) :
    fac = 1
    while n > 1 :
        fac *= n
        n = n - 1
    return fac

print(f"factorial of 4 is = {fact(4)}")

# with recursion

def fact(n) :
    if n == 1:
        return 1
    else :
        fac = n * fact(n - 1)
        return fac
    
print(f"factorial of 5 is = {fact(5)}")
