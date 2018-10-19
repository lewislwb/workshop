def twoSum(nums, target):
        m=0
        for i in nums:
            a=target-i
            if a in nums and nums.index(a) != m:
                return [m,nums.index(a)]
            else:
                m+=1
                
        return 0
        

print(twoSum([1,2,3,4,5,6,7,8],15))
