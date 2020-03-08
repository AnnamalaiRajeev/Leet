class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i, number in enumerate(nums):
            if hash_map.get(number, False) is False:
                hash_map[number] = [i]
            else:
                hash_map[number].append(i)

        for i in range(len(nums)):
            number_to_search = target - nums[i]
            if hash_map.get(number_to_search, False) is not False:
                print("oyou")
                print(hash_map.get(number_to_search))
                if number_to_search == nums[i]:
                    if len(hash_map.get(number_to_search)) == 2:
                        return [hash_map.get(number_to_search)[0], hash_map.get(number_to_search)[1]]
                else:
                    return [i, hash_map.get(number_to_search)[0]]

    def twoSum_1(self,nums,target): # one pass
        hash_map ={}
        for i, number in enumerate(nums):
            if hash_map.get(number, False) is False:
                compliment = target - number
                if compliment in hash_map:
                    return i, hash_map[compliment][0]
            else:
                compliment = target - number
                if compliment in hash_map:
                    return i, hash_map[compliment][0]
                hash_map[number] = [i]









