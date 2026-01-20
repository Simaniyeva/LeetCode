nums=[2,4,3,8]
for i in range(1,len(nums)):
    nums[i]=nums[i-1]+nums[i]
print(nums)
    