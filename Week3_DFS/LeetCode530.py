
'''
Time 99.48% (happy on that)
Memory 5.17%

The key point is that an inorder traversal of a BST is in inorder
Therefore, the minimum difference is between adjacent value in an
inroder traversal
'''


import collections

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        prev = float('inf')
        ans = float('inf')
        p = root
        s = collections.deque()

        # do an inorder traversal
        while p is not None or s:
            if p is not None:
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                ans = min(ans,abs(prev-p.val))
                prev = p.val
                p = p.right
        return ans
