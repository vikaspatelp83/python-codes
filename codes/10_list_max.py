def find_max(list_):
    max = list_[0]

    for num in list_:
        if num>max:
            max = num
    return max

lst = list(map(int,input("enter numbers :").split()))

print(find_max(lst))