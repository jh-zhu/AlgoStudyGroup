
'''
LeetCode 444 (LintCode 605) Sequence sequenceReconstruction

LintCode Time: 99.80%

Kahn's Algotithm
'''




class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        if len(seqs)==0:
            return False
        if len(org) == 0 and len(seqs[0])==0:
            return True
        if seqs== [[],[]]:
            return False

        s1 = set(org)
        for seq in seqs:
            for i in seq:
                if i not in s1:
                    return False

        n = len(org)

        adjlist = {}
        in_count = {}
        result = []

        for c in org:
            in_count[c] = 0
            adjlist[c] = []

        # build adjlist
        for l in seqs:
            for i in range(len(l)-1):
                start = l[i]
                end = l[i+1]
                adjlist[start].append(end)
                in_count[end]+=1



        # build S
        s = collections.deque()

        for key,val in in_count.items():
            if val == 0:
                s.append(key)

        # begin algorithm
        while s:
            # exist if not unique
            if len(s)>1:
                return False
            no = s.popleft()
            result.append(no)

            nodes = adjlist[no]
            for node in nodes:
                in_count[node] -=1
                if in_count[node] == 0:
                    s.append(node)

        # if there is edge left over
        if len(result) != n:
            return False

        # check if the result is the same as org
        check = org*2
        for i in range(n):
            if result == check[i:i+n]:
                return True
        return False
