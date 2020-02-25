class Solution(object):
    def findDuplicates_1(self, nums):  # O(n) # extra space
        hash_nums = {}
        list_return = []
        for num in nums:
            if hash_nums.get(num, False):
                list_return.append(num)
            else:
                hash_nums[num] = 1

        return list_return

    def find_duplicates_1(self, nums): # O(n) # No extra space
        nums.sort()
        lister = []
        i = 0
        j = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[j]:
                lister.append(nums[i])
            j += 1
        return lister

    def find_duplicates_2(self,nums):    # O(n) # No extra space # using reference logic
        retur_ = []
        for i in range(len(nums)):
            if abs(nums[nums[i]-1]) < 0:
                retur_.append(nums[i])
            else:
                nums[nums[i]-1] = -1 * nums[nums[i]-1]
        return retur_


obj = Solution()
print(obj.find_duplicates_2([4,3,2,7,8,2,3,1]))

