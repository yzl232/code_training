# encoding=utf-8


'''
给你一个有序数组 和一个X 让你返回数组里所有满足a + b <= X的 tuple。  follow up： 换成 a, b, c三元  满足 a+ b+ c <= X  大概的方法签名如下： int xxxxxx(int[] array, int X)

如果是求个数，可以做到O(n)
'''




'''
when A[start] + A[end] > X, end--;
when A[start] + A[end] <= X, we know A[start] can be paired with every element from A[start+1] to A[end]. so we add (end- start) to our final result, then start++.
'''