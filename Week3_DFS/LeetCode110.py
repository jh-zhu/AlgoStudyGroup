'''
Time 31.76%
Memory 45 %

The inefficiency I found is that for each node, we need
to calculate the height again, which is time consuming ans wasty
'''



class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        balanced = True if abs(self.height(root.left)-self.height(root.right))<2 else False
        return balanced and self.isBalanced(root.left) and self.isBalanced(root.right)




    def height(self,root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))
