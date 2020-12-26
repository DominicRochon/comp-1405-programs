def lucas(n):
    if n < 2:
        return [2,1][n]
    else:
        return lucas(n-1) + lucas(n-2)

print(lucas(5))