# Check if an array is sorted and rotated
class Solution:
    def check(self, nums) -> bool:
        n=len(nums)
        if n==1:
            return True
        count=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:  #logic to check for rotation of array
                count=count+1
        if count<=1:
            return True
        else:
            return False
        
ob=Solution()
print(ob.check([3,4,5,1,2]))
print(ob.check([2,1,3,4]))
print(ob.check([1,2,3]))
print(ob.check([1,1,1]))