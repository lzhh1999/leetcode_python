# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  示例 1: 
# 
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "rat", t = "car"
# 输出: false 
# 
#  说明: 
# 你可以假设字符串只包含小写字母。 
# 
#  进阶: 
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 排序 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution(object):
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for sh in s:
            d[sh] = d.get(sh, 0) + 1
        for th in t:
            d[th] = d.get(th, 0) - 1
            if d[th] < 0:
                return False
        return True

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d = [0] * 26
        for i in range(len(s)):
            d[ord(s[i]) - ord('a')] += 1
            d[ord(t[i]) - ord('a')] -= 1
        for i in d:
            if i != 0:
                return False
        return True

    def isAnagram4(self, s, t):
        return Counter(s) == Counter(t)
# leetcode submit region end(Prohibit modification and deletion)
