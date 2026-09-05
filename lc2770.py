class Solution:
    #dp solution
    def maximumJumps_dp(self, nums: List[int], target: int) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if dp[j] == 0:
                    continue
                if -target <= nums[j] - nums[i] <= target:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return dp[-1] - 1


    #segment tree solution
    def maximumJumps(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(set(nums))
        segment_tree = SegmentTree(len(nums), float('-inf'))

        idx = self.find_idx(sorted_nums, nums[0])
        segment_tree.update(idx, 0)
        for i in range(1, len(nums)):
            l, h = nums[i] - target, nums[i] + target
            l_idx = self.find_low_idx(sorted_nums, l)
            h_idx = self.find_high_idx(sorted_nums, h)

            if l_idx is None or h_idx is None or l_idx > h_idx:
                continue

            res = segment_tree.find(l_idx, h_idx)
            if res == float('-inf'):
                continue

            if i == len(nums) - 1:
                return res + 1
            else:
                idx = self.find_idx(sorted_nums, nums[i])
                segment_tree.update(idx, res + 1)
        
        return -1

    def find_idx(self, sorted_nums, num):
        #first index where value >= num
        m = l = 0
        h = len(sorted_nums)
        while l < h:
            m = (l + h) // 2
            if sorted_nums[m] < num:
                l = m + 1
            else:
                h = m
        return l
    
    def find_low_idx(self, sorted_nums, num):
        idx = self.find_idx(sorted_nums, num)
        #left boundary greater already no answer lies there
        if idx == len(sorted_nums):
            return None
        return idx

    def find_high_idx(self, sorted_nums, num):
        idx = self.find_idx(sorted_nums, num)
        #if exactly num
        if idx < len(sorted_nums) and sorted_nums[idx] == num:
            return idx
        #right boundary smaller already no answer lies there
        if idx == 0:
            return None
        #if not then its greater, so - 1
        return idx - 1


class SegmentTree:
    def __init__(self, ln, fill):
        import math
        self.ln = ln
        tree_len = 2 ** math.ceil(math.log2(ln))
        self.tree = [fill] * (2 * tree_len)

    def find(self, l, h):
        return self._find(1, 0, self.ln - 1, l, h)
    
    def update(self, i, val):
        self._update(1, 0, self.ln - 1, i, val)

    def _find(self, node, cl, ch, l, h):
        if (h < cl or l > ch):
            return float('-inf')

        if (l <= cl and ch <= h):
            return self.tree[node]

        m = (cl + ch) // 2
        return max(self._find(node * 2, cl, m, l, h), self._find(node * 2 + 1, m + 1, ch, l, h))

    def _update(self, node, cl, ch, i, val):
        m = (cl + ch) // 2
        if cl == ch:
            #store max for duplicates
            self.tree[node] = max(self.tree[node], val)
            return

        if m < i:
            self._update(2 * node + 1, m + 1, ch, i, val)
        else:
            self._update(2 * node, cl, m, i, val)

        self.tree[node] = max(self.tree[node], val)
    
    def print(self):
        print("================ TREE ================")
        print()
        q = deque([1])
        while q:
            levelcnt = len(q)
            for _ in range(levelcnt):
                node = q.popleft()
                if node >= len(self.tree):
                    continue
                print(self.tree[node], end = " ")
                q.append(node * 2)
                q.append(node * 2 + 1)
            print()
        print("======================================"

