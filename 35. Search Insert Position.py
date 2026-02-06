nums_1=[1,3,5,6]
target_1=7
def searchInsert(nums,target):
    if target not in nums:
        nums.append(target)
        nums.sort()
    for i in range(len(nums)):
        if nums[i]==target:
            return i

        
print(searchInsert(nums_1,target_1))