'''
Time 86.95%
Memory 99.43%

Similar to 207, Kahn's Algorithm

'''



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for i in range(numCourses)]
        in_count = [0 for i in range(numCourses)]
        result = []

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
            result.append(no)

            nodes = adjlist[no]
            for node in nodes:
                in_count[node] -=1
                if in_count[node] == 0:
                    s.append(node)
        return result if len(result)==numCourses else []
