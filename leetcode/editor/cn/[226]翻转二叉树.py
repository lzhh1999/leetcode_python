# 翻转一棵二叉树。 
# 
#  示例： 
# 
#  输入： 
# 
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9 
# 
#  输出： 
# 
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1 
# 
#  备注: 
# 这个问题是受到 Max Howell 的 原问题 启发的 ： 
# 
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。 
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left = self.invertTree1(root.left)
        right = self.invertTree1(root.right)
        root.left = right
        root.right = left
        return root

    def invertTree(self, root):
        if not root:
            return None
        queue = [root]
        while queue:
            curr = queue.pop()
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root

# leetcode submit region end(Prohibit modification and deletion)
