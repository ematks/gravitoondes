def nextPowerOf2(n: int):
    """
    This function returns the closest power of 2 bigger than n

    If the entered int is negative, returns 0 to show miscontent
    """
    if n<0:
        print("The entered integer is negative. Cannot compute next opxer of 2")
        return 0
    power = 0
    while n != 0:
        power += 1
        n = n // 2

    return power

x = -0.5
print(nextPowerOf2(x), 2**(nextPowerOf2(x)-1),2**nextPowerOf2(x))