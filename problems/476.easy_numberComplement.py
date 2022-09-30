#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, nums: int) -> int:
        nums = str(bin(nums))[2:]
        revNums = list(map(lambda num: "0" if num=="1" else "1", nums))
        revNums = "".join(revNums)
        return int(revNums, 2) 
# @lc code=end
