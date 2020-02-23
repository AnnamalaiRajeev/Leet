class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) == 0:
            return nums
        i = 0
        count = 0
        while i != (len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                count += 1
            i += 1
        print("count",count)
        if count == len(nums) - 1:
            nums.sort()
            return nums
        j = len(nums)-1
        for i in range(len(nums)):
            print(j)
            if nums[j] > nums[j - 1]:
                position = j - 1
                print("position",position)
                for i in range(position, len(nums)):
                    print("i", i)
                    print("nums[i] -->{}, nums[position]-->{}".format(nums[i], nums[position]))
                    if nums[i] < nums[position] or i == len(nums)-1:
                        if i == len(nums)-1 and nums[i] > nums[position]:
                            x = i
                        else:
                            x = i - 1
                        print("yo",nums[x],nums[position])
                        nums[x],nums[position] = nums[position], nums[x]
                        nums[position+1:] = reversed(nums[position+1:])
                        print(nums)
                        break
                break
            j -= 1
        return nums


obj = Solution()
y = obj.nextPermutation([1,3,2])
print(y)
    
# 2 1 3
