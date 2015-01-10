# encoding=utf-8
#Implement memcpy(void* src, void* dst, int len)
class Solution:
    def memcpy(self, dst, src, n):
        if not dst or not src: return
        for i in range(n):
            dst[i] = src[i]