a,b,c = map(int,input("Enter 3 values (space separated):").split())
if a>b and a>c:
    print("{} is greater".format(a))
elif b>c:
    print("{} is greater".format(b))
else:
    print("{} is greater".format(c))
