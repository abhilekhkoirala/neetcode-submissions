class Solution:
    def countBits(self, n: int) -> List[int]:
        retr_arr = [0]*(n+1)

        for i in range(1, n+1):
            if i%2 ==0:
                retr_arr[i] = retr_arr[i//2]
            else:
                retr_arr[i] = retr_arr[i//2] + 1

        return retr_arr

