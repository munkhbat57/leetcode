class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        ans = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                ans.append(1)
            else:
                ans.append(0)
        return ans