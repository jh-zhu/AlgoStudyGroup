'''
Time 91.15%
Memory 20.78%
'''


class Solution:
    m = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathHelper(root)
        return self.m

    def maxPathHelper(self,root):
        if root is None:
            return 0

        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        max_root = max(left,right,left+right,0) + root.val

        if max_root > self.m:
            self.m = max_root


        # adds to uper level node
        return max(left,right,0) + root.val
