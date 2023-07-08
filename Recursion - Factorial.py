def Factorial(Integer):
    if Integer == 1:
        Result = 1
    else:
        Result = Integer * Factorial(Integer-1)
    return Result


print(Factorial(4))
