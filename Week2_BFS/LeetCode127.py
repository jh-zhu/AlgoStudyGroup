from collections import deque

'''
Time 37.71%
Memory 26.91%
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord,1))

        # speed up using set
        wlist = set(wordList)

        # begin to process our queue
        while q:
            word,step = q.popleft()
            if word == endWord:
                return step
            # if not equal, transform
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nword = word[:i]+c+word[i+1:]

                    if nword in wlist:
                        q.append((nword,step+1))
                        # prevent we go back to a phase we were already there
                        wlist.remove(nword)
        return 0
