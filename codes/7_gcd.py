def gcd(a,b):
    # choose the least number
    if a > b:
        least = b
    else:
        least = a
    for i in range(1, least + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i #or hcf

    return gcd


print(gcd(11,22))