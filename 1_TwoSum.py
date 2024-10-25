# class Solution:
#     def twoSum(self, nums, target):
#         result = []
#         for index in range(len(nums)):
#             for_find_nums = nums[:index] + nums[index+1:]
#             num_find = target-nums[index]
#             if num_find in for_find_nums:
#                 result = [index, for_find_nums.index(num_find)+1]
#                 break
        
#         return result

# sol = Solution()

# print(sol.twoSum([3,3], 6))

class Solution:
    def twoSum(self, nums, target):
        hash_nums = {num: i for i, num in enumerate(nums)}
        for i in range(len(nums)):
            if target-nums[i] in hash_nums and i != hash_nums[target-nums[i]]:
                return [i, hash_nums[target-nums[i]]]
        return []