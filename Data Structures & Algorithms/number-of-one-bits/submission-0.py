class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_n = bin(n)[2:]
        count = 0 
        for i in binary_n:
            if i == '1':
                count+=1 

        return count