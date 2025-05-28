class Solution:
    def numberOfAlternatingGroups(self, colors) -> int:
        cnt = 0
        r = 0
        while r < len(colors):
            if colors[r] == colors[r - 1]:
                r += 1
            elif colors[r] == colors[r - 2]:
                cnt += 1
            r += 1
        
        return cnt






x = Solution()
print(x.numberOfAlternatingGroups(colors = [0,1,0,0,1]))
        
