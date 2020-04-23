# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            temp = target - num
            if temp in hashmap:
                return [hashmap[temp], index]
            hashmap[num] = index
        return None

    def twoSum(self, nums, target):
        n = len(nums)
        for x in range(n):
            for y in range(x + 1, n):
                if nums[x] + nums[y] == target:
                    return [x, y]
                    break
                else:
                    continue


if __name__ == "__main__":
    x = 4
    a = [1, 2, 3]
    s = Solution()
    print(s.twoSum1(a, 4))


# leetcode submit region end(Prohibit modification and deletion)
