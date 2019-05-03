'''
Time 14.62%
Memory 12.16%
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        adj = {}
        # adjacency list
        for i in range(n):
            adj[i] = set()
        for edge in edges:
            i,j = edge[0],edge[1]
            adj[i].add(j)
            adj[j].add(i)

        # find leaves
        leaves = []
        for key,item in adj.items():
            if len(item) == 1:
                leaves.append(key)
        # prune trees
        while(n>2):
            n = n - len(leaves)

            for leaf in leaves:
                adj[adj[leaf].pop()].remove(leaf)
                del adj[leaf]

            #update leaves
            leaves = [key for key,leaf in adj.items() if len(leaf)<=1]
        return leaves

'''
@Author Bingchu Huang
https://github.com/bingchuhuang

time 93.06%
memory 18.92%

Difference from my implementation. Use a list to maintain
adjacency list instead of dictionary.
Using a liitle bit more memory, but significant faster than my implmentation
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        adj = [set() for _ in range(n)]
        # adjacency list
        for edge in edges:
            i,j = edge[0],edge[1]
            adj[i].add(j)
            adj[j].add(i)

        # find leaves
        leaves = []
        leaves = [i for i in range(n) if len(adj[i])==1 ]

        # prune trees
        while(n>2):
            n = n - len(leaves)

            new_leaves = []
            for leaf in leaves:
                j = adj[leaf].pop()
                adj[j].remove(leaf)

                #update leaves
                if len(adj[j])==1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
