nums=[5,8,9]
target=int(input())
for i in range(len(nums)):
    for x in range(i+1,len(nums)):
        if target==nums[i]+nums[x]:
            print(nums[i],nums[x])
            print(i,x)
        else:
            continue
        