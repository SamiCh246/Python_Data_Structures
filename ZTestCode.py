def printt(n):
    if n <= 0:
        return 0
    if n == 1:
        return 2
    return printt(n-1) + printt(n-2)

print(printt(6))