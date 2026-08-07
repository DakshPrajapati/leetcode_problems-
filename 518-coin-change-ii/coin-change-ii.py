class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sol = [0 for _ in range(amount+1)]
        sol[0] = 1
        coins = set(coins)

        for c in coins:
            for i in range(c, amount+1):
                sol[i] += sol[i-c]

        return sol[-1]