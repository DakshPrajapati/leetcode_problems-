class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        minOps = [float("inf")] * n
        minOps[0] = 0  # already have 1 A

        for idx in range(n):
            currentChars = idx + 1

    

            # Copy currentChars once, then paste repeatedly
            targetChars = currentChars * 2
            pasteCount = 1

            while targetChars <= n:
                targetIdx = targetChars - 1

                minOps[targetIdx] = min(
                    minOps[targetIdx],
                    minOps[idx] + 1 + pasteCount
                )

                pasteCount += 1
                targetChars += currentChars

        return minOps[n - 1]