def power(x, y, p) :
    res = 1
    x = x % p

    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % p
        y = y//2
        x = (x * x) % p
    return res




x = int(input("x:")); y = int(input("y:")); p = int(input("p:"))
print("Power is ", power(x, y, p))
