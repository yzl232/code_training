class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        result = maxN = minN = A[0]
        for i in range(1, len(A)):
            a = maxN; b = minN
            maxN = max(b * A[i], a * A[i], A[i])
            minN = min(b * A[i], a * A[i], A[i])
            result = max(result, maxN)
        return result