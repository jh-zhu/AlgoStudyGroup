import collections


'''
Recursive Implementation
Time 83.98%
Memory 6.12% (Memory consuming becasue you need to build calls on stack)
'''

class Solution:
    def preorderTraversal(self, root: TreeNode) -> "List[int]":
        self.ans = []
        self.preOrder(root)
        return self.ans

    def preOrder(self,root):
        if root is None:
            return
        self.ans.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)


'''
Recursive Implementation (Divide and Conquer)
Time 19.70%
Memory 6.12%
'''

class Solution:
    def preorderTraversal(self,root:TreeNode) -> "List[int]":
        return self.preOrder(root)

    def preOrder(self,root):
        if root is None:
            return []
        return [root.val]+ self.preOrder(root.left) + self.preOrder(root.right)

'''
Iterative Implementation
Time 37.05%
Memory 6.12%
'''
import collections


class Solution:
    def preorderTraversal(self,root:TreeNode) -> "List[int]":
        s = collections.deque()
        ans = []
        p = root

        while p is not None or s:
            if p is not None:
                ans.append(p.val)
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                p = p.right
        return ans
