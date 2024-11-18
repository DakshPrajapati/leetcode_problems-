class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = int(right/2 if right%2==0 else (right//2)+1)
        if nums[mid] == target:
                return mid
        while left < right:
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] > nums[left]:
                if nums[mid] >= target and nums[left] <= target:
                    right = mid - 1
                    mid = int((left+right)/2 if (left+right)%2==0 else (left+right)//2+1)
                else:
                    left = mid + 1
                    mid = int((left+right)/2 if (left+right)%2==0 else (left+right)//2+1)
            elif nums[mid] < nums[right]:
                if nums[mid] <= target and nums[right] >= target:
                    left = mid + 1
                    mid = int((left+right)/2 if (left+right)%2==0 else (left+right)//2+1)
                else:
                    right = mid - 1
                    mid = int((left+right)/2 if (left+right)%2==0 else (left+right)//2+1)
            else:
                break
        return -1