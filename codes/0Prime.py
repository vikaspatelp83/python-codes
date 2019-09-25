def prime(n):
    p = 0
    for i in range(1,n+1):
        if n%i == 0:
            p = p+1
    return p



if __name__ == "__main__":
    num = int(input("enter how many prime numbers you want: "))
    count = 0
    p = 0
    i = 1
    while(count < num):
        p = prime(i)
        if p == 2:
            print(count+1,"->",i,"is prime ")
            count += 1
        i = i + 1



