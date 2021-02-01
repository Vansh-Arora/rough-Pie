class Solution:
    def hammingWeight(self, n: bytes) -> int:
        return bin(n).count('1')