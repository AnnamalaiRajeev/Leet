class Solution():
    def threeSum(self, nums):
        hash_map = {}
        for i, num in enumerate(nums):
            if hash_map.get(num, False) is False:
                hash_map[num] = 0
            else:
                hash_map[num] += 1
        count = 0
        solution_set = []
        for i, value in enumerate(nums):
            for j in range(i+1, len(nums)):
                sum = value+nums[j]
                if -1*sum in hash_map:
                    print(value, nums[j], -1*sum)
                    print(nums[j:])
                    count+=1
                    solution_set.append([value, nums[j], -1*sum])
        for i, array in enumerate(solution_set):
            array.sort()
        print(set(solution_set))

        return solution_set

    def threeSum_1(self, nums):
        nums.sort()  # sort the list i.e [-1,-1,0,1,2,3]
        hash_map = {}
        solution_Set = []
        print(nums)
        for i, num in enumerate(nums):  # create hash_map of hasharray with keys as numbers and array with indices
            if num in hash_map:
                hash_map[num].append(i)
            else:
                hash_map[num] = []
        a = 0
        while nums[a] <= 0 and a <= len(nums)-3:  # a is negative
            if a > 0:
                while nums[a] == nums[a-1] and a <= len(nums)-3:
                    a += 1

            window_end = len(nums) - 1
            window_start = a+1
            for i in range(a + 1, len(nums)):
                if a == 2:
                    #print("window_start, window_end", nums[window_start], nums[window_end])
                    pass
                if window_start == window_end:
                    break
                if nums[a] + nums[window_start] + nums[window_end] == 0:
                    print("match hit for {} {}".format(nums[a], [[nums[a], nums[window_start], nums[window_end]]]))
                    solution_Set.append([nums[a], nums[window_start], nums[window_end]])
                if -1 * nums[a] < nums[window_start] + nums[window_end]:  # then decrement window_end
                    window_end -= 1
                else:
                    window_start += 1

            a += 1
        return solution_Set

    def threeSum_2(self, nums):
        if len(nums) <= 2:  # take care of base case
            return []
        nums.sort()  # sort the list i.e [-1,-1,0,1,2,3]
        hash_map = {}
        solution_Set = []
        a = 0
        while nums[a] <= 0 and a <= len(nums) - 3:  # a is negative
            if a > 0 and  nums[a] == nums[a - 1]:   # loop to skip same values that are adjacent to each other ex [-1, -1, ...]
                a += 1
                continue
            window_end = len(nums) - 1
            window_start = a + 1
            for i in range(a + 1, len(nums)):
                if window_start == window_end:
                    break
                if window_start > a+1 and nums[window_start] ==nums[window_start-1]: # for window start to skip same values that are adjacent to each other ex [-1, -1, ...]
                    window_start += 1
                    continue
                if window_end < (len(nums)-1) and nums[window_end] == nums[window_end+1]:  # for window end to skip same values that are adjacent to each other ex [-1, -1, ...]
                    window_end -= 1
                    continue
                if nums[a] + nums[window_start] + nums[window_end] == 0:
                    print("match hit for index- ->{} {} {},  {} {}".format(a,window_start,window_end, nums[a], [[nums[a], nums[window_start], nums[window_end]]]))
                    solution_Set.append([nums[a], nums[window_start], nums[window_end]])
                if -1 * nums[a] < nums[window_start] + nums[window_end]:  # then decrement window_end
                    window_end -= 1
                else:
                    window_start += 1

            a += 1
        return solution_Set



obj = Solution()
y = obj.threeSum_2([0,0,0,1,0,0,0,-1,0,0,0,0,1])
print(y)


