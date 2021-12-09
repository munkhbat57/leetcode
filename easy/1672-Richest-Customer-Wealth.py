class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for customer in accounts:
            cus_sum = sum(customer) 
            if cus_sum > max:
                max = cus_sum
        return max