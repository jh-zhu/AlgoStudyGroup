# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Time 65.09%
Memory 67.09%

Remember to update the result pointer itself
'''


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def divide(lists,start,end):
            if start == end:
                return lists[start]
            mid = start + int((end-start)/2)
            left = divide(lists,start,mid)
            right = divide(lists,mid+1,end)
            return merge(left,right)

        def merge(left,right):
            l = left
            r = right
            res = p = ListNode(0) #dummy node
            # as long as there is one element
            while( l or r):
                if not l:
                    p.next = r
                    break
                if not r:
                    p.next = l
                    break
                else:
                    if l.val <= r.val:
                        p.next = l
                        l = l.next
                    else:
                        p.next = r
                        r = r.next
                    p = p.next
            return res.next
        return divide(lists,0,len(lists)-1) if lists else []
