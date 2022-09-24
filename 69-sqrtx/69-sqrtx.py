class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        y = []
        x = int(x)
        while x > 0 :
            x = x-i
            i += 2
            y.append(i)
            if x - i < 0:
                break
        return len(y)       
        