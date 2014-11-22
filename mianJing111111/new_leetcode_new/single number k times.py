# encoding=utf-8
'''
@1337c0d3r has a great answer. But here is a better version to understand and extend.

public class Solution {
    public int singleNumber(int[] A) {
        if (A == null) return 0;
        int x0 = ~0, x1 = 0, x2 = 0, t;
        for (int i = 0; i < A.length; i++) {
            t = x2;
            x2 = (x1 & A[i]) | (x2 & ~A[i]);
            x1 = (x0 & A[i]) | (x1 & ~A[i]);
            x0 = (t & A[i]) | (x0 & ~A[i]);
        }
        return x1;
    }
}

The general version of the question would be:

    Given an array of integers, every element appears k times except for one. Find that single one who appears l times.

We need a array x[i] with size k for saving the bits appears i times. For every input number a, generate the new counter by x[j] = (x[j-1] & a) | (x[j] & ~a). Except x[0] = (x[k] & a) | (x[0] & ~a).

In the equation, the first part indicates the the carries from previous one. The second part indicates the bits not carried to next one.

Then the algorithms run in O(kn) and the extra space O(k).

public class Solution {
    public int singleNumber(int[] A, int k, int l) {
        if (A == null) return 0;
        int t;
        int[] x = new int[k];
        x[0] = ~0;
        for (int i = 0; i < A.length; i++) {
            t = x[k-1];
            for (int j = k-1; j > 0; j--) {
                x[j] = (x[j-1] & A[i]) | (x[j] & ~A[i]);
            }
            x[0] = (t & A[i]) | (x[0] & ~A[i]);
        }
        return x[l];
    }
}


'''