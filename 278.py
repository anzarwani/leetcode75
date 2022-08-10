class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        
        while high > low:
            mid = (low+high)//2
            
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
                
        return low
                
        
        
        
