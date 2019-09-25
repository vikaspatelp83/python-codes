nums = list(map(int,input("enter numbers ").split(" ")))
max = nums[0]
for num in nums:
    if num>max:
        max = num

print("max = ",max)