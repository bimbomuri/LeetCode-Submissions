class Solution:
    def addBinary(self, a: str, b: str) -> str:
        val = str(bin(int(a,2) + int(b,2)))
        
        return val[2:]
        