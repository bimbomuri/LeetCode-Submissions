class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        y = int(s[::-1])
        
        if y > 2147483647:
            return 0
      
        return y if x > 0 else(y * -1)
        