# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def ds(root, mi, ma):
            if root == None:
                return True
            if root.val <= mi or root.val >= ma:
                return False
            return ds(root.left, mi, root.val) and ds(root.right, root.val, ma)

        return ds(root, float("-inf"), float("inf"))

    def isValidBST2(self, root):
        stack = []
        curr = root
        temp = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if temp and temp.val >= curr.val: return False
            temp = curr
            curr = curr.right
        return True

    def isValidBST(self, root):
        self.pre = None

        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            return isBST(root.right)

        return isBST(root)

# leetcode submit region end(Prohibit modification and deletion)
