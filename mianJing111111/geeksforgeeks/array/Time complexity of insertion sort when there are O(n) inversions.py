# encoding=utf-8
'''
What is an inversion?
Given an array arr[], a pair arr[i] and arr[j] forms an inversion if arr[i] < arr[j] and i > j. For example, the array {1, 3, 2, 5} has one inversion (3, 2) and array {5, 4, 3} has inversions (5, 4), (5, 3) and (4, 3). We have discussed a merge sort based algorithm to count inversions

What is the time complexity of Insertion Sort when there are O(n) inversions?
Consider the following function of insertion sort.
/* Function to sort an array using insertion sort*/
void insertionSort(int arr[], int n)
{
   int i, key, j;
   for (i = 1; i < n; i++)
   {
       key = arr[i];
       j = i-1;

       /* Move elements of arr[0..i-1], that are
          greater than key, to one position ahead
          of their current position */
       while (j >= 0 && arr[j] > key)
       {
           arr[j+1] = arr[j];
           j = j-1;
       }
       arr[j+1] = key;
   }
}

If we take a closer look at the insertion sort code, we can notice that every iteration of while loop reduces one inversion.

The while loop executes only if i > j and arr[i] < arr[j]. Therefore total number of while loop iterations (For all values of i) is same as number of inversions.

Therefore overall time complexity of the insertion sort is O(n + f(n)) where f(n) is inversion count.

 If the inversion count is O(n), then the time complexity of insertion sort is O(n).

In worst case, there can be n*(n-1)/2 inversions. The worst case occurs when the array is sorted in reverse order. So the worst case time complexity of insertion sort is O(n2).

Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above
'''

# 每次 arr[j] > key  是一个inversion.     . 于是确定内部循环进行O(n)次。  于是是O（n）