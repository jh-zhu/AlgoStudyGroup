# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Solution 1
Time: 76.29%
Memory: 9.71%
'''

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        # initialize
        S = deque([root])
        res = []
        while S:
            curr_level = []
            # how many nodes in this level
            n = len(S)
            for i in range(n):
                V = S.popleft()
                curr_level.append(V.val)
                # check left
                if V.left:
                    S.append(V.left)
                # check right
                if V.right:
                    S.append(V.right)

            # current level done
            res.append(curr_level)
        return res

'''
Solution 2
Time 76.29% same 44ms
Memory 10.2%
'''

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        S = [root]
        res=[]

        while S:
            res.append([s.val for s in S])
            S = [node for s in S for node in (s.left,s.right) if node]
        return res
