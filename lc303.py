class NumArray:

    def __init__(self, nums):
        self.sums = [0] * (len(nums) + 1)
        
        for x in range(1, len(nums) + 1):
            self.sums[x] = self.sums[x - 1] + nums[x - 1]
        
        print(self.sums)


        

    def sumRange(self, left: int, right: int) -> int:
    	return self.sums[right + 1] - self.sums[left]
	

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


x = NumArray(nums=[1,2,3,4])

print(x.sumRange(0,3))
