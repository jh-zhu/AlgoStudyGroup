

'''
Time 79.07%
Memory 5.97%

'''


import collections

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # do a inorder Travesal
        ans = TreeNode(None)
        p_a = ans
        s = collections.deque()
        p = root

        while p is not None or s:
            if p is not None:
                s.append(p)
                p = p.left
            else:
                p = s.pop()

                # build a tree
                if p_a.val is None:
                    p_a.val = p.val
                else:
                    p_a.right = TreeNode(p.val)
                    p_a = p_a.right

                p = p.right
        return ans
