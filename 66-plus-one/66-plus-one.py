class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(''.join(str(i) for i in digits)) 
        digits = digits + 1
        y = []
        for x in str(digits):
            y.append(x)
            
            
        return y
           