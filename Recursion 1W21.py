def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return Unknown(X + 1, Y) * 2
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return Unknown(X - 1, Y) // 2


def Unknown2(X, Y):
    Total = 1
    while X != Y:
        print(X + Y)
        if X < Y:
            X = X + 1
            Total = Total * 2
        else:
            X = X - 1
            Total = Total//2
    return Total


print(Unknown(15, 10))
print(Unknown2(10, 15))
