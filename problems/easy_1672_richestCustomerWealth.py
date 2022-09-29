class Solution(object):
    def maximumWealth(self, accounts):
        sumAmounts = map(lambda x: sum(x), accounts)
        richestCustomer = max(sumAmounts)
        return richestCustomer
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        