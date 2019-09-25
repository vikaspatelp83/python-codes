def exponential(base,number):
    if number == 1:
        return number
    else:
        return number**base

b = int(input("enter base :"))
n = int(input("enter number :"))

print(exponential(b,n))
