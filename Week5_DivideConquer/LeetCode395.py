import collections
import re

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = collections.Counter(s)
        # find chars appear less than K, as seperator
        sep = [c for c in cnt if cnt[c] < k]

        # end condition
        if not sep:
            return len(s)

        # split string
        subs = re.split('|'.join(sep),s)

        return max(self.longestSubstring(sub,k) for sub in subs)
