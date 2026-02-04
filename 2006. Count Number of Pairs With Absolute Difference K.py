nums=[1,2,2,1]
k=1
count=0
for i in range(len(nums)):
    for x in range(len(nums)):
        if nums[i]-nums[x]==k:
            count+=1
print(count)