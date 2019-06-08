'''
Time 86.16%
Memory 97.83%

Kahn's Algorithm 

'''



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for i in range(numCourses)]
        in_count = [0 for i in range(numCourses)]
        count = 0

        # build adjlist
        for l in prerequisites:
            start = l[1]
            end = l[0]
            adjlist[start].append(end)
            in_count[end]+=1

        # build S
        s = collections.deque()
        for i in range(len(in_count)):
            if in_count[i] == 0:
                s.append(i)
        # begin algorithm
        while s:
            no = s.popleft()
            count+=1

            nodes = adjlist[no]
            for node in nodes:
                in_count[node] -=1
                if in_count[node] == 0:
                    s.append(node)
        return True if count == numCourses else False
