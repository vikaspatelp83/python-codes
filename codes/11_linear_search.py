list = list(map(int,input("enter numbers :").split()))
num = int(input("enter number:"))
for i in list:
    if i == num:
        print(i,"found at position",list.index(i)+1)

