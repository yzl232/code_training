#给一个数列和一个目标数， 返回目标数出现的次数，数列已经排序
def find_times(arr,target):
	left=0;right=len(arr)-1
	while left<=right:
		mid=(left+right)/2
		if arr[mid]==target:
			newleft=0;newright=mid-1
			while newleft<=newright:
				newmid=(newleft+newright)/2
				if arr[newmid]==target:
					newright=newmid-1
				else:
					newleft=newmid+1
			index1=newleft
			newleft=mid+1;newright=len(arr)-1
			while newleft<=newright:
				newmid=(newleft+newright)/2
				if arr[newmid]==target:
					newleft=newmid+1
				else:
					newright=newmid-1
			index2=newleft
			return (index1,index2)
		elif arr[mid]<target:
			left=mid+1
		else:
			right=mid-1
	return 0
#二树， 打印层次顺序的节点 (level order traversal)
def level_order(root):
	def traverse(root,level):
		if root:
			if len(res)<level+1:res.append([])
			res[level].append(root.val)
			traverse(root.left,level+1)
			traverse(root.right,level+1)
	res=[]
	traverse(root,0)
	return res
def level_order(root):
	res=[]
	if root is None:return res
	res=[[root.val]]
	nodes=[root]
	while True:
		nums=[]
		newnodes=[]
		for i in nodes:
			if i.left:
				newnodes.append(i.left)
				nums.append(i.left.val)
			if i.right:
				newnodes.append(i.right)
				nums.append(i.right.val)
		nodes=newnodes
		res.append(nums)
		if nodes is None:
			break
	return res
#给一个字符串只由一，零和星组成， 返还一组数， 把星替换成1和2
def replace_star(str):
	def dfs(start,str):
		if start==len(str):
			res.append(str)
			return
		if str[start]=='1' or str[start]=='0':
			dfs(start+1,str)
		else:
			dfs(start+1,str[:start]+'1'+str[start+1:])
			dfs(start+1,str[:start]+'2'+str[start+1:])
	res=[]
	dfs(0,str)
	return res
#有n个tuple 比如 ["a","b","c"] ["red","blue"]....要求生成 从每个tuple中取一个string构成的所有组合 比如 ["a","red"] ["b","blue"].....
def generate_comb(tuples):
	def dfs(start,currlist):
		if len(currlist)==len(tuples):
			if currlist not in res:
				res.append(currlist)
			return 
		for i in range(len(tuples[start])):
			if i>0 and tuples[start][i]==tuples[start][i-1]:
				continue
			dfs(start+1,currlist+[tuples[start][i]])
	res=[]
	dfs(0,[])
	return res
#给一个String的array，问如何移除重复的string (hashmap,bst)
def remove_duplicate_str(strArr):
	strDict={}
	newlength=0
	for i in range(len(strArr)):
		if strDict.has_key(strArr[i]):
			pass
		else:
			strArr[newlength]=strArr[i]
			newlength+=1
			strDict[strArr[i]]=1
	return strArr[:newlength]
#binary tree的max height
def tree_max_height(root):
	if root is None:
		return 0
	return 1+max(tree_max_height(root.left),tree_max_height(root.right))
#给一个integer的array，按照n1<=n2>=n3<=n4>=n5 的order排序。
#A[0]<=A[1]>=A[2]<=A[3] shuffle
#coding:
#u = [u1, u2, u3, u4, u5, u6, …] (integers)
#s = [s1, s2, s3, s4, s5, s5, …]
#s1 <= s2, s2 >=s3, s3 <= s4, s4 >= s5,.....
def wried_order(arr):
	flag=True
	for i in range(1,len(arr)):
		if (not flag and arr[i-1]<arr[i]) or (flag and arr[i-1]>arr[i]):
			arr[i-1],arr[i]=arr[i],arr[i-1]
		flag=not flag
	return arr
#fibonacci为啥不用recursive。分别的时间复杂度。空间复杂度，包含函数栈上的。
#revursive n! or n (memorize or not)
def fib(n):
	if n<2:return 1
	f0=1;f1=1;f2=f0+f1
	for i in range(2,n+1):
		f2=f1+f0
		f0=f1
		f1=f2
	return f2
#sorted array有正有负如何按顺序输出平方值 (binary search,然后两边扫)
def output_square(arr):
	res=[]
	index=-1
	left=0;right=len(arr)-1
	while left<=right:
		mid=(left+right)/2
		if arr[mid]==0:
			index=mid
			break
		elif arr[mid]<0:
			left=mid+1
		else:
			right=mid-1
	if index==-1:index=left
	lp=index-1;rp=index
	while lp>=0 and rp<len(arr):
		if arr[rp]*arr[rp]<arr[lp]*arr[lp]:
			res.append(arr[rp]*arr[rp])
			rp+=1
		else:
			res.append(arr[lp]*arr[lp])
			lp-=1
	while lp>=0:
		res.append(arr[lp]*arr[lp])
		lp-=1
	while rp<len(arr):
		res.append(arr[rp]*arr[rp])
		rp+=1
	return res
#给一个BST，找第k个元素(inorder traversal or heap)
def find_k(root,k):
	count=0
	def inorder(root):
		if root:
			inorder(root.left)
			if count==k:return root.val
			count+=1
			inorder(root.right)
	return inorder(root)
def find_k1(root,k):
	stack=[]
	count=0
	while stack or root:
		if root:
			stack.append(root)
			root=root.left
		else:
			root=stack.pop()
			if count==k:
				return root.val
			count+=1
			root=root.right
#一个led 矩阵[1..m,1..n] 设计函数set/reset 第[i,j]位 ， 主要用到的是bit 的按位操作.(set or(00000100) reset and (1111110)
def set_matrix(matrix,i,j):
	setbits=1<<(j-1)
	matrix[i]|=setbits
def reset_matrix(matrix,i,j):
	setbits=~(1<<(j-1))
	matrix[i]&=setbits
#在地址栏输入url address后整个过程
'''
CTCI
'''
#1枚硬币，来选择出1-3的数字（比如3部电影，选出看哪一部）如果投到0，那再投一次，那么就有0-7 8个数字，那么可以：
#1-2 -》1.
#3-4 -》2
#5-6 -》3
#0-7 -》再投一次 
#LRU Cache
class Node:
    def __init__(self,val,key):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class DList:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_first(self,newNode):
        if self.head is None and self.tail is None:
            self.head=newNode;self.tail=newNode
            return
        self.head.prev=newNode
        newNode.next=self.head
        self.head=newNode
    def remove(self,newNode):
        if self.head is None and self.tail is None:
            return
        if self.head==self.tail and self.head==newNode:
            self.head=self.tail=None
        elif self.head==newNode:
            self.head.next.prev=None
            self.head=self.head.next
        elif self.tail==newNode:
            newNode.prev.next=None
            self.tail=newNode.prev
        else:
            newNode.prev.next=newNode.next
            newNode.next.prev=newNode.prev
            newNode.next=newNode.prev=None
    def remove_last(self):
        self.remove(self.tail)
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.size=0
        self.capacity=capacity
        self.dlist=DList()
        self.dataDict={}
    # @return an integer
    def get(self, key):
        if self.dataDict.has_key(key):
            self.dlist.remove(self.dataDict[key])
            self.dlist.add_first(self.dataDict[key])
            return self.dataDict[key].val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.dataDict.has_key(key):
            self.dlist.remove(self.dataDict[key])
            self.dataDict[key].val=value
            self.dlist.add_first(self.dataDict[key])
        else:
            if self.size==self.capacity:
                del self.dataDict[self.dlist.tail.key]
                self.dlist.remove_last()
                self.dataDict[key]=Node(value,key)
                self.dlist.add_first(self.dataDict[key])
            else:
                self.dataDict[key]=Node(value,key)
                self.dlist.add_first(self.dataDict[key])
                self.size+=1
#数一个区间内的平方数，根号N
def find_square(a,b):
	return int(b**(1/N))-int(a**(1/N))
def find_square(a,b,n):
	index1=-1;index2=-1
	pointer=0
	while pointer**n<a:
		pointer+=1
	index1=pointer
	while pointer**n<b:
		pointer+=1
	index2=pointer
	return index2-index1+1
#写一个程序判断两个单词是否可以通过一次字母对调变成一样的。扩展问题是判断两个单词是否可以通过若干次字母对调变成一样的
def one_replace1(str1,str2):
	if str1==str2:return False
	if len(str1)!=len(str2):return False
	p1=0;p2=0;diff=0;index1=None;index2=None
	diff=0
	while p1<len(str1) and p2<len(str2):
		if str1[p1]==str2[p2]:
			pass
		else:
			if not index1 and not index2:
				index1=str1[p1]
				index2=str2[p2]
			else:
				if index1!=str2[p2] or index2!=str1[p1]:
					return False
				else:
					diff+=1
			p1+=1;p2+=1
	return diff==1
def one_replace(str1,str2,n):
	if str1==str2:return False
	if len(str1)!=len(str2):return False
	diff=0
	numDict={};indexDict={}
	for i in range(len(str1)):
		if str1[i] not in numDict:
			numDict[str1[i]]=1
		else:
			numDict[str1[i]]+=1
		if str1[i] not in indexDict:
			indexDict[str1[i]]=[i]
		else:
			indexDict[str1[i]].append(i)
	for i in range(len(str2)):
		if str2[i] not in numDict:
			return False
		else:
			numDict[str2[i]]-=1
			if numDict[str2[i]]<0:
				return False
		isDiff=True
		for j in indexDict[str2[i]]:
			if j==i:
				isDiff=False
				break
		if isDiff:
			diff+=1
	return diff==n*2
'''
2 player game
- there’s a set of marbles
- take turns removing 1 or 2
- winner removes the last one

- you get decide who goes first
如果轮到我选择球的时候， 我会胜利的要求是当我选择以后，留给对手的球他输了我就能赢，只要他无论怎样都赢了， 我就输了。 比如我现在手里有 i个球， 我只能选择两个球或者一个球， 留给对手的就是i-1 或 i-2 个球。 假设D＝ true or false 表示我当前能否赢。 
那么DP表达式为D = !D[i-1] || !D[i-2];
basic case为 D[1] = true; D[2] = true; 因为无论怎样都可以拿1个或两个球
最后true为我先拿
'''
def get_ball(n):
	dp=[False for x in range(n+1)]
	dp[1]=True;dp[2]=True
	for i in range(3,n+1):
		dp[i]=(not dp[i-1]) or (not dp[i-2])
	return dp[-1]
#找一个普通的二叉树里的最大元素
def find_max_inTree(root):
	def inorder(root):
		if root:
			inorder(root.left)
			currmax=max(currmax,root.val)
			inorder(root.right)
	def inorder1(root):
		stack=[]
		while stack or root:
			if root:
				stack.append(root)
				root=root.left
			else:
				root=stack.pop()
				currmax=max(currmax,root.val)
				root=root.right
	currmax=-2147483648
	inorder(root)
	return currmax
#Reverse linkedlist
def reverse_linkedlist(head):
	if head is None or head.next is None:return head
	dummy=ListNode(0);dummy.next=head
	while head and head.next:
		newnext=head.next
		head.next=newnext.next
		dummy.next=newnext
		newnext.next=head
	return dummy.next
#给一个文本，输出其中所有的bi-gram的次数。比如a b c b c就是“a b”1次，"b c"2次，“c b”1次。如果要按顺序输出就再走一遍
def bi_gram(strs):
	bidict={};res=[]
	for i in range(2,len(strs)+1):
		if strs[i-2:i] not in bidict:
			bidict[strs[i-2:i]]=1
		else:
			bidict[strs[i-2:i]]+=1
	for i in range(2,len(strs)+1):
		if strs[i-2:i] not in bidict:
			continue
		else:
			res.append((strs[i-2:i],bidict[strs[i-2:i]]))
			del bidict[strs[i-2:i]]
	return res
#给一array integer用神马数据结构如何实现insert 和lookup，最后讨论用unordered_set
#find Y(Y is between A[]的最大最小值) 使min(|Y-Ai|)最大,sort后两个相邻的数相减，然后取最大的除2
def find_max_abs(arr):
	arr.sort()
	currmax=-2147483648
	for i in range(1,len(arr)):
		currmax=max(currmax,arr[i-1]-arr[i])
	return currmax/2
#hashtable collision的概率 http://preshing.com/20110504/hash-collision-probabilities/
#给一个n个node的BST，给一个Key，返回与key最接近的m个node(m<N). 
def find_closet(root,key):
	def inorder(root):
		if root:
			inorder(root.left)
			res.append(root.val)
			inorder(root.right)
	res=[]
	inorder(root)
	index1=-1;index2=-1
	left=0;right=len(res)-1
	while left<=right:
		mid=(left+right)/2
		if res[mid]==key:
			index1=mid-1;index2=mid
			break
		elif key<res[mid]:
			right=mid-1
		else:
			left=mid+1
	if index1==-1 and index2==-1:
		index1=left;index2=left+1
	ret=[];count=0
	while count<m and index1>=0 and index2<len(res):
		if abs(res[index1]-key)<abs(res[index2]-key):
			ret.append(res[index1])
			index1-=1
		else:
			ret.append(res[index2])
			index2+=1
		count+=1
	while count<m and index1>=0:
		ret.append(res[index1])
		index1-=1
		count+=1
	while count<m and index2<len(res):
		ret.append(res[index2])
		index2+=1
		count+=1
	return ret
#给多台机器，怎么bfs？ give each machine an id, and add id to graph node
#check一个数是否是3的次幂。(integer or not)
def check_power_three(num):
	if num<=0:return False
	if num<1:return check_power_three(1/num)
	while num>1:
		strNum=str(num)
		tempSum=0
		for i in strNum:
			tempSum+=int(i)
		if tempSum%3!=0:
			return False
		tempSum/=3
		num=tempSum
	return True
#flip coin  比如一共 flip 5次，有三次 H(head) 2次 T（tail）.要求输出所有可能的组合。（generate paraenthesis, combination)
def filp_coin(head,tail):
	def dfs(currhead,currtail,currstr):
		if currhead+currtail==head+tail:
			if currhead==head and currtail==tail:
				res.append(currstr)
			return
		if currhead>head or currtail>tail:
			return
		dfs(currhead+1,currtail,currstr+'H')
		dfs(currhead,currtail+1,currstr+'T')
	res=[]
	dfs(0,0,'')
	return res
def flip_coin1(head,tail):
	def dfs(currlist,currstr):
		if len(currlist)==head+tail:
			if currlist not in res:
				res.append(currlist)
			return
		for i in range(len(currstr)):
			if i>0 and currstr[i]==currstr[i-1]:
				continue
			dfs(currlist+currstr[i],currstr[:i]+currstr[i+1:])
	coins='H'*head+'T'*tail
	res=[]
	dfs('',coins)
	return res
#第一个是有两个数组 让你求两个数组的差 比如{1,2,3,4,5,5,} {2,5}  输出就是1 3 4 5
def sorted_two_array(arr1,arr2):
	res=[]
	p1=0;p2=0
	while p1<len(arr1) and p2<len(arr2):
		if arr1[p1]<arr2[p2]:
			res.append(arr1[p1])
			p1+=1
		elif arr1[p1]==arr2[p2]:
			p1+=1;p2+=1
		else:
			res.append(arr2[p2])
			p2+=1
	while p1<len(arr1):
		res.append(arr1[p1])
		p1+=1
	while p2<len(arr2):
		res.append(arr2[p2])
		p2+=1
	return res
def unsorted_two_array(arr1,arr2):
	numDict={}
	if len(arr2)>len(arr1):return unsorted_two_array(arr2,arr1)
	for i in arr1:
		if numDict.has_key(i):
			numDict[i]+=1
		else:
			numDict[i]=1
	for i in arr2:
		if numDict.has_key(i):
			numDict[i]-=1
	res=[]
	for i in numDict:
		for j in range(numDict[i]):
			res.append(i)
	return res
#Copy List with Random Pointer
def copy_list(head):
	if head is None:return head
	if head.next is None: return ListNode(head.val)
	dummy=ListNode(0);dummy.next=head
	while head:
		tempNode=ListNode(head.val)
		oldNext=head.next
		tempNode.next=oldNext
		head.next=tempNode
		head=oldNext
	head=dummy.next
	while head:
		if head.random:
			head.next.random=head.random.next
		head=head.next.next
	newDummy=ListNode(0)
	newhead=newDummy;head=dummy.next
	while head:
		tempNode=head.next
		head.next=tempNode.next
		tempNode.next=None
		newhead.next=tempNode
		newhead=newhead.next
		head=head.next
	return newDummy.next
def copy_list1(head):
	nodeDict={}
	dummy=ListNode(0);dummy.next=head
	newDummy=ListNode(0);newhead=newDummy
	while head:
		newNode=ListNode(head.val)
		nodeDict[head]=newNode
		head=head.next
		newhead.next=newNode
		newhead=newhead.next
	head=dummy.next;newhead=newDummy.next
	while head:
		if head.random:
			newhead.random=nodeDict[head.random]
		head=head.next
		newhead=newhead.next
	return newDummy.next
#介绍utf-8的存储特点，让写一个函数判断一串byte[]是不是valid utf-8。
'''
UTF-8的编码规则很简单，只有二条：
1）对于单字节的符号，字节的第一位设为0，后面7位为这个符号的unicode码。因此对于英语字母，UTF-8编码和ASCII码是相同的。
2）对于n字节的符号（n>1），第一个字节的前n位都设为1，第n+1位设为0，后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。
'''
public static boolean isValidUTF8( byte[] input ) {

    CharsetDecoder cs = Charset.forName("UTF-8").newDecoder();

    try {
        cs.decode(ByteBuffer.wrap(input));
        return true;
    }
    catch(CharacterCodingException e){
        return false;
    }       
}
#find the pairs of words in the dictionary that have no letters in common, find one that maximizes the product of the words' lengths（给每个单词做个26位的bits，查看相交就 a&b==0。。 这样可能快点）
def max_product(strs):
	def make_bitmap(strs):
		res=[]
		for i in strs:
			bits=0
			for letter in i:
				bits|=(1<<(ord(letter)-ord('a')))
			res.append(bits)
		return res
	res=make_bitmap(strs)
	maxproduct=0
	for i in range(len(res)):
		for j in range(i+1,len(res)):
			if res[i]&res[j]!=0:
				continue
			else:
				maxproduct=len(strs[i])*len(strs[j])
	return maxproduct
#java solution
'''
1. Sort words 
2. Build a boolean 2D table where row corresponds to a letter and column to a word in the dictrionary. Mark an element[c][w] true if the word contains the word w contain letter c. 
3. Iterate over each row of the 2D table to contruct, for each letter, a set of words that do not contain the letter. 
4. Iterate over the disctionary words in decreasing order. For each word, find the intersections of the sets computed in step 3 that correspond to the letters of this word. Then, multiply the length of the current word with the largest word in the intersection. Remember the result if is greater than previous maximum. 
5. Repeat step 4 until the length of the current word is smaller than the square root of the previous maximum. 

The overall complexity is roughly O(nlogn + m * S), where m is the overall number of letters in the dictionary and S is the average size of a set computed in step 3.
'''
import java.util.Arrays;
import java.util.HashSet;
public class GetBiggestNonSharedWordMultiple {
	private final static int NUM_LETTERS = 26;

	private static int charToIndex(char ch){
		return Character.toLowerCase(ch)-'a';

	}
	public static int getBiggestMultiple (String [] words){
		int n = words.length;
		Arrays.sort(words); // O(n log n) ascending

		boolean [][] table = new boolean[NUM_LETTERS][];
		for(int i = 0; i < NUM_LETTERS; i ++) table[i] = new boolean[n];

		// O(m); m overall num of letters in input
		for(int w = 0; w < n; w++){
			String word = words[w];
			for(int i = word.length()-1; i >=0 ; i--){
				table[charToIndex(word.charAt(i))][w] = true;
			}

		}
		// O(k*n)
		HashSet<String> [] absenceSets = new HashSet[NUM_LETTERS];
		for(int i = 0; i < NUM_LETTERS; i ++) {
			HashSet<String> abSet = new HashSet<>();
			for(int w = 0; w < n; w++) {
				if(!table[i][w]) abSet.add(words[w]);
			}
			absenceSets[i] = abSet;
		}
		// O(m * AvgSetSize)
		int max = -1;
		for(int w = n-1; w >=0 ; w--){
			String word = words[w];	
			int wLen = word.length();
			if(wLen*wLen < max) break;
			if(wLen == 0){
				if(max < 0) max = 0;
				continue;
			}
			HashSet<String> currentSet = new HashSet<>();
			currentSet.addAll(absenceSets[charToIndex(word.charAt(0))]);

			for(int i =1 ; i < wLen ; i++){
				currentSet.retainAll(absenceSets[charToIndex(word.charAt(i)) ]);
			}
			int largestSize = -1;
			for(String otherWord: currentSet){
				if(otherWord.length() > largestSize) largestSize = otherWord.length();	
			}
			int mult = wLen * largestSize;
			if(mult > max) max = mult;
		}
		return max;
	}
	public static void main(String[] args) {
		String [] arr = { "hello", "world" ,"superb", "my", "mercury" };
		System.out.println(getBiggestMultiple(arr));		
	}
}
#两个 collection 的 object 问 这两个 collection 里面的东西是不是相同的。(toArray and use equals)
#问如果有一个hashmap<sol, string> map， 可否直接 map.get(str); str 是一个string。 如果不可以，怎样改才行。(修改hashmap中的hashcode()和equals())
#google suggestion 怎么实现， 我说tree存相关单词heap按搜索率存 
#String serialize(String[] a); String[] deserialize(String b); (存总长度,每个string长度)
def serialize(arrs):
	res=[]
	res.append(str(len(arrs))+'#')
	for word in arrs:
		res.append(str(len(word))+'%')
	for word in arrs:
		res.append(word)
	return ''.join(res)
def deserialize(s):
	sizeContent=s.split('#')
	length=int(sizeContent[0])
	s=s[len(sizeContent[0])+1:]
	eachSize=s.split('%')
	size=[]
	total=0
	for i in range(length):
		size.append(int(eachSize[i]))
		total+=size[i]
	content=s[len(s)-total:len(s)]
	result=[]
	for i in range(length):
		result.append(content[:size[i]])
		content=content[size[i]:]
	return result
'''
java solution
'''
import java.util.*;
public class combineStrings{
    public static void main(String[] args) {
                String[] arr = {"abc%cde", "a#aa", "haha"};
                for(String s : arr) {
                        System.out.println(s);
                }
                String result = serialize(arr);
                System.out.println(result);
                String[] newArr = deserialize(result);
                for(String s : newArr) {
                        System.out.println(s);
                }
        }
        public static String serialize(String[] arr) {-google 1point3acres
                StringBuilder sb = new StringBuilder();
                sb.append(arr.length + "#");. more info on 1point3acres.com
                for (String s : arr) {
                        sb.append(s.length() + "%");
                }
                for (String s : arr) {
                        sb.append(s);
                }
                return sb.toString();
        }
        public static String[] deserialize(String s) {
                String[] sizeAndContent = s.split("#");
                int len = Integer.parseInt(sizeAndContent[0]);
                s = s.substring(sizeAndContent[0].length()+1);
                String[] eachSize = s.split("%");
                int[] size = new int[len];
                int total = 0;
                for (int i = 0; i < len; i++) {
                        size[i] = Integer.parseInt(eachSize[i]);
                        total += size[i];
                }
                String content = s.substring(s.length() - total, s.length());
                String[] result = new String[len];
                for (int i = 0; i < len; i++) {
                        result[i] = content.substring(0, size[i]);
                        content = content.substring(size[i]);
                }
                return result;
        }
}
#integer division string 给两个int，实现小数除法，比如1/5=0.2   1/3=0.[3] 
def divide(a,b):
	result=''
	if a>=b and b==0:
		return str(a)+'/'+str(b)
	elif a>b:
		result+=str(a/b)
		result+='.'
		a=a%b
	else:
		result+='0.'
	table={}
	while True:
		a=a*10
		while a<b:
			a*=10
		mod=a%b
		if mod==0:
			result+=str(a/b)
			return result
		if mod not in table:
			a=a/b
			result+=str(a)
			table[mod]=len(result)-1
			a=mod
		else:
			index=table[mod]
			in_parenthese=result[index:]
			result=result[:index]
			if in_parenthese!='0':
				result+='('
				result+=in_parenthese
				result+=')'
				return result
#数组nums中有n个非负整数（整数用字符串表示），将它们以一定的顺序拼接，得到最小的整数。样例：n=4 nums: ["54", "546", "548", "60"] 可以拼接得到的最小整数为"5454654860"。
def mycmp(s1,s2):
	return int(s1+s2)-int(s2+s1)
def get_min_int(strArr):
	length=len(strArr)
	strArr.sort(mycmp)
	res=''
	for i in range(length):
		res+=strArr[i]
	return res
#merge interval
def merge(intervals):
	if len(intervals)<2:return intervals
	intervals.sort(key=lambda x:x.start)
	res=[];start=intervals[0]
	for i in range(1,len(intervals)):
		if start.end<intervals[i].start:
			res.append(start)
			start=intervals[i]
		else:
			start=Interval(start.start,max(start.end,intervals[i].end))
	res.append(start)
	return res
#transfer a binary search tree(bst) between two computers（传一个preorder） if it's binary tree(传preorder and inorder)
#Merge k sorted arrays
def mergeKArray(arrs):
	pq=[]
	for x in range(len(arrs)):
		if arrs[x]:
			heapq.heappush(pq,(arrs[x][0],1,x))
	res=[]
	while pq:
		value,index,arrNum=heapq.heappop(pq)
		res.append(value)
		if index<len(arrs[arrNum]):
			heapq.heappush(pq,(arrs[arrNum][index],index+1,arrNum))
	return res
#Evaluate Reverse Polish Notation
def evalRPN(tokens):
	stack=[]
	res=0
	for i in tokens:
		if i in '+-*/':
			value1=stack.pop()
			value2=stack.pop()
			if i=='+':
				stack.append(int(value1)+int(value2))
			elif i=='-':
				stack.append(int(value2)-int(value1))
			elif i=='*':
				stack.append(int(value2)*int(value1))
			else:
				stack.append(-(abs(int(value2))/abs(int(value1))) if int(value2)*int(value1)<0 else int(value2)/int(value1))
		else:
			stack.append(i)
		return int(stack.pop())
#压缩字符串 aabbbcccc -> 2a3b4c abc -> abc compress string
def compressStr(strs):
	res=''
	i=0
	while i<len(strs):
		j=i+1
		while j<len(strs) and strs[j]==strs[i]:
			j+=1
		if j-i==1:
			res+=strs[i]
		else:
			res+=str(j-i)+strs[i]
		i=j
	return res
#第一个题是10进制转换成26 进制 decimal
def decimalTo26(number):
	res=''
	table={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P'}
	while number>0:
		res+=table[number%26]
		number/=26
	return res[::-1]
def tsToDecimal(str):
	res=0
	table={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25}
	str=str[::-1]
	for i in range(len(str)):
		res+=table[str[i]]*(26**i)
	return res
#count and say
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''
def countAndSay(n):
	def count(s):
		t='';count=0;curr='#'
		for i in s:
			if i!=curr:
				if curr!='#':
					t+=str(count)+curr
				curr=i
				count=1
			else:
				count+=1
		t+=str(count)+curr
		return t
	s='1'
	for i in range(2,n+1):
		s=count(s)
	return s
#在 trillion integer中找出最小的，O(n)；其实在问map-reduce.
# 在 Set<String> 中找出common suffix
def commonSuffix(strs):
	def findSuffix(str1,str2):
		p1=len(str1)-1;p2=len(str2)-1
		while p1>=0 and p2>=0:
			if str1[p1]==str2[p2]:
				p1-=1;p2-=1
			else:
				break
		return str1[p1+1:]
	suffix=strs[0]
	for i in range(1,len(strs)):
		suffix=findSuffix(suffix,strs[i])
	return suffix
#把数组里奇数都挪到前面偶数都挪到后面然后排序 move odd number in front of even number
def oddFrontEven(arr):
	def inplace_quick_sort(S, a, b):
		"""Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
		if a >= b: return                                      # range is trivially sorted
		pivot = S[b]                                           # last element of range is pivot
		left = a                                               # will scan rightward
		right = b-1                                            # will scan leftward
		while left <= right:
		# scan until reaching value equal or larger than pivot (or right marker)
			while left <= right and S[left] < pivot:
				left += 1
				# scan until reaching value equal or smaller than pivot (or left marker)
			while left <= right and pivot < S[right]:
				right -= 1
			if left <= right:                                    # scans did not strictly cross
				S[left], S[right] = S[right], S[left]              # swap values
				left, right = left + 1, right - 1                  # shrink range

			# put pivot into its final place (currently marked by left index)
		S[left], S[b] = S[b], S[left]
		# make recursive calls
		inplace_quick_sort(S, a, left - 1)
		inplace_quick_sort(S, left + 1, b)
	p1=0;p2=0
	while p1<len(arr) and p2<len(arr):
		while p1<len(arr) and arr[p1]%2!=0:p1+=1
		p2=p1
		while p2<len(arr) and arr[p2]%2==0:p2+=1
		if p1==len(arr) or p2==len(arr):
			break
		arr[p1],arr[p2]=arr[p2],arr[p1]
	inplace_quick_sort(arr,0,p1-1)
	inplace_quick_sort(arr,p1,len(arr)-1)
	return arr
#two sum
def twoSum(arr,target):
	numDict={}
	index1=-1;index2=-1
	for i in range(len(arr)):
		if arr[i] not in numDict:
			numDict[target-arr[i]]=i
		else:
			index1=numDict[arr[i]]
			index2=i
			break
	return [index1,index2]
'''
给的是每个token的数量，以及要取的token数k，返回所有可能的组合，例子：
input:
A: 3, B: 1, C: 0, D: 2
k = 3
output:
AAA, AAB, AAD, ABD, ADD, BDD
就是一个对同一token的内循环，然后recursive找下一个token，从所有返回值的前面append当前选中的token。注意处理一下边界情况，比如挑完了还没到k个，或者什么时候算挑完了返回给recursion上一层。
'''
def generateTokens(input,k):
	def dfs(currRes,remainStr):
		if len(currRes)==k:
			if currRes not in res:
				res.append(currRes)
			return
		for i in range(len(remainStr)):
			if i>0 and remainStr[i]==remainStr[i-1]:
				continue
			#remainStr[:i] can be removed depends on the condition in the problem
			dfs(currRes+remainStr[i],remainStr[:i]+remainStr[i+1:])
	currStr=''
	for i in input:
		currStr+=i*input[i]
	print currStr
	res=[]
	dfs('',currStr)
	return res
'''
bit manipulation：given byte[] date, length of data (in bit), byte[] pattern, length of pattern (in bit)。多出来的bit无视。（比如说data有可能是byte[] = {10101001, 01001100}，length是14的话，其实就是只有前面14个bit是有效的，即10101001 010011；pattern同理）
返回所有pattern和data能够match的index。
例子：
input:
date[] = {10101001, 01001100}, length = 14
pattern[] = {10100000}, length = 3
output:
0 2 7
'''
def patternMatch(data,dataLen,pattern,patternLen):
	dataStr=''
	for i in data:
		if len(dataStr)<dataLen:
			binPart=str(bin(i))[2:]
			if len(binPart)!=8:
				binPart='0'*(8-len(binPart))+binPart
			dataStr+=binPart
		else:
			break
	dataStr=dataStr[:dataLen]
	patternStr=''
	for i in pattern:
		if len(patternStr)<patternLen:
			binPart=str(bin(i))[2:]
			if len(binPart)!=8:
				binPart='0'*(8-len(binPart))+binPart
			patternStr+=binPart
		else:
			break
	patternStr=patternStr[:patternLen]
	res=[]
	for i in range(dataLen-patternLen):
		if dataStr[i:i+patternLen]==patternStr:
			res.append(i)
	print dataStr
	return res
#检查两个字符是否为乱序重组，比如abc和bac, 如果不用hashset怎么做 (排序去重复)。
def sameLetterStr(str1,str2):
	if len(str1)!=len(str2):return False
	strDict1={}
	strDict2={}
	for i in str1:
		if i not in strDict1:
			strDict1[i]=1
		else:
			strDict1[i]+=1
	for i in str2:
		if i not in strDict2:
			strDict2[i]=1
		else:
			strDict2[i]+=1
	return strDict1==strDict2
def sameLetterStr1(str1,str2):
	if len(str1)!=len(str2):return False
	str1=''.join(sorted(str1))
	str2=''.join(sorted(str2))
	for i in range(len(str1)):
		if str1[i]!=str2[i]:
			return False
	return True
#举一个例子, 如果有一个class A, 和一个object b, 什么时候会用到(A)b 这种TypeCast
'''
You need to be sure you can perform the cast
You should design your classes polymorphically so casting is unnecessary
Even though you know of this reference as type X, I want you to treat it as if it were of type Y.
Base b = new Derived(); //reference variable of Base class points object of Derived class
Derived d = b; //compile time error, requires casting
Derived d = (Derived) b; // type casting Base to Derived
'''
#写了一个类Foo,里面只有一个int和一个string和一个非常普通的constructor。问：如果这个类要当hashtable的key，应该多做什么？目前综合起来比较正确的答案是：implements Comparable<Foo>，写好equals函数，然后，override hashcode提供比较靠谱的hash function。他还问我这个hashcode的好坏应该有什么判别标准，答：尽可能地避免conflict
#Print all factors of the product of a given list of distinct primes.input: 2 3 7   output: factors of 2*3*7:  1 2 3 6 7 14 21 42
def powerset(primes):
	def helper(deep,buffer):
		if deep==len(primes):
			res.append(buffer)
			return
		helper(deep+1,buffer)
		helper(deep+1,buffer*primes[deep])
	res=[]
	helper(0,1)
	res.sort()
	return res
#or we can make something like[[1,2],[1,3],[1,7]] first, and do dfs
'''
java solution
public class Test {

    public List<Integer> powerset(List<Integer> primes) {
        List<Integer> res = new ArrayList<>();
        helper(res, primes, 0, 1);
        return res;
    }

    public void helper(List<Integer> res, List<Integer> primes, int deep,
            int buffer) {
        if (deep == primes.size()) {
            res.add(buffer);
            return;
        }
        helper(res, primes, deep + 1, buffer);
        helper(res, primes, deep + 1, buffer * primes.get(deep));
    }

    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(2);
        list.add(3);
        list.add(7);
        List<Integer> res = new Test().powerset(list);
        System.out.println(res);
    }
}
'''
#Print all factors of a given int:e.g. input : 20   output: 1 2 4 5 10 20
def allFactor(n):
	res=[]
	currUpper=n
	res.append(1)
	if n==1:return res
	res.append(n)
	i=2
	while i<currUpper:
		if n%i==0:
			res.append(i)
			currUpper=n/i
			if currUpper!=i:
				res.append(currUpper)
		i+=1
	return res
'''
java solution
public class Test {

    public List<Integer> allfactor(int N) {
        List<Integer> res = new ArrayList<>();
        int curupper = N;
        res.add(1);
        if (N == 1) {
            return res;
        }
        res.add(N);
        for (int i = 2; i < curupper; i++) {
            if (N % i == 0) {
                res.add(i);
                curupper = N / i;
                if (curupper != i) {
                    res.add(curupper);
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        List<Integer> res = new Test().allfactor(20);
        System.out.println(res);
    }
}
'''
#Longest common subsequence
#http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
'''
String C is a longest common subsequence (LCS) of strings A and B if C is a common subsequence of A & B and there is no other common subsequence of A & B that has greater length.

Let Li, j be the length of an LCS of A[1...i] & B[1...j], i.e., the prefixes of strings A & B of lengths i and j.

Li, j = Li-1, j-1 + 1, if Ai = Bj 
Li, j = Max{ Li-1, j, Li, j-1}, if Ai ≠ Bj

LONGEST COMMON SUBSEQUENCE(A,m,B,n)
    for i := 0 to m do Li,0 := 0
    for j := 0 to n do L0,j := 0
    for i := 1 to m do
       for j := 1 to n do
          if Ai = Bj then
             Li,j := 1 + Li-1,j-1
          else
             Li,j := Max{ Li-1,j, Li,j-1}
    length := Lm,n
'''
#Longest common substring
'''
Let Li, j = maximum length of common strings that end at A[i] & B[j].   Then,

        A[i] = B[j] → Li, j = 1 + Li-1, j-1 
        A[i] ≠ B[j] → Li, j = 0

LONGEST COMMON SUBSTRING(A,m,B,n)
    for i := 0 to m do Li,0 := 0
    for j := 0 to n do L0,j := 0
    len := 0
    answer := <0,0>
    for i := 1 to m do
       for j := 1 to n do
          if Ai ≠ Bj then
             Li,j := 0
          else
             Li,j := 1 + Li-1,j-1
             if Li,j > len then
                len := Li,j
                answer = <i,j>
'''
#Palindrome Paritioning II
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        dp=[0 for i in range(len(s)+1)]
        p=[[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)+1):
            dp[i]=len(s)-i
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j] and (((j-i)<2) or p[i+1][j-1]):
                    p[i][j]=True
                    dp[i]=min(1+dp[j+1],dp[i])
        return dp[0]-1
#Reverse Nodes in k-Group
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dummy=ListNode(0);dummy.next=head
        pre=dummy
        while head:
            count=0
            start=head
            while head and count<k-1:
                head=head.next
                count+=1
            if count!=k-1 or head is None:
                break
            nexthead=head.next
            head.next=None
            first,last=self.reverse(start,head)
            pre.next=first;last.next=nexthead
            pre=last;head=nexthead
        return dummy.next
    def reverse(self,start,end):
        dummy=ListNode(0);dummy.next=start
        while start and start.next:
            first=start;second=start.next
            old=dummy.next
            dummy.next=second
            first.next=second.next
            second.next=old
        return dummy.next,start
'''
一些人排成队，每个人知道自己前面有多少个人比自己高(height)(taller)。已知每个人的身高。要求根据这些信息求出原先排好的队。(从高往低排)
个人感觉应该先按height排序，然后再从后往前扫根据Tvalue进行微调。不过由于对数组元素的删除和插入的开销较大
height[] = {4, 5, 10, 5, 4, 3};
Tvalue[] = {0, 0, 0, 1, 3, 5};

排序后：
height:       3, 4, 4, 5, 5, 10
对应Tvalue: 5, 0, 3, 0, 1, 0;

从后往前扫，如果Tvalue为0，就不动，否则移到队列的尾部。如果输入结构是数组，则另外需要额外开辟一个数组空间；如果输入结构是链表，则没有空间开销。
1) 3, 4, 4, 5, 5, 10; (check 10 - stay) 最后一个数最大，所以必然不动
2) 3, 4, 4, 5, 10, 5; (check 5 - move)
3) 3, 4, 4, 5, 10, 5; (check 5 - stay)
4) 3, 4, 5, 10, 5, 4; (check 4 - move)
5) 3, 4, 5, 10, 5, 4; (check 4 - stay)
6) 4, 5, 10, 5, 4, 3; (check 3 - move)
'''
def lineUp(peoples):
	peoples.sort()
	for i in range(1,len(peoples)):
		higherBefore=0;shiftLeft=i
		for j in range(i):
			if peoples[j][0]>peoples[i][0]:
				higherBefore+=1
			while higherBefore>peoples[shiftLeft][1] and shiftLeft>0:
				if peoples[shiftLeft-1][0]>peoples[shiftLeft][0]:
					higherBefore-=1
					peoples[shiftLeft],peoples[shiftLeft-1]=peoples[shiftLeft-1],peoples[shiftLeft]
					shiftLeft-=1
	return peoples	
#validate binary search tree
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def check(root,minval,maxval):
            if root is None:
                return True
            if root.val<=minval or root.val>=maxval:
                return False
            return check(root.left,minval,root.val) and check(root.right,root.val,maxval)
        return check(root,-2147483648,2147463647)
#一种商品的价格和数量不一定是线性关系，给你一定数量的钱，问最多可以买多少。因为不是线性关系，所以直接用二分就好了。不过先找到upper boundary，每次指数增长，不断尝试，直到钱不够就好了。然后在这个区间中做二分。
#inorder traversal preorder traversal postorder traversal
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res
    def preorderTraversal(self, root):
        res=[]
        stack=[None]
        while root:
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            root=stack.pop()
        return res
	def postorderTraversal(self, root):
        stack=[]
        pre=None
        res=[]
        while stack or root:
            if root is not None:
                stack.append(root)
                root=root.left
            else:
                peek=stack[-1]
                if peek.right and pre!=peek.right:
                    root=peek.right
                else:
                    stack.pop()
                    res.append(peek.val)
                    pre=peek
        return res
#给你一张m*n的board, 还有随机一个movie的名字，输出left right up down 把电影的名字中的字符依次select. Find a Word in a Matrix
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(x,y,currpos):
            if currpos==len(word):
                return True
            if x>0 and board[x-1][y]==word[currpos]:
                temp,board[x-1][y]=board[x-1][y],'1'
                if dfs(x-1,y,currpos+1):
                    return True
                temp,board[x-1][y]=board[x-1][y],temp
            if x<len(board)-1 and board[x+1][y]==word[currpos]:
                temp,board[x+1][y]=board[x+1][y],'1'
                if dfs(x+1,y,currpos+1):
                    return True
                temp,board[x+1][y]=board[x+1][y],temp
            if y<len(board[x])-1 and board[x][y+1]==word[currpos]:
                temp,board[x][y+1]=board[x][y+1],'1'
                if dfs(x,y+1,currpos+1):
                    return True
                temp,board[x][y+1]=board[x][y+1],temp
            if y>0 and board[x][y-1]==word[currpos]:
                temp,board[x][y-1]=board[x][y-1],'1'
                if dfs(x,y-1,currpos+1):
                    return True
                temp,board[x][y-1]=board[x][y-1],temp
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    temp,board[i][j]=board[i][j],'1'
                    if dfs(i,j,1):
                        return True
                    board[i][j]=temp
        return False
#一个two-dimensional array， 只有0和1, 相邻的一堆1 构成一个cluster, 问总共有几个cluster.
#find longest in sequence in a matrix,use dfs add another counter variable to track the sequence
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        def dfs(x, y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y]!='1':return
            board[x][y] = 'D'
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
		if len(board)==0:
			return
		count=0
        m = len(board); n = len(board[0])
        for i in range(m):
			for j in range(n):
				if board[i][j]=='1':
					count+=1
					dfs(i, j)
		return count
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        def fill(x, y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y] != '1': return
            queue.append((x,y))
            board[x][y]='D'
        def bfs(x, y):
            if board[x][y]=='1':queue.append((x,y)); fill(x,y)
            while queue:
                curr=queue.pop(0); i=curr[0]; j=curr[1]
                fill(i+1,j);fill(i-1,j);fill(i,j+1);fill(i,j-1)
        if len(board)==0: return
        m=len(board); n=len(board[0]); queue=[]
		count=0
        for i in range(m):
            for j in range(n):
				if board[i][j]=='1':
					count+=1
					bfs(i,j)
#写一个函数Children(Node *r)输出BST的当前节点的所有儿子。递归和非递归，哪个快怎样优化之类的问了问，就结束了。
#level order traversal?
#find k largest value (two/2 largest value) in an array (quick select)
def quick_select(S, k):
  """Return the kth smallest element of list S, for k from 1 to len(S)."""
  if len(S) == 1:
    return S[0]
  pivot = random.choice(S)             # pick random pivot element from S
  L = [x for x in S if x < pivot]      # elements less than pivot
  E = [x for x in S if x == pivot]     # elements equal to pivot
  G = [x for x in S if pivot < x]      # elements greater than pivot
  if k <= len(L):
    return quick_select(L, k)          # kth smallest lies in L
  elif k <= len(L) + len(E):
    return pivot                       # kth smallest equal to pivot
  else:
    j = k - len(L) - len(E)            # new selection parameter
    return quick_select(G, j)          # kth smallest is jth in G
import random
def partition(vector, left, right, pivotIndex):
    pivotValue = vector[pivotIndex]
    vector[pivotIndex], vector[right] = vector[right], vector[pivotIndex]  # Move pivot to end
    storeIndex = left
    for i in range(left, right):
        if vector[i] < pivotValue:
            vector[storeIndex], vector[i] = vector[i], vector[storeIndex]
            storeIndex += 1
    vector[right], vector[storeIndex] = vector[storeIndex], vector[right]  # Move pivot to its final place
    return storeIndex
 
def _select(vector, left, right, k):
    "Returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1] inclusive."
    while True:
        pivotIndex = random.randint(left, right)     # select pivotIndex between left and right
        pivotNewIndex = partition(vector, left, right, pivotIndex)
        pivotDist = pivotNewIndex - left
        if pivotDist == k:
            return vector[pivotNewIndex]
        elif k < pivotDist:
            right = pivotNewIndex - 1
        else:
            k -= pivotDist + 1
            left = pivotNewIndex + 1
'''
+1 North America
+1950 Northern Cal
+44 UK
+4420 London
+447 UK Mobile
+44750 Vodafoned
and we have a phone number, for instance
+447507439854795
+44989045454
return where the number is from
trie Trie
'''
class Node:
    def __init__(self):
        self.value = None
        self.children = {}    # children is of type {char, Node}                                                                                                       
 
class Trie:
    def __init__(self):
        self.root = Node()
 
    def insert(self, key):      # key is of type string                                                                                                                
        # key should be a low-case string, this must be checked here!                                                                                                  
        node = self.root
        for char in key:
            if char not in node.children:
                child = Node()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = key
 
    def search(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            else:
                node = node.children[char]
        return node.value
 
    def display_node(self, node):
        if (node.value != None):
            print node.value
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char in node.children:
                self.display_node(node.children[char])
        return
 
    def display(self):
        self.display_node(self.root)
#给个board，有且仅有一片连续的1，其他位置是0，找一个最小的box（rectangular）将1全部装进去。用BFS解决
#遍历整个board，找到min(up),min(left),max(right),max(down)
#或者bfs，参考line 1470
#wildcard matching pattern
'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        sp=0;pp=0;ss=0
        star=-1
        while sp<len(s):
            if pp<len(p) and (s[sp]==p[pp] or p[pp]=='?'):
                sp+=1
                pp+=1
                continue
            if pp<len(p) and p[pp]=='*':
                star=pp
                pp+=1
                ss=sp
                continue
            if star!=-1:
                pp=star+1
                ss+=1
                sp=ss
                continue
            return False
        while pp<len(p) and p[pp]=='*':
            pp+=1
        if pp==len(p):return True
        return False
#word break
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for k in range(0,i):
                if dp[k] and s[k:i] in dict:
                    dp[i]=True
        return dp[len(s)]
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        #看s能否完全分割开
        def check(s,dict):
            dp=[False for i in range(len(s)+1)]
            dp[0]=True
            for i in range(1,len(s)+1):
                for j in range(0,i):
                    if dp[j] and s[j:i] in dict:
                        dp[i]=True
            return dp[len(s)]
        def dfs(s,dict,stringlist):
            if check(s,dict):
                #s已经被完全分割
                if len(s)==0:
                    res.append(stringlist[1:])
                #每次以不同的长度分割s
                for i in range(1,len(s)+1):
                    if s[:i] in dict:
                        dfs(s[i:],dict,stringlist+' '+s[:i])
        res=[]
        dfs(s,dict,'')
        return res
#two sorted array 找出合并之后的kth smallest的值/Median of two sorted Array
class Solution:
    # @return a float
    # @line20 must multiply 0.5 for return a float else it will return an int
    def getKth(self, A, B, k):
        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k/2, lenA); pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)
    
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5
#least common ancestor· 有指向父节点指针的情况。
def lca(root,x,y):
	if root is None:
		return False,False,None
	leftx,lefty,leftca=lca(root.left,x,y)
	if leftca:
		return True,True,leftlca
	rightx,righty,rightca=lca(root.right,x,y)
	if rightca:
		return True,True,rightca
	foundx=leftx or rightx or root is x
	foundy=lefty or righty or root is y
	return foundx,foundy,root if foundx and foundy else None
def lca(x,y):
	tempx=x;tempy=y
	levelx=0;levely=0
	while tempx:
		tempx=tempx.parent
		levelx+=1
	while tempy:
		tempy=tempy.parent
		levely+=1
	if levelx>levely:
		count=levelx-levely
		while count>0:
			x=x.parent
			count-=1
	elif levelx<levely:
		count=levely-levelx
		while count>0:
			y=y.parent
			count-=1
	while x!=y:
		x=x.parent
		y=y.parent
	return x
#Clone Graph
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def dfs(input, map):
            if input in map:
                return map[input]
            output = UndirectedGraphNode(input.label)
            map[input] = output
            for neighbor in input.neighbors:
                output.neighbors.append(dfs(neighbor, map))
            return output
        if node == None: return None
        return dfs(node, {})
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return None
        queue = []; map = {}
        newhead = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = newhead
        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    copy = UndirectedGraphNode(neighbor.label)
                    map[curr].neighbors.append(copy)
                    map[neighbor] = copy
                    queue.append(neighbor)
                else:
                    # turn directed graph to undirected graph
                    map[curr].neighbors.append(map[neighbor])
        return newhead
#Spiral Matrix
def spiralMat(arr):
	res=[]
	up=0;left=0
	down=len(arr)-1
	right=len(arr[0])-1
	direction=0
	while True:
		if direction==0:
			for i in range(left,right+1):
				res.append(matrix[up][i])
			up+=1
		if direction==1:
			for i in range(up,down+1):
				res.append(matrix[i][right])
			right-=1
		if direction==2:
			for i in range(right,left-1,-1):
				res.append(matrix[down][i])
			down-=1
		if direction==3:
			for i in range(down,up-1,-1):
				res.append(matrix[i][left])
			left+=1
		direction=(direction+1)%4
		if up>down or left>right:break
	return res
#数组加一个数，比如[2,3,4,5] + 45=[2,3,9,0]。DT的是只能用数组不能用vector，在加完还有进位的时候需要重新new空间，很快写完以后又让优化了几遍
def arrAdd(arr,num):
	carry=0
	arr[-1]+=num
	for i in range(len(arr)-1,-1,-1):
		arr[i]+=carry
		carry=arr[i]/10
		arr[i]%=10
	if carry!=0:
		arr=[int(x) for x in str(carry)]+arr
	return arr
#FindCloset(float a[],length,target)，有序表找最接近数字，这个简单二分查找，写完他也没说什么。
def findCloset(a,length,target):
	left=0;right=length-1
	while left<=right:
		mid=(left+right)/2
		if a[mid]==target:
			return mid
		elif target<a[mid]:
			right=mid-1
		else:
			left=mid+1
	return -1
#很多文件里面有很多数字，设计排序的算法，答了个外排序的归并，接着问很多机器怎么进一步优化。楼主不懂Map-Reduce就YY了一通。那边又要求希望两个Iterator做完所有排序，然后瞎扯了一会这题就这么过了
#heap sort?
#There is an array of 3-tuple, in the form of (a, 1, 5). The first element in the tuple is the id, the second and third elements are both integers, and the third is always larger than or equal to the second. Assume that the array is sorted based on the second element of the tuple. Write a function that breaks each of the 3-tuple into two 2-tuples like (a, 1) and (a, 5), and sort them according to the integer. E.g. given (a, 1, 5), (b, 2, 4), (c, 7, 8), output (a, 1), (b, 2), (b, 4), (a, 5), (c, 7), (c, 8).
def myCmp(a,b):
	return a[1]-b[1]
def sortTuple(tuples):
	res=[]
	for i in tuples:
		res.append((i[0],i[1]))
		res.append((i[0],i[2]))
	res.sort(myCmp)
	return res
#Maximal Rectangle Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        def largestRectangle(height):
            stack=[];i=0;area=0
            while i<len(height):
                if stack==[] or height[i]>height[stack[len(stack)-1]]:
                    stack.append(i)
                else:
                    curr=stack.pop()
                    width=i if stack==[] else i-stack[len(stack)-1]-1
                    area=max(area,width*height[curr])
                    i-=1
                i+=1
            while stack:
                curr=stack.pop()
                width=i if stack==[] else len(height)-stack[len(stack)-1]-1
                area=max(area,width*height[curr])
            return area
        if matrix==[]:return 0
        a=[0 for i in range(len(matrix[0]))];maxarea=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j]=a[j]+1 if matrix[i][j]=='1' else 0
            maxarea=max(maxarea,largestRectangle(a))
        return maxarea
#给个Binary Search Tree.with duplicate nodes。要求找到出现次数最多的那个数字。现场coding的话关键注意点在如何inorder遍历的同时刷新max。此外如果max是最后的一组数是个边界条件。
def findMaxNode(root):
	def inorder(node):
		if node:
			inorder(node.left)
			if node.val==pre:
				count+=1
				maxcount=max(maxcount,count)
			else:
				count=1
			pre=node.val
			inorder(node.right)
	pre=-2147483648
	maxcount=1
	inorder(root)
	return maxcount
#插入整数，然后计算最近五个数的平均数。
#以插入的整数为pivot做一次quick select,然后在左右两边做quick select
#设计snake的数据结构，queue + 二维boolean数组。然后写一个每次移动的函数。
#用queue来保存一条蛇的位置情况，boolean来设置边界
'''
给以下matrix sequence
level 0:
0
level 1:
1,2
3,4
level 2:
5,6,7,8
9,10,11,12
13,14,15,16
17,18,19,20
写个转换方程
4*4^(n-1) n>0
Sn=4(1-4^n)/(1-4)
row col 2^n n>0
'''
def generateMat(n):
	res=[[0]]
	if n<1:return res
	count=1
	for level in range(1,n+1):
		matrix=[[0 for x in range(2**level)] for x in range(2**level)]
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				matrix[i][j]=count
				count+=1
		res.append(matrix)
	return res
#给了A[], B[], C[]三个String数组，要求求出数组的Combination，每一个数组中至少选一个，不用考虑duplicate
def threeCombination(strs):
	def dfs(currComb,depth):
		if depth==len(strs) and len(currComb)>=len(strs):
			res.append(currComb)
			return
		for i in range(len(strs[depth])):
			originalComb=currComb
			if len(originalComb)<depth+1:
				pass
			else:
				dfs(originalComb,depth+1)
			currComb+=strs[depth][i]
			dfs(currComb,depth+1)
	res=[]
	dfs('',0)
	return res
#两个数组，问是不是permutation。 然后如果只能用constant space怎么做：quicksort。然后如果再让这两个数组是imutable，而且只能是n的复杂度,不考虑空间用couting sort
#有这么个游戏，举个例子：给你5个空_ _ _ _ _, 每次猜一个字母，这里出题人想让你猜出来clock，假如你猜a，告诉你这里面没有。你又猜c，他把c全写出来，所以你有c _ _ c _。 让你最多猜10次。写一个程序去猜。输入是几个空，要考虑每次猜的反馈，尽量把词猜出来。
#给不给字典，没给就是扯淡题
#坐标系第一象限上加射线，接下来所有输入的数据都是不相等的整数，不用考虑任何edge case。 想要这两个操作：1. insertX（x）， insertY（y），比如insertX， 就是现有的图上面加上x这条射线，象限会被插入的这些射线分成网格，每个格叫一个区域。 2. find（x，y），就是给个坐标，返回这个坐标所在的区域。可以返回区域的id，区域的id自己定。用二叉树。两棵平衡二叉搜索树，找到y1<=point<=y2/None,x1<=point<=x2/None
'''
Moving Average, 每次输入一个数，调用double next_val(int val)，和现有的windows_size，输出当前平均数。
例如，win_size = 3，
next_val(1) = 1/3; 
next_val(10) = (1 + 10) / 2; 
next_val(3) = (1 + 10 + 3) / 3; 
next_val(5) = (10 + 3 + 5) / 3 （因为已经数的总数已经到达win_size）
……
这题还算直接，一个queue不断记录当前的win_size个数，一个sum不断记录当前和就行。
'''
def movingAve(window_size,iter):
	queue=[]
	sum=0
	while iter.hasNext():
		item=iter.next()
		if len(queue)<window_size:
			queue.append(item)
		else:
			tmp=queue.pop(0)
			sum-=tmp
			queue.append(item)
		print sum/len(queue)
'''
Use the shorest unique prefix to represent each word in the array
input: ["zebra", "dog", "duck",”dot”]
output: {zebra: z, dog: do, duck: du}

[zebra, dog, duck, dove]
{zebra:z, dog: dog, duck: du, dove: dov}

[bearcat, bear]
{bearcat: bearc, bear: ""} 
再进一步处理,或者用radix tree
'''
def uniquePrefix(strs):
	validSubs={}
	usedSubs=set()
	for word in strs:
		for i in range(len(word)+1):
			sub=word[:i]
			if sub in usedSubs:
				if sub in validSubs:
					del validSubs[sub]
			else:
				validSubs[sub]=word
				usedSubs.add(sub)
	return validSubs
#flatten a linked list (merge k sorted list or merge and then sort)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def merge(self, head1, head2):
        if head1 == None: return head2
        if head2 == None: return head1
        dummy = ListNode(0)                             #归并时，新建一个链表头结点
        p = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
                p = p.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next
        if head1 == None:
            p.next = head2
        if head2 == None:
            p.next = head1
        return dummy.next
        
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        slow = head; fast = head                        #快慢指针技巧的运用，用来截断链表。
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None                                #head1和head2为截为两条链表的表头
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head
#输入： 乱序的byte collection ， 输出：有序byte 除去dup
#先排序再去重
def removeDup(arr):
	newlength=0
	i=0
	while i<len(arr):
		if i==0 or arr[newlength-1]!=arr[i]:
			arr[newlength]=arr[i]
			newlength+=1
		i+=1
	return arr[:newlength]
#第一个轮是给一个字符串，比如{a,b}xy{c,d,e}，返回所有的combination，也就是axyc, axyd, axye, bxyc, bxyd, bxye
def allCombination(strs):
	def dfs(depth,currStr):
		if depth==len(res):
			sol.append(currStr)
			return
		for i in range(len(res[depth])):
			dfs(depth+1,currStr+res[depth][i])
	first=strs.split('{')
	res=[]
	for second in first:
		if len(second)>0:
			third=second.split('}')
			for forth in third:
				if len(forth)>0:
					res.append(forth.split(','))
	sol=[]
	dfs(0,'')
	return sol
#第二个是有一个5*6的方格子，上面有26个字母和4个空格，给你两个字母，找到一个到另一个的路径
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board,a,b):
        def dfs(x, y,seq):
            if x<0 or x>m-1 or y<0 or y>n-1 or ord(board[x][y])!=seq:return
			if board[x][y]==b:return
            board[x][y] = '0'
            dfs(x-1, y,seq-1)
            dfs(x+1, y,seq-1)
            dfs(x, y+1,seq-1)
            dfs(x, y-1,seq-1)
		if len(board)==0:
			return
		count=0
        m = len(board); n = len(board[0])
        for i in range(m):
			for j in range(n):
				if board[i][j]==a:
					dfs(i, j,ord(a))
		return count
#aabbbcc compress a*2b*3c*2，decompress，原来的字符串里可能也有数字和* 4X0
def compress(strs):
	pre=strs[0]
	count=1
	res=''
	for i in range(1,len(strs)):
		if strs[i]==pre:
			count+=1
		else:
			res+=(pre+'*'+str(count))
			count=1
			pre=strs[i]
	res+=(pre+'*'+str(count))
	return res
def decompress(strs):
	res=''
	arrs=strs.split('*')
	letter=''
	if len(arrs[0])==0:
		letter='*'
	else:
		letter=arrs[0]
	for i in range(1,len(arrs)):
		if len(arrs[i])==0:
			letter='*'
		else:
			if len(arrs[i])==1:
				res+=letter*int(arrs[i])
			else:
				res+=letter*int(arrs[i][0:-1])
			letter=arrs[i][-1]
	return res
#time stamp
'''
给一堆数，代表时间戳/访问人数，输出整理出如果在相应时间内有时间戳，就输出出来，没有就填NaN。如果在短时间内有多个时间戳，就留下一个。 
sampling interval: 100
input sequence:
timestamps value
1012 7
1102 5
1095 3
1199 10
1405 8
output sequence:
timestamps value
1012 7
1102 5 (or 1095 3)
1199 10
1300 NaN
1405 8
'''
def timeStamp(sequence,interval):
	curr=1000
	maxValue=0
	valueIndex=-1
	i=0
	while i<len(sequence):
		if abs(sequence[i][0]-curr)<=interval/2:
			if sequence[i][1]>maxValue:
				valueIndex=i
				maxValue=sequence[i][1]
			i+=1
		else:
			if valueIndex==-1:
				print 'NaN'
			else:
				print sequence[valueIndex]
			maxValue=0
			valueIndex=-1
			curr+=interval
	if valueIndex==-1:
		print 'NaN'
	else:
		print sequence[valueIndex]
'''
stream of strings like this
"1 34 5 6"
"3 4 5 6 3"
"4 5 6 3 3"
...
每行是一个包含数字的string。去除所有数字完全重复的strings.比如这里的第二和第三行数字完全相同，可以合并成一个。要求合并所有数字完全重复的strings。
'''
#sort+trie or calculate hashcode+dict
#数字有重复，比如如果sum是10，{2,2,2,8,8}里面算两个(2,8)pair。求pair总数。
#if it is sorted, use two pointer
def twoSum(arrs,target):
	numDict={}
	for i in range(len(arrs)):
		if arrs[i] in numDict:
			numDict[arrs[i]].append(i)
		else:
			numDict[arrs[i]]=[i]
	count=0
	for i in range(len(arrs)):
		diff=target-arrs[i]
		if diff in numDict:
			count+=1
			if len(numDict[diff])==1:
				del numDict[diff]
			else:
				numDict[diff]=numDict[diff][1:]
	return count/2
#一道二叉树的，给定一个数字，判定二叉树上是否有条路径，总和等于这个数字
#binary tree path given sum
def findPath(root,uset,finalSum):
	lset=set();rset=set()
	if findPath(root.left,lset,finalSum) or findPath(root.right,rset,finalSum):
		return True
	for s1 in lset:
		if finalSum-root.val-s1==0 or (finalSum-root.val-s1) in rset:
		#first condition means a path from root to some descendant in root's left child
		#second condition means a path from some node in root's left child to some node in root's right child
			return True
		uset.add(s1+root.val)
	for s2 in rset:
		if finalSum-root.val-s2==0:
		#the path from root to some descendant in root's right child
			return True
		uset.add(s2+root.val)
	return False
#input是一个无限的int stream，然后要能随时输出之前所有数的平均数什么的
def outputAve(sequence):
	count=0
	totalSum=0
#sorted array and a X return all tuples a + b <= X   follow up： 换成 a, b, c三元  满足 a+ b+ c <= X  （二分法+头尾扫）duplicate
def tupleTwoSum(arr,x):
	search=x-arr[0]
	left=0;right=len(arr)-1
	tail=-1
	while left<=right:
		mid=(left+right)/2
		if arr[mid]==search:
			tail=mid
			break
		elif search<arr[mid]:
			right=mid-1
		else:
			left=mid+1
	if tail==-1:tail=left-1
	res=[]
	i=0;j=tail
	while i<j:
		currsum=arr[i]+arr[j]
		if currsum<=x:
			for k in range(i+1,j+1):
				res.append((arr[i],arr[k]))
		if currsum==x:
			i+=1;j-=1
			while i<j and arr[i]==arr[i-1]:i+=1
			while i<j and arr[j]==arr[j+1]:j-=1
		elif currsum<x:
			i+=1
			while i<j and arr[i]==arr[i-1]:i+=1
		else:
			j-=1
			while i<j and arr[j]==arr[j+1]:j-=1
	return res
def tupleThreeSum(arr,x):
	search=x-arr[0]-arr[1]
	left=0;right=len(arr)-1
	tail=-1
	while left<=right:
		mid=(left+right)/2
		if arr[mid]==search:
			tail=mid
			break
		elif search<arr[mid]:
			right=mid-1
		else:
			left=mid+1
	if tail==-1:tail=left-1
	res=[]
	for i in range(tail+1):
		j=i+1;k=tail
		while j<k:
			currsum=arr[i]+arr[j]+arr[k]
			if currsum<=x:
				for m in range(j+1,k+1):
					res.append((arr[i],arr[j],arr[m]))
			if currsum==x:
				j+=1;k-=1
			elif currsum<x:
				j+=1
			else:
				k-=1
	return res
#实现 void Schedule(int64 timestamp, function* to_run) = 0;多个模块会调用这个function 如何实现 semaphore or lock(mutex)
# tic-tac-toe： 给一个board，以current state判断是o赢,x赢,还是没人赢.follow up每次只能取一行的信息，每次只能存储O（2N＋K）的数据
#不考虑时间复杂度可以做到,用2 bits来存储状态
#atoi Implement atoi to convert a string to an integer.
class Solution:
    # @return an integer
    def atoi(self, str):
        for i in range(len(str)):
            if str[i]!=' ':
                str=str[i:]
                break
        for i in range(len(str)-1,-1,-1):
            if str[i]!=' ':
                str=str[:i+1]
                break
        if len(str)==0:return 0
        neg=False
        if str[0]=='-':
            neg=True
            str=str[1:]
        elif str[0]=='+':
            str=str[1:]
        if len(str)==0:return 0
        for i in range(0,len(str),):
            if ord(str[i])>=ord('0') and ord(str[i])<=ord('9'):
                continue
            else:
                str=str[:i]
                break
        res=0
        for i in range(0,len(str)):
            if ord(str[i])>=ord('0') and ord(str[i])<=ord('9'):
                res+=int(str[i])*(10**(len(str)-1-i))
            else:
                break
        if neg and res>2147483648:
            return -2147483648
        elif not neg and res>2147483647:
            return 2147483647
        return res if not neg else -res
#given Set<Point>, find the line with most number of Point's max points
class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points)<3:
            return len(points)
        res=0
        for i in range(len(points)):
            dup=1
            slopeList={'inf':0}
            for j in range(len(points)):
                if i==j:
                    continue
                if points[i].x== points[j].x and points[i].y==points[j].y:
                    dup+=1
                    continue
                slope=self.calculate_slope(points[j],points[i])
                if slope in slopeList.keys():
                    slopeList[slope]+=1
                else:
                    slopeList[slope]=1
            res=max(res,max(slopeList.values())+dup)
        return res
    def calculate_slope(self,a,b):
        if a.x==b.x:
            return 'inf'
        else:
            return float((b.y-a.y))/float((b.x-a.x))
#Implement strStr() using recursion
def strStr(s1,s2):
	def strStrHelper(s1,s2,start):
		if s1 is None:return -1
		index=start
		isFound=False
		for i in range(index,len(s2)):
			if s1[i]!=s2[i]:
				break
			else:
				if i==len(s2)-1:
					isFound=True
		if isFound:
			return index
		else:
			return strStrHelper(s1[1:],s2,start+1)
	if s1 is None:
		return -1
	return strStrHelper(s1,s2,0)
public class StrStr {

    public String strKMP(String haystack, String needle) {
        if (needle.length() == 0) {
            return haystack;
        }
        //get next array
        int[] next = generateNext(needle.toCharArray());
        int len = 0;     // Number of characters matched            

        for (int i = 0; i < haystack.length(); i++) {
            while (len > 0 && needle.charAt(len) != haystack.charAt(i)) {
                len = next[len];
            }
            if (needle.charAt(len) == haystack.charAt(i)) {
                len++;
            }
            if (len == needle.length()) {
                return haystack.substring(i - needle.length() + 1);
            }
        }

        return null;
    }

    /**
     * KeyPoint. Get next array.
     *
     * @param needle
     * @return
     */
    private int[] generateNext(char[] needle) {
        //next array. next[i] means when match length = i, the common prefix and real suffix length = next[i] 
        int[] next = new int[needle.length + 1];
        //the longest common length of  prefix and real suffix.
        int presufix = 0;
        //next[1] = 0, starting from 2. i = match length.
        for (int i = 2; i < next.length; i++) {
            while (presufix > 0 && needle[presufix] != needle[i - 1])//trickiest part
            {
                presufix = next[presufix];
            }
            if (needle[presufix] == needle[i - 1]) {
                presufix++;
            }
            next[i] = presufix;
        }
        return next;
    }

}
#2GB memory to sort 100GB data
#N-Way merge or counting sort
#关于suffix和prefix的题，给一个list，存一些词，然后组合成新词，然后把新词加到list，问longest word。比如 danc nce 可以组合成dance，然后dance存在list里面，dance又可以跟其他词组成新词。
#trie or some sort of radix tree
#把字典放到trie里面，再把字典中的单词反过来放一个trie，然后把list中的词拿过去search
#diameter of a binary tree
def getDiameter(root):
# calculates height and diameter at the same time
	result=[0,0]
	if root is None:return result
	leftResult=getDiameter(root.left)
	rightResult=getDiameter(root.right)
	height=max(leftResult[1],rightResult[1])+1
	rootDiameter=leftResult[1]+rightResult[1]+1
	leftDiameter=leftResult[0]
	rightDiameter=rightResult[0]
	result[0]=max(rootDiameter,max(leftDiameter,rightDiameter))
	result[1]=height
	return result
def getDiameter1(root):
	def getHeight(root):
		if root is None:return 0
		return max(getHeight(root.left),getHeight(root.right))+1
	if root is None:return 0
	rootDiameter=getHeight(root.left)+getHeight(root.right)+1
	leftDiameter=getDiameter(root.left)
	rightDiameter=getDiameter(root.right)
	return max(rootDiameter,max(leftDiameter,rightDiameter))
#input is players like（A,B,C,D）, print total rounds[[(A, B), (C, D)], [(A, C), (B, D)], [(A, D), (B, C)]], tournament
def tourney(teams):
    N = len(teams)
    R = N-1 # rounds
    M = N/2 # matches per round
    sched = [[None] * M for i in range(R)]
    played = set()
    def fill(i, t):
        # Replenish t at the start of each round.
        if i % M == 0:
            t = teams[:]
        # Pick out the highest-seeded team left in t.
        topseed = t.pop(min(range(len(t)), key=lambda i: teams.index(t[i])))
        # Try opponents in reverse order until we find a schedule that works.
        for j, opp in reversed(list(enumerate(t))):
            match = topseed, opp
            if match not in played:
                # OK, this is match we haven't played yet. Schedule it.
                sched[i // M][i % M] = match
                played.add(match)
                # Recurse, if there are any more matches to schedule.
                if i + 1 == R * M or fill(i + 1, t[j+1:]+t[:j]):
                    return True  # Success!
                # If we get here, we're backtracking. Unschedule this match.
                played.remove(match)
        return False
    if not fill(0, []):
        raise ValueError("no schedule exists")
    return sched
#给定two points，求shortest path，中间可能有一堆rectangular obstacle。O(mlogn)
import pqdict

def dijkstra(graph, source, target=None):
    """
    Computes the shortests paths from a source vertex to every other vertex in
    a graph
    """
    # The entire main loop is O( (m+n) log n ), where n is the number of
    # vertices and m is the number of edges. If the graph is connected
    # (i.e. the graph is in one piece), m normally dominates over n, making the
    # algorithm O(m log n) overall.

    dist = {}   
    pred = {}

    # Store distance scores in a priority queue dictionary
    pq = pqdict.PQDict()
    for node in graph:
        if node == source:
            pq[node] = 0
        else:
            pq[node] = float('inf')

    # Remove the head node of the "frontier" edge from pqdict: O(log n).
    for node, min_dist in pq.iteritems():
        # Each node in the graph gets processed just once.
        # Overall this is O(n log n).
        dist[node] = min_dist
        if node == target:
            break

        # Updating the score of any edge's node is O(log n) using pqdict.
        # There is _at most_ one score update for each _edge_ in the graph.
        # Overall this is O(m log n).
        for neighbor in graph[node]:
            if neighbor in pq:
                new_score = dist[node] + graph[node][neighbor]
                if new_score < pq[neighbor]:
                    pq[neighbor] = new_score
                    pred[neighbor] = node

    return dist, pred

def shortest_path(graph, source, target):
    dist, pred = dijkstra(graph, source, target)
    end = target
    path = [end]
    while end != source:
        end = pred[end]
        path.append(end)        
    path.reverse()
    return path

if __name__=='__main__':
    # A simple edge-labeled graph using a dict of dicts
    graph = {'a': {'b':14, 'c':9, 'd':7},
             'b': {'a':14, 'c':2, 'e':9},
             'c': {'a':9, 'b':2, 'd':10, 'f':11},
             'd': {'a':7, 'c':10, 'f':15},
             'e': {'b':9, 'f':6},
             'f': {'c':11, 'd':15, 'e':6}}

    dist, path = dijkstra(graph, source='a')
    print dist
    print path
    print shortest_path(graph, 'a', 'e')
#O(mn)
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
 
  def add_node(self, value):
    self.nodes.add(value)
 
  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
 
 
def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}
 
  nodes = set(graph.nodes)
 
  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node
 
    if min_node is None:
      break
 
    nodes.remove(min_node)
    current_weight = visited[min_node]
 
    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node
 
  return visited, path
#一个房间也就是2d array里面有obstacle，已知有k个点，求房间中离这k个点distance之和最短的那个点
#dijkstra?  
'''
In 2-D the problem can be solved in O(n log n) as follows:

Create a sorted array of x-coordinates and for each element in the array compute the "horizontal" cost of choosing that coordinate. The horizontal cost of an element is the sum of distances to all the points projected onto the X-axis. This can be computed in linear time by scanning the array twice (once from left to right and once in the reverse direction). Similarly create a sorted array of y-coordinates and for each element in the array compute the "vertical" cost of choosing that coordinate.

Now for each point in the original array, we can compute the total cost to all other points in O(1) time by adding the horizontal and vertical costs. So we can compute the optimal point in O(n). Thus the total running time is O(n log n).
'''
#coding and debugging: given a license plate like " ORS23T" and a dictionary in file, get the shortest word composed from the letters in plate "SORT" 
#generate all sequences and check?
#给你一个Node class，有getID, setID, getChildren（返回iterator）三个method。 有一个图，图里面有的node有ID，有的没有，怎么在1个pass之内把所有node都set上ID，要求所有ID不能重复，只能是正数，而且图上已有的ID不能改动。 (don't really understand)
#打印webpage的title和link page的title
import urllib, htmllib, formatter, re, sys
#necessary
url = sys.argv[1]
website = urllib.urlopen("http://"+url)
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
links = []
#get <a> tag
links = ptext.anchorlist
for link in links:
   if re.search('http', link) != None:
      print(link)
      website = urllib.urlopen(link)
      data = website.read()
      website.close()
      ptext = htmllib.HTMLParser(format)
      ptext.feed(data)
      morelinks = ptext.anchorlist
      for alink in morelinks:
         if re.search('http', alink) != None:
            links.append(alink)
#always remember to close
ptext.close()
'''
web server，many request，each request has a latency，find median value of these latencys
(two heap or 首先将全部整数划分为 216 个区域,然后读取数据统计落到各个区域里的数的个数,之后根据统计结 果就可以判断中位数落到哪个区域,同时知道这个区域中的第几大数刚好是中位数。然后第二次扫描我们 只统计落在这个区域中的那些数就可以了(bucket sort?))
Step 1: Add next item to one of the heaps

   if next item is smaller than maxHeap root add it to maxHeap,
   else add it to minHeap

Step 2: Balance the heaps (after this step heaps will be either balanced or
   one of them will contain 1 more item)

   if number of elements in one of the heaps is greater than the other by
   more than 1, remove the root element from the one containing more elements and
   add to the other one
Then at any given time you can calculate median like this:

   If the heaps contain equal elements;
     median = (root of maxHeap + root of minHeap)/2
   Else
     median = root of the heap with more elements
'''
#two heap
import Queue as queue # replace with 'import queue' if using Python 3

class MedianHeap:
    def __init__(self, numbers = None):
        self.median = None
        self.left = queue.PriorityQueue() # max-heap
        self.right = queue.PriorityQueue() # min-heap
        self.diff = 0 # difference in size between left and right
        
        if numbers:
            for n in numbers:
                self.put(n)

    def top(self):
        return self.median

    def put(self, n):
        if not self.median:
            self.median = n
        elif n <= self.median:
            self.left.put(-n)
            self.diff += 1
        else:
            self.right.put(n)
            self.diff -= 1

        if self.diff > 1:
            self.right.put(self.median)
            self.median = -self.left.get()
            self.diff = 0
        elif self.diff < -1:
            self.left.put(-self.median)
            self.median = self.right.get()
            self.diff = 0

    def get(self):
        median = self.median

        if self.diff > 0:
            self.median = -self.left.get()
            self.diff -= 1
        elif self.diff < 0:
            self.median = self.right.get()
            self.diff += 1
        elif not self.left.empty():
            self.median = -self.left.get()
            self.diff -= 1
        elif not self.right.empty():
            self.median = self.right.get()
            self.diff += 1
        else: # median was the only element
            self.median = None
        
        return median

    
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        numbers = map(int, sys.argv[1:])
        m = MedianHeap(numbers)
        print "Median is ", m.get()
#给一个string和一个dictionary， 找出只用字典里的字可以组成的longest substring
#多加一个循环
 class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for k in range(0,i):
                if dp[k] and s[k:i] in dict:
                    dp[i]=True
        return dp[len(s)]
#design elevator system  20 floor 3 elevators
import random

class Elevator(object):
    def __init__(self, num_of_floors, register_list, direction = "up", cur_floor=1):
        self.total_floors = num_of_floors
        self.reg_list = []
        self.floor = cur_floor
        self.direct = direction
    def move(self):
        """Moves the elevator one floor"""
        if self.total_floors == self.floor:
            self.direct = "down"
        if self.direct == "up":
            self.floor += 1
        else:
            self.floor -= 1
    def register_customer(self, customer):
        self.reg_list.append(customer)
    def cancel_customer(self, customer):
        self.reg_list.remove(customer)

class Building(object):
    def __init__(self, num_of_floors, customer_list, elevator):
        self.total_floors = num_of_floors
        self.customers = customer_list
    def run(self):
        while elevator.floor != 0:
            for customer in self.customers:
                if elevator.floor == customer.on_floor:
                    elevator.reg_list.append(customer)
                    customer.indicator = 1
                elif elevator.floor == customer.going_floor:
                    elevator.reg_list.remove(customer)
                    customer.indicator = 0
                    customer.fin = 1
            elevator.move()

    def output(self):
        pass

class Customer(object):
    def __init__(self, ID, num_of_floors, cur_floor=0, dst_floor=0, in_elevator=0, finished=0):
        self.ident = ID
        self.indicator = in_elevator
        self.fin = finished
        cur_floor = random.randint(1, num_of_floors)
        self.on_floor = cur_floor
        dst_floor = random.randint(1, num_of_floors)
        while dst_floor == cur_floor:
            dst_floor = random.randint(1, num_of_floors)
        self.going_floor = dst_floor


customer_count = 15
floor_count = 20
cus_list = []
for i in range(1, customer_count+1):
    cus_list.append(Customer(i, floor_count))
elevator = Elevator(floor_count, cus_list)
building = Building(floor_count, cus_list, elevator)
#anagram substring matching 
def search(pattern,txt):
	m=len(pattern);n=len(txt)
	res=[]
	countP={};countTW={}
	for i in range(m):
		if pattern[i] in countP:
			countP[pattern[i]]+=1
		else:
			countP[pattern[i]]=1
		if txt[i] in countTW:
			countTW[txt[i]]+=1
		else:
			countTW[txt[i]]=1
	for i in range(m,n):
		if countTW==countP:
			res.append(i-m)
		if txt[i] in countTW:
			countTW[txt[i]]+=1
		else:
			countTW[txt[i]]=1
		if countTW[txt[i-m]]==1:
			del countTW[txt[i-m]]
		else:
			countTW[txt[i-m]]-=1
	if countP==countTW:
		res.append(n-m)
	return res
#Given a bag of letters and a stream of words, identify whether word can be formed by the letter in the bag(letter in the bag cannot be reused). (hash map)
'''
Find a biggest room in a 100*100 cells
Each cell may have walls at North, East, South, and/or West.  The walls of a cell are represented by an integer with value 0 to 15.
A room consists of contiguous cells where each cell in that room can reach any other cells in the same room, without being blocked by a wall.
What is the size (the number of cells) of the biggest room?
NSWE
1000 :
   _   _  _  _
|  _            |
|  _ |_ _ _  |
|                |
|                |
   _   _  _  _
BFS+HASH?
'''
'''
There is a museum organized as NxN room. Some rooms are locked and inaccessible. Other rooms are open and some rooms have guards. Guards can only move north, south, east and west, only through open rooms and only within the museum. For each room, find the shortest distance to a guard. What is the time complexity of your algorithm?

As a start, consider a relatively naive approach.

With each guard G as a vertex in the set of rooms, R=N*N, and possible paths between adjacent rooms (edges) E.

If all room minimum distances must be known, BFS from each guard to each room.

This should take time G * (R+E), or something like G*(N*N+E), or G*(N*N).

This can certainly be optimized with memoization, as each BFS will be computing subtrees repeatedly that have already been completed. Depending on the room configuration, this could greatly reduce G from the above time complexity. I'm sure there must be something better than this, however.
You can get this down to O(N^2) by running a queue-based BFS after inserting all of the guards into the queue. You don't have to rerun the BFS for each guard.
BFS, add all guards into queue by an O(N^2) search. Then since each rooms only been add into queue at most once and the maximum degree of each node is 4, the time complexity is O(N^2)
'''
#window size k，input stream，要求随着流的输入，输出窗口中数字的majority(hashmap)
'''
第一题是, 给一个很大文件, 格式是这样的:
{
    foo=1
    bar=22
    baz=13
}
有很多这样的block. 然后问有"foo"的block的个数.
split and check or run through the whole file
'''
#following question 1, say we have a dictionay counting the scaned integer, for example dict={0:123, 1:3000,2:12, 3:500...}implement the method generate(), which return the next integer based on the probability in the dict
#加起来然后算比例，或者生成相应多的0,1,2...然后randchoice
#given a binary tree find all the same subtree
#level order traversal and same tree from bottom to top
class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
#given a target number，return square number (1，4，9，16…)组成的集合，sum为target且元素的minimum。(首先当然是先求出小于等于target的所有平方数。然后转化为背包问题)
int calMinNum(int num){
        vector<int> dp(num);
        dp[0] = 1;
        for (int i = 1; i<num; ++i){
                // dp[i] : number i+1;
                if (i + 1 == (int)sqrt(i + 1) * (int)sqrt(i + 1))
                        dp[i] = 1;
                else{
                        int tmp = i + 1;
                        for (int j = i; j >= (i + 1) / 2; --j){
                                tmp = min(tmp, dp[j - 1] + dp[i + 1 - j - 1]);
                                if (tmp == 2)
                                        break;
                        }. 
                        dp[i] = tmp;
                }
        }
        return dp.back();
}
#knapsack coin change
#http://blog.csdn.net/sgbfblog/article/details/7908837
def knap01(N, C): 
#num为物品数目，C为背包容量，w[i]为物品i的重量，v[i]为物品i的价值，f为结果列表长度C+1
    for i in range(0, N):
        for c in range(C, w[i]-1, -1):
            f[c] = max(f[c], f[c-w[i]] + v[i])
#####完全背包问题 解法1########
def knap_complete(N, C):
    for i in range(0, N):
        for c in range(C, -1, -1):
            for k in range(0, c/w[i]+1):
               if k*w[i] <= c:
                    f[c] = max(f[c], f[c-k*w[i]] + k*v[i])
#####完全背包问题 解法2########
def knap_complete_2(N, C):
    for i in range(0, N):
        for c in range(w[i], C+1):
            f[c] = max(f[c], f[c-w[i]] + v[i])
'''
有一个流输入的文件，要求实时输出根据输入的等概率数字，比如输入1，输出1，输入12，输出1或者2（1和2各占50%），输入1112，输出1(75%概率)或者2(25%概率)。输入的数列是一直在实时输入的流，会非常大，不能离线记录。
'''
#split and then random.choice
#transfer a binary search tree to a doubly linked list
'''
// This is a modified in-order traversal adapted to this problem.
// prev (init to NULL) is used to keep track of previously traversed node.
// head pointer is updated with the list's head as recursion ends.
'''
def treeToSortedDoublyList(root):
	def transfer(p,prev,head):
		if p is None:return
		transfer(p.left,prev,head)
		#current node's left points to previous node
		p.left=prev
		if prev:
			#previous node's right points to current node
			prev.right=p
		else:
			head=p
			'''
			// current node (smallest element) is head of
            // the list if previous node is not available
			// as soon as the recursion ends, the head's left pointer 
			// points to the last node, and the last node's right pointer
			// points to the head pointer.
			'''
		right=p.right
		head.left=p
		p.right=head
		#updates previous node
		prev=p
		transfer(right,prev,head)
	prev=None
	head=None
	transfer(root,prev,head)
	return head
'''
c++ normal transfer
/* This is the core function to convert Tree to list. This function follows
  steps 1 and 2 of the above algorithm */
node* bintree2listUtil(node* root)
{
    // Base case
    if (root == NULL)
        return root;
 
    // Convert the left subtree and link to root
    if (root->left != NULL)
    {
        // Convert the left subtree
        node* left = bintree2listUtil(root->left);
 
        // Find inorder predecessor. After this loop, left
        // will point to the inorder predecessor
        for (; left->right!=NULL; left=left->right);
 
        // Make root as next of the predecessor
        left->right = root;
 
        // Make predecssor as previous of root
        root->left = left;
    }
 
    // Convert the right subtree and link to root
    if (root->right!=NULL)
    {
        // Convert the right subtree
        node* right = bintree2listUtil(root->right);
 
        // Find inorder successor. After this loop, right
        // will point to the inorder successor
        for (; right->left!=NULL; right = right->left);
 
        // Make root as previous of successor
        right->left = root;
 
        // Make successor as next of root
        root->right = right;
    }
 
    return root;
}
 
// The main function that first calls bintree2listUtil(), then follows step 3 
//  of the above algorithm
node* bintree2list(node *root)
{
    // Base case
    if (root == NULL)
        return root;
 
    // Convert to DLL using bintree2listUtil()
    root = bintree2listUtil(root);
 
    // bintree2listUtil() returns root node of the converted
    // DLL.  We need pointer to the leftmost node which is
    // head of the constructed DLL, so move to the leftmost node
    while (root->left != NULL)
        root = root->left;
 
    return (root);
}
'''
#There are n coins in a line. (Assume n is even). Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.
#Would you rather go first or second? Does it matter?Assume that you go first, describe an algorithm to compute the maximum amount of money you can win.
#http://leetcode.com/2011/02/coins-in-line.html
def coinsInLine(A,N):
	c=[[0 for x in range(N)] for x in range(N)]
	for i in range(N):
		m=0;n=i
		while n<N:
			x=c[m+2][n] if m+2<N else 0
			y=c[m+1][n-1] if m+1<N and n-1>=0 else 0
			z=c[m][n-2] if n-1>0 else 0
			c[m][n]=max(A[m]+min(x,y),A[n]+min(y,z))
			m+=1;n+=1
	return c[0][N-1]
#sqrt(x)
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x<2:return x
        left=1;right=x-1
        while left<=right:
            mid=(left+right)/2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
        return left-1
#given two sorted array A B find matrix M[j] = A[i] + B[j] N largest number
import heapq
def nLargest(A,B,N):
	indexDict={}
	pq=[]
	i=len(A)-1;j=len(B)-1
	heapq.heappush(pq,(-A[i]-B[j],i,j))
	indexDict[(i,j)]=1
	count=0
	res=[]
	while count<N:
		number,indexI,indexJ=heapq.heappop(pq)
		res.append(-number)
		count+=1
		if (indexI-1,indexJ) not in indexDict:
			indexDict[(indexI-1,indexJ)]=1
			heapq.heappush(pq,(-A[indexI-1]-B[indexJ],indexI-1,indexJ))
		if (indexI,indexJ-1) not in indexDict:
			indexDict[(indexI,indexJ-1)]=1
			heapq.heappush(pq,(-A[indexI]-B[indexJ-1],indexI,indexJ-1))
	return res
#white cells black cells 摆成一排，颜色相同的相邻的格子不能超过两个，问有多少种组合方法
def whiteBlack(w,b):
    white=[[0 for x in range(b+1)] for x in range(w+1)]
    black=[[0 for x in range(b+1)] for x in range(w+1)]
    white[1][0]=1;white[2][0]=1;white[0][0]=0
    black[0][1]=1;black[0][2]=1;black[0][0]=0
    for i in range(1,w+1):
        for j in range(1,b+1):
            white[i][j]=black[i-1][j]
            if i>=2:
                white[i][j]+=black[i-2][j]
            black[i][j]=white[i][j-1]
            if j>=2:
                black[i][j]+=white[i][j-2]
    return white[-1][-1]+black[-1][-1]
#Hailstone sequence，从一个数n开始，如果n是奇数 乘3 +1， 如果是偶数就除以2， 直到到1为止（虽然没有人可以证实，但所有的数都可以到1）给你一个positive int， 找到经过多少步可以到1，定义为hailstone value
def hailStone(num):
	count=0
	res=[]
	orig=num
	while num>1:
		if num%2==0:
			num/=2
		else:
			num=num*3+1
		if num>orig:
			res.append(num)
		count+=1
	return count,res
'''
给你一个n，打印所有从1-n中 number whose hailstone value is greater than that for any smaller number.
比如n = 6
1 -- 0
2 -- 1
3 -- 7
4 -- 2（这里2< 7, 4不可以打印）
5 -- 5 （5 < 7, 不打印）
6 -- 8
'''
def allHail(n):
	skipDict={}
	res=[]
	for i in range(1,n+1):
		if i in skipDict:
			continue
		count,skip=hailStone(i)
		res.append((i,count))
		for i in skip:
			skipDict[i]=1
	return res
#给一个list和k（number）。找一个区域k，使得这个区域里k的最大值和最小值的差值最大，返回这个值
#use two heaps, one min heap one max heap, sliding window,use array to store max value for current start index
'''
h[i] = h[-1]
h.pop()
heapq.heapify(h)
'''
import heapq
def maxMinRegion(num,k):
	maxHeap=[]
	minHeap=[]
	res=[0 for x in range(len(num)-k+1)]
	for i in range(len(num)):
		if i<k:
			heapq.heappush(maxHeap,-num[i])
			heapq.heappush(minHeap,num[i])
		else:
			searchValue=num[i-k]
			index=maxHeap.index(-searchValue)
			maxHeap[index]=maxHeap[0]
			maxValue=-heapq.heappop(maxHeap)
			heapq.heapify(maxHeap)
			heapq.heappush(maxHeap,-num[i])
			index=minHeap.index(searchValue)
			minHeap[index]=minHeap[0]
			minValue=heapq.heappop(minHeap)
			heapq.heapify(minHeap)
			heapq.heappush(minHeap,num[i])
			res[i-k]=maxValue-minValue
        maxValue=-heapq.heappop(maxHeap)
        minValue=heapq.heappop(minHeap)
        res[len(num)-k]=maxValue-minValue
	return res
'''
given a list node ,every node can point to null or other nodes in the list, node 有个 getparent()的功能，问你list里面所有的node能不能形成一个tree。
1.先check是否只有一个node的getparent()方法返回的是否是null
2. 从root开始DFS,或者BFS, 看看是不是每个节点正好遍历一次 
'''
'''
given Set<String> set, List<Character> chars, return Set<String> which has longest be covered by the List<Character>
e.g. dgg cat naioe lot
1st case: dcnlggatio -> return [dgg,cat,lot]
2st case: dcnlggatioe -> return [naioe]
'''
def longest(strSet,chars):
	def containsAll(sortedChar,string):
		for i in string:
			if i not in sortedChar:
				return False
		return True
	sorted(chars)
	strList=list(strSet)
	strList.sort()
	res=[]
	maxLength=0
	for word in strList:
		contains=containsAll(chars,word)
		if contains and len(word)>maxLength:
			res=[word]
			maxLength=len(word)
		elif contains and len(word)==maxLength:
			res.append(word)
	return res
#find the longest increasing sequence in an integer matrix in 4 directions (up down left right), return the sequence; for example: input:	
'''
    //2,loop the matrix for filling
	public int filldp(int[][] grid,int[][] dp){
		if(grid.length==0 || grid[0].length==0) throw new IllegalArgumentException("");
		int rows = grid.length, cols = grid[0].length;
		//int[][] dp = new int[rows][cols];
		int max = 0;
		for(int i=0;i<rows;i++){
			for(int j=0;j<cols;j++){
				if(dp[i][j]==0){
					max = Math.max(max,fill(grid,i,j,dp));
				}else{
					max = Math.max(max, dp[i][j]);
				}
			}
		}
		return max;
	}
	
	//1,fill the dp matrix
	public int fill(int[][] grid, int r, int c,int[][] dp){
		if(r<=0 || c<=0 || r>grid.length-1 || c>grid[0].length-1){
			return 0;
		}
		if(dp[r][c]!=0){
			return dp[r][c];
		}
		int left=0,right=0,down=0,up=0;
		if(r-1>=0 && grid[r-1][c]==grid[r][c]+1){
			up = fill(grid,r-1,c,dp);
		}
		if(r+1<grid.length && grid[r+1][c] == grid[r][c]+1){
			down = fill(grid,r+1,c,dp);
		}
		if(c-1>=0 && grid[r][c-1] == grid[r][c]+1){
			left = fill(grid,r,c-1,dp);
		}
		if(c+1<grid.length && grid[r][c+1] == grid[r][c]+1){
			right = fill(grid,r,c+1,dp);
		}
		dp[r][c] = Math.max(Math.max(up, down),Math.max(left, right))+1;
		return dp[r][c];
	}
	
	//4, DFS for finding snake paths
	public void findall(int[][] grid,int[][] dp, ArrayList<ArrayList<Integer>> paths, ArrayList<Integer> one, int r, int c){
		if(dp[r][c]==1){
			one.add(grid[r][c]);
			paths.add(one);
			System.out.println(one);
			return;
		}
		one.add(grid[r][c]);
		if(r-1>=0 && dp[r-1][c] == dp[r][c]-1 && grid[r-1][c] == grid[r][c] +1)
			findall(grid,dp,paths,new ArrayList<Integer>(one),r-1,c);
		if(r+1<grid.length && dp[r+1][c] == dp[r][c]-1 && grid[r+1][c] == grid[r][c] +1)
			findall(grid,dp,paths,new ArrayList<Integer>(one),r+1,c);
		if(c-1>=0 && dp[r][c-1] == dp[r][c]-1 && grid[r][c-1] == grid[r][c] +1)
			findall(grid,dp,paths,new ArrayList<Integer>(one),r,c-1);
		if(c+1<grid[0].length &&   dp[r][c+1] == dp[r][c] -1 && grid[r][c+1] == grid[r][c] +1)
			findall(grid,dp,paths,new ArrayList<Integer>(one),r,c+1);
	}	
	//3,main func for finding all the snake seqs
	// assume we just need to find the elements along the snake paths not the coordinates
	public ArrayList<ArrayList<Integer>> findallsnakes(int[][] grid){
		if(grid.length==0 || grid[0].length==0) throw new IllegalArgumentException("");
		ArrayList<ArrayList<Integer>> snakes = new ArrayList<ArrayList<Integer>>();
		int rows = grid.length, cols = grid[0].length;
		int[][] dp = new int[rows][cols];
		int max = filldp(grid,dp);
		for(int i=0;i<rows;i++){
			for(int j=0;j<cols;j++){
				if(dp[i][j] == max){
					findall(grid,dp,snakes,new ArrayList<Integer>(),i,j);
				}
			}
		}
		return snakes;
	}
'''
'''
Tilt Maze,就只只能沿着一个方向走迷宫,不能一步步走,只能向一个方向走到边界或者遇到障碍物.面试官出了几个问题：
1.写一个数据结构来记录这个Maze
2.找到一条从起点s到终点e的路径，要求使用最少的move
3.找到一条从起点s到终点e的路径，要求使用距离最少
1就是给每个节点填一个byte 1110 用二进制mark每个方向是否能走: 
2就是BFS嘛
3是要建一个新的图，从s开始BFS，以一个点到达的另外一个顶点的距离为权值建一个新的图，如果该点已经被访问过了，则不用继续bfs这个节点；最坏的情况下，有N^2个节点。然后用Dijkstra做吧。
'''
'''
一个n*n矩阵，里面有整数，代表每个位置山的高度，然后如果在这个山头下雨，水流只能流去比他矮小或者一样高的山头。矩阵上边和左边是太平洋，下边和右边是大西洋。好吧。现在你找所有能流向两个大洋的点。
1.N*N次BFS
2.一次BFS可以搞定，就是初始化BFS的Queue的时候把四个边上的顶点全部放进去，然后按照可以去更高的顶点这么遍历就行了。所有被访问的点都是可达的。 
'''
#给了A[],B[],C[]三个String数组,要求求出数组的Combination,每一个数组中至少选一个,不用考虑duplicate
def threeCombination(A,B,C):
	def generateCombo(index,currlist,currArr,start):
		if len(currlist)>0:
			if index==0:
				res0.append(currlist)
			elif index==1:
				res1.append(currlist)
			else:
				res2.append(currlist)
		if len(currlist)==len(currArr):
			return
		for i in range(start,len(currArr)):
			if i>start and currArr[i]==currArr[i-1]:
				continue
			dfs(index,currlist+[currArr[i]],currArr,i+1)
	res0=[]
	res1=[]
	res2=[]
	generateCombo(0,[],A,0)
	generateCombo(1,[],B,0)
	generateCombo(2,[],C,0)
	res=[]
	for i in res0:
		for j in res1:
			for k in res2:
				res.append(i+j+k)
	return res
#local minimum local maxima
def localExtrema(arr):
	isRise=False
	minma=[]
	maxma=[]
	i=0
	while i<len(arr):
		if i==0:
			i+=1
			while arr[i]==arr[i-1]:
				i+=1
			if arr[i]>arr[i-1]:
				minma.append([x for x in range(i)])
				isRise=True
			else:
				maxma.append([x for x in range(i)])
				isRise=False
			continue
		if i==len(arr)-1:
			j=i
			while j-1>=0 and arr[j-1]==arr[j]:
				j-=1
			if isRise:
				maxma.append([x for x in range(j,i+1)])
			else:
				minma.append([x for x in range(j,i+1)])
			i+=1
			continue
		if isRise and arr[i]>=arr[i-1]:
			i+=1
			continue
		if not isRise and arr[i]<=arr[i-1]:
			i+=1
			continue
		if isRise and arr[i]<arr[i-1]:
			j=i-1
			while j-1>=0 and arr[j-1]==arr[j]:
				j-=1
			maxma.append([x for x in range(j,i)])
			isRise=False
			continue
		if not isRise and arr[i]>arr[i-1]:
			j=i-1
			while j-1>=0 and arr[j-1]==arr[j]:
				j-=1
			minma.append([x for x in range(j,i)])
			isRise=True
			continue
	return minma,maxma
#how many binary 1s in an integer. use AND operation
#h index. sort or http://stackoverflow.com/questions/20139640/looking-for-algorithm-to-calculate-h-index-fast
#求array 里unordered pair 的数量(前一个数比后一个数大)比如{1, 3, 2}里面有一个(3, 2), {1, 2,3}里面没有, {3, 2, 1}里面有三个(3, 2)(3, 1)(2, 1)
#naive approach, n^2
def unorderPair(arr):
	pairDict={}
	i=1
	while i<len(arr):
		if arr[i]>arr[i-1]:
			i+=1
		else:
			if i-1 in pairDict:
				pairDict[i]=[i-1]
				for index in pairDict[i-1]:
					pairDict[i].append(index)
			else:
				pairDict[i]=[i-1]
			i+=1
	return pairDict
#given an int[] array, e.g {1,5,0,6} and an int target，e.g. target = 21;问是否存在某种分法把array 分成几部分，每部分看成一个int，这几部分加起来等于target
'''
rec(int[] array, int start, int target, int prev) {
	for(i from start -> array.length) {
		/*
			get the number from start to this i
		*/
		rec(array, i+1, target, sum of prev and number);
	}
}
'''
#given an integer, find minlen expression of integer， minlen 定义为多少个square number相加
def findMinExpression(target):
	data=[0 for x in range(target+1)]
	i=1
	while i*i<=target:
		data[i*1]=1
		i+=1
	for i in range(1,target+1):
		tempMin=i
		j=1
		while j*j<=i:
			temp=data[i-j*j]+1
			tempMin=min(tempMin,temp)
			j+=1
		data[i]=tempMin
	return data[-1]
'''
int MinExpressionInteger(int i)
{
    int k = sqrt(i);
    if (k*k == i)
        return 1;
    int minLen = INT_MAX;
    while (k > sqrt(i / 2) - 1)
    {
        int len = 1 + MinExpressionInteger(i - k*k);
        if (minLen > len)
            minLen = len;
        k--;
    }
    return minLen;
}
'''
#社交网络中，如何实现好友推荐。抽象成图，然后找出共同好友最多的那个人
#given two sorted array 返回它们两个包含的相同元素,比如[2, 3, 4], [1, 2, 3, 5] 返回[2, 3].然后追加的是如果其中一个array 特别长一个比较短怎么做
#hashtable/binary search
#program对于相同的input 有时会crash 有时会正确。可能原因是什么
#sometimes a program works, sometimes it does not. Possible reasons
#multithreading random generator time based
#search minimum in rotated sorted array
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        left=0;right=len(num)-1
        ans=num[0]
        while left<=right:
            middle=(left+right)/2
            if num[middle]<=num[right]:
                right=middle-1
            else:
                left=middle+1
            ans=min(ans,num[middle])
        return ans
#search maximum in rotated sorted array
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMax(self, num):
        left=0;right=len(num)-1
        ans=num[0]
        while left<=right:
            middle=(left+right)/2
            if num[middle]<=num[right]:
                left=middle+1
            else:
                right=middle-1
            ans=max(ans,num[middle])
        return ans
#在一个文本中找不重复的行数有几个,返回行数 rolling hash+two hashmap
#remove duplicates from a list of strings sort/hashmap
#multithreading 程序开发应该注意什么(deadlock, livelock)
#开关灯问题
'''
class CheckLamp {
    public static void main(String[] arguments){
        int[] indexLamp;
        indexLamp=new int[100];
        String str="所有人按完开关后，还亮的灯有：";
        for (int personid=1;personid<101;personid++){
            for (int lightnum=personid;lightnum<101;lightnum++){
                if (lightnum%personid==0)
                    indexLamp[lightnum-1]=indexLamp[lightnum-1]+1;
                if ((lightnum==personid)&&(indexLamp[lightnum-1]%2==1))
                    str=str+lightnum+",";
                }
            }
        System.out.println(str);
'''
#big integer
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        res=[0 for x in range(len(num1)+len(num2))]
        num1=num1[::-1];num2=num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j]+=int(num2[j])*int(num1[i])
        carry=0
        for i in range(len(res)):
            currSum=carry+res[i]
            res[i]=currSum%10
            carry=currSum/10
        index=len(res)-1
        while res[index]==0 and index>0:
            index-=1
        resStr=''
        while index>=0:
            resStr+=str(res[index])
            index-=1
        return resStr
    }
}
#判断一个文件是否有重复的行，字符相同，顺序不同也算，比如abcd 和dcba 算重复。
#sort+hashmap or calculate hashcode+hashmap
#find longest substring with 2 distinct ASCII character
#find longest substring with N distince character
def longest(S,n):
    i = j = K = 0
    res = (0,0)
    last = {}

    while i < len(S):
        # if current substring is better than others than save
        if K == n and j - i > res[1] - res[0]:
            res = (i,j)

        # if we can go further with the right end than do it
        if K <= n and j + 1 <= len(S):
            if not last.has_key(S[j]):
                K = K + 1
            last[S[j]] = j
            j = j + 1
        # if we must go further with the left end than do it
        else:
            if last[S[i]] == i:
                del last[S[i]]
                K = K - 1
            i = i + 1
    return S[res[0]:res[1]]
#right rotate an array k times
def rightRotate(n,arr):
	if n==len(arr):
		return arr
	count=0;index=0
	prev=arr[index]
	for i in range(len(arr)):
		tmp=arr[(index+n)%(len(arr))]
		arr[(index+n)%len(arr)]=prev
		prev=tmp
		index=(index+n)%len(arr)
		count+=n
		if count%len(arr)==0:
			count=0
			index=(index+1)%len(arr)
			prev=arr[index]
	return arr
#left rotate
#http://www.geeksforgeeks.org/array-rotation/
#问一个word grid.给一个词，返回有多少个path 可以组成所给定的词 bfs or dfs
#find longest arithmetic progression in an unsorted array 
def lengthOfLongestAP(arr,n):
	arr.sort()
	if n<=2:
		return n
	L=[[0 for x in range(n)] for x in range(n)]
	llap=2
	for i in range(n):
		L[i][n-1]=2
	for j in range(n-2,0,-1):
		i=j-1;k=j+1
		while i>=0 and k<=n-1:
			if arr[i]+arr[k]<2*arr[j]:
				k+=1
			elif arr[i]+arr[k]>2*arr[j]:
				L[i][j]=2
				i-=1
			else:
				L[i][j]=L[j][k]+1
				llap=max(llap,L[i][j])
				i-=1
				k+=1
		while i>=0:
			L[i][j]=2
			i-=1
	return llap
#有k 个数，排好序的，这些数都是0 到N 间的，写一个randomnumber generate 来generate一个0-N 间的数且不能是k 里面的。
#keep generating, or generate a new array
#shuffle input [0,2,_,3],output [0,_,2,3] (hashmap)
#subarray containing continuous 1
'''
    public static int continOnes(int[] arr){
        int start=-1,end=-1;
        int max=0;
        boolean show=false;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==1&&!show){
                start=i;
                show=true;
                continue;
            }
            if(arr[i]!=1&&show){
                end=i;
                show=false;
                max=Math.max(end-start,max);
                continue;
            }
        }
        if(show){
            end=arr.length;
        }
        return Math.max(end-start,max);
    }
'''
#Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def largestRectangleArea(self, height):
        stack=[]; i=0; area=0
        while i<len(height):
            if stack==[] or height[i]>height[stack[-1]]:
                stack.append(i)
            else:
                curr=stack.pop()
                width=i if stack==[] else i-stack[-1]-1
                area=max(area,width*height[curr])
                i-=1
            i+=1
        while stack!=[]:
            curr=stack.pop()
            width=i if stack==[] else len(height)-stack[-1]-1
            area=max(area,width*height[curr])
        return area
        
    def maximalRectangle(self, matrix):
        if matrix==[]: return 0
        a=[0 for i in range(len(matrix[0]))]; maxArea=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j]=a[j]+1 if matrix[i][j]=='1' else 0
            
            maxArea=max(maxArea, self.largestRectangleArea(a))
        
        return maxArea
#container with most water 2d matrix(除去四周，一个一个找)
#longest common suffix of two linked list(reverse and compare one by one)
def reverseList(head):
	dummy=ListNode(0)
	dummy.next=head
	while head and head.next:
		newhead=head.next
		newNext=newhead.next
		newhead.next=dummy.next
		dummy.next=newhead
		head.next=newNext
	return dummy.next
#implement queue using stack
class Queue:
	def __init__(self):
		self.stack1=[]
		self.stack2=[]
	def add(self,item):
		self.stack1.append(item)
	def remove(self):
		if stack2:
			return stack2.pop()
		else:
			while stakc1:
				stack2.append(stack1.pop())
			return stack2.pop()
	def peek(self):
		if stack2:
			return stack2[-1]
		else:
			while stakc1:
				stack2.append(stack1.pop())
			return stack2[-1]
#implement a stack and able to query minimum value in O(1) time
class Stack:
	def __init__(self):
		self.stack=[]
		self.mins=[]
	def push(self,item):
		if len(self.stack)==0:
			self.stack.append(item)
			self.mins.append(item)
		else:
			self.stack.append(item)
			if item<=self.mins[-1]:
				self.mins.append(item)
	def pop(self):
		item=self.stack.pop()
		if item==self.mins[-1]:
			self.mins.pop()
		return item
	def min(self):
		return self.mins[-1]
	def peek(self):
		return self.stack[-1]
#given n lines in a panel,how can you find how many intersection points are there
#双重for loop,计算每条线对应其他线的交点数，斜率相同肯定没有交点，斜率不同肯定有一个交点
def maxIntersections(points):
	lineDict={}
	for i in range(len(points)):
		count=0
		for j in range(len(points)):
			if i==j:
				continue
			if points[i].slope!=points[j].slope:
				count+=1
		lineDict[points[i]]=count
class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points)<3:
            return len(points)
        res=0
        for i in range(len(points)):
            dup=1
            slopeList={'inf':0}
            for j in range(len(points)):
                if i==j:
                    continue
                if points[i].x== points[j].x and points[i].y==points[j].y:
                    dup+=1
                    continue
                slope=self.calculate_slope(points[j],points[i])
                if slope in slopeList.keys():
                    slopeList[slope]+=1
                else:
                    slopeList[slope]=1
            res=max(res,max(slopeList.values())+dup)
        return res
    def calculate_slope(self,a,b):
        if a.x==b.x:
            return 'inf'
        else:
            return float((b.y-a.y))/float((b.x-a.x))
#given array A and B, write function to find the smallest window in A that covers all numbers in B
class Solution:
    # @return a string
    def minWindow(self, S, T):
        count1={}
        for char in T:
            if char not in count1:count1[char]=1
            else:count1[char]+=1
        count=len(T)
        start=0;minSize=len(S)+1;minStart=0
        for end in range(len(S)):
            if S[end] in count1:
                count1[S[end]]-=1
                if count1[S[end]]>=0:
                    count-=1
            if count==0:
                while True:
                    if S[start] in count1:
                        if count1[S[start]]<0:
                            count1[S[start]]+=1
                        else:
                            break;
                    start+=1
                if minSize>end-start+1:
                    minSize=end-start+1;minStart=start
        if minSize==len(S)+1:
            return ''
        return S[minStart:minStart+minSize]
#Largest Rectangle in Histogram
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack=[]
        area=0
        i=0
        while i<len(height):
            if stack==[] or height[i]>height[stack[-1]]:
                stack.append(i)
            else:
                curr=stack.pop()
                width=i if stack==[] else i-stack[-1]-1
                area=max(area,width*height[curr])
                i-=1
            i+=1
        while stack:
            curr=stack.pop()
            width=i if stack==[] else len(height)-stack[-1]-1
            area=max(area,width*height[curr])
        return area
#Integer to roman
#整数（1~3999）到罗马数字的转换。字母前置表示减法，例如CM表示M-C=1000-100=900，XL表示L-X=50-10=40
class Solution:
    # @return a string
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list
#Roman to integer
#将罗马数字转换成对应的整数。首先将罗马数字翻转，从小的开始累加，如果遇到CM（M-C=1000-100=900）这种该怎么办呢？因为翻转过来是MC，M=1000先被累加，所以使用一个last变量，把M记录下来，如果下一个数小于M，那么减两次C，然后将C累加上，这个实现比较巧妙简洁
class Solution:
    # @return an integer
    def romanToInt(self, s):
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        sum=0
        s=s[::-1]
        last=None
        for x in s:
            if last and numerals[x]<last:
                sum-=2*numerals[x]
            sum+=numerals[x]
            last=numerals[x]
        return sum
#add two linked lists without reverse in O(n) time using constant space	
'''	
	private void swap(SLinkedList a, SLinkedList b) {
		Node tNode = a.head;
		a.head = b.head;
		b.head = tNode;
	}

	public void add(int[] arr, int[] brr) {

		SLinkedList aList = new SLinkedList(arr);
		SLinkedList bList = new SLinkedList(brr);

		if (aList.size() == 0) {
			sum.head = bList.head;
			return;
		} else if (bList.size() == 0) {
			sum.head = aList.head;
			return;
		}

		int aSize = aList.size();
		int bSize = bList.size();

		if (aSize == bSize)
			sum.head = addSameSize(aList.head, bList.head, carry);
		else {
			int diff = Math.abs(aSize - bSize);

			if (aSize < bSize) {
				swap(aList, bList);
			}

			Node cNode = aList.head;
			while (diff > 0) {
				cNode = cNode.next;
				diff--;
			}

			sum.head = addSameSize(cNode, bList.head, carry);
			sum.head = addCarryToRemaining(aList.head, cNode, carry);
		}

		if (carry > 0) {
			Node nNode = new Node(carry);
			sum.count++;
			nNode.next = sum.head;
			sum.head = nNode;
		}

	}

	private Node addSameSize(Node a, Node b, int c) {
		if (a == null)
			return null;

		Node result = new Node();
		sum.count++;
		result.next = addSameSize(a.next, b.next, carry);
		int sumVal = a.val + b.val + carry;
		carry = sumVal / 10;
		sumVal %= 10;
		result.val = sumVal;
		return result;
	}

	private Node addCarryToRemaining(Node a, Node b, int c) {
		if (a == b)
			return sum.head;
		Node result = new Node();
		sum.count++;
		result.next = addCarryToRemaining(a.next, b, carry);
		int sumVal = a.val + carry;
		carry = sumVal / 10;
		sumVal %= 10;
		result.val = sumVal;
		return result;
	}
'''
'''
a) There is a square of nxn size which is comprised of n-square 1x1 squares. Some of these 1x1 squares are colored. Find the biggest subsquare which is not colored. 

b) Also asked to extend it to find the biggest area rectangle.
'''
def findSquareSubMatrixWithAllOnes(board):
	newBoard=[[0 for x in range(len(board[o]))] for x in range(len(board))]
	resMax=0
	for row in range(len(board)-1,-1,-1):
		for col in range(len(board[0])-1,-1,-1):
			if row==len(board)-1 or col==len(board[0])-1:
				newBoard[row][col]=board[row][col]
			elif board[row][col]==1:
				newBoard[row][col]=1+min(newBoard[row+1][col],newBoard[row][col+1],newBoard[row+1][col+1])
			resMax=max(resMax,newBoard[row][col])
	return resMax
'''
Lets say Square is N*N matrix. Colored cell=0, uncolored cell=1 
So problem reduces to finding out a square(rectangle) sub matrix containing all 1s. 
It can be done using DP with in O(N*N) with O(N*N) space. 
Scan the entire matrix and keep on increamenting(accumulate) the number of 1s. 
for any cell [i,j] if anyof [i-1,j-1] or [i][j-1] or [i-1][j] contains 0 then reinitailize the count (i mean again start count with 1).
void findMaxSubMatrix(int matrix[10][10], int row, int col)
{
	int sumMatrix[10][10]={0}, sum = -1;
	int i,j, bottomRight_i, bottomRight_j, topLeft_i, topLeft_j;
	
	/*initialize col 0 and row 0 of sum matrix same as given matrix*/
	for(i=0; i<row; i++)
		sumMatrix[i][0] = matrix[i][0];
	for(i=0; i<col; i++)
		sumMatrix[0][i] = matrix[0][i];	
	/*calculate the sum matrix*/
	for(i=1; i<row; i++)
		for(j=1; j<col; j++)
			if(matrix[i][j]==1)
				sumMatrix[i][j] = 1 + MIN(sumMatrix[i-1][j-1],sumMatrix[i][j-1],sumMatrix[i-1][j]);
			else
				sumMatrix[i][j] = 0;
	/*find the top left and bottom right indixes of square matrix*/		
	for(i=1; i<row; i++)
		for(j=1; j<col; j++)
			if(sum<sumMatrix[i][j])
			{
				sum = sumMatrix[i][j];
				bottomRight_i = i;
				bottomRight_j = j;
			}		
	i=bottomRight_i;
	j=bottomRight_j;	
	while(i>;0 && j>;0)
	{
		if(((sumMatrix[i][j]-sumMatrix[i-1][j-1])>;0) && (sumMatrix[i-1][j-1] != 0))
		{
			i--;
			j--;
		}
		else
		{
			break;
		}
	}
	topLeft_i=i;
	topLeft_j=j;
	printf("Top left indexes: [%d,%d]\n", topLeft_i, topLeft_j);
	printf("Bottom right indexes: [%d,%d]\n", bottomRight_i, bottomRight_j);
}
'''
'''
For the square problem, there is an o(N^2) solution: 

when A[i][j] == 1 
def preLen = min( maxSquareSideLen(i-1,j), maxSquareSideLen(i,j-1) ) 
maxSquareSideLen(i,j) = A[i-preLen][j-preLen] == 1? preLen+1 : prelen; 

For rectangle problem, there is also a N^2 solution: 
first, you need to convert this matrix to another format: 
which A[i][j] indicate the max height between A[i][j] .... A[i][k] (between A[i][j] and A[i][k], they are all not colored). 

Then this become a finding max rectangle problem from histogram: 
see the detail description about this problem below which can be solved by O(n) solution 
oj.leetcode.com/problems/largest-rectangle-in-histogram/ 

for each row, we try to find max rectangle. so the complexity is also O(n^2)
// assume 1 not colored
	// and 0 colored
	int maxSquare(vector<vector<int>> &matrix)
	{
		int n = matrix.size();
		if (n == 0)
			return 0;
		int m = matrix[0].size();
		int max = 0;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				if (matrix[i][j] == 1)
				{
					int min = -1;
					if (j > 0){
						min = matrix[i][j-1];
					}

					if (i > 0)
					{
						if (min == -1 || min > matrix[i-1][j])
						{
							min = matrix[i-1][j];
						}
					}

					if (min == -1)
						min = 0;
					
					matrix[i][j] = matrix[i-min][j-min] > 0? min+1 : min;
					if (max < matrix[i][j])
					{
						max = matrix[i][j];
					}
				}
			}
		}
		return max*max;
	}
int maxRectangle(vector<vector<int>> &matrix)
	{
		int n = matrix.size();
		if (n == 0)
			return 0;
		int m = matrix[0].size();
		for(int i=1; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				if (matrix[i][j] == 1)
				{
					matrix[i][j] += matrix[i-1][j];
				}
			}
		}
		int max = 0;
		for(int i=0; i<n; i++)
		{
			int v = largestRectangleArea(matrix, m, i);
			if (v > max)
			{
				max = v;
			}
		}
		return max;
	}

	int largestRectangleArea(vector<vector<int>> &matrix, int m, int k) {
		vector<int> vm(m, 0);

		vector<int> v;
		vector<int> vh;
		for(int i = 0;i<m; i++)
		{
			int h = matrix[k][i];
			int start = i;
			while (v.size() > 0 && h <= vh[v.size()-1])
			{
				start = v[v.size()-1];
				v.pop_back();
				vh.pop_back();
			}

			v.push_back(start);
			vh.push_back(h);

			vm[i] = (i-start +1) * h;
		}

		v.clear();
		vh.clear();

		int max = 0;
		for(int i = m-1;i>= 0; i--)
		{
			int h = matrix[k][i];
			int start = i;
			while (v.size() > 0 && h <= vh[v.size()-1])
			{
				start = v[v.size()-1];
				v.pop_back();
				vh.pop_back();
			}

			v.push_back(start);
			vh.push_back(h);

			vm [i] += (start -i + 1 -1) *h;
			if (vm [i] > max)
			{
				max = vm [i];
			}
		}
		return max;
	}
'''
#find all prime factors of a number
def primeFactors(n):
	res=[]
	#add the number of 2s that divide n
	while n%2==0:
		res.append(2)
		n=n/2
	#n must be odd at this point, so we can skip one element(Note u=u+2)
	for i in range(3,(n**0.5)+1,2):
		#while i divides n, print i and divide n
		while n%i==0:
			res.append(i)
			n=n/i
	#this condition is to handle the case when n is a prime number greater than 2
	if n>2:
		res.append(n)
	return res
#print all the primes below a certain number
public void findPrimes(n){
	List<Integer> res=new ArrayList<Integer>();
	for(int i=2;i<n;i++){
		if(isPrime(i)){
			res.add(i);
		}
	}
}
public boolean isPrime(n){
	for(int i=2;i<Math.sqrt(n);i++){
		if(n%i==0){
			return false;
		}
	}
	if(n==2){
		return false;
	}
	return true;
}
def runEratosthenesSieve(upperBound):
	upperBoundRoot=int(upperBound**0.5)
	isComposite=[False for i in range(upperBound+1)]
	res=[]
	for m in range(2,upperBoundRoot+1):
		if not isComposite[m]:
			res.append(m)
			for k in range(m*m,upperBound+1,m):
				isComposite[k]=True
	for m in range(upperBoundRoot,upperBound+1):
		if not isComposite[m]:
			res.append(m)
	return res
#find missing number range
def findMissingNumber(range,input):
	res=[]
	numDict={}
	for i in input:
		numDict[i]=1
	i=range[0]
	while i<=range[1]:
		if i in numDict:
			i+=1
		else:
			p=[0,0]
			j=i
			p[0]=j
			while j<=range[1] and j not in numDict:
				j+=1
			p[1]=j-1
			res.append(p)
			i=j
	return res
#super prime problem,  定义为所有前缀是prime的数，比如239，打印所有长度为N的super prime
#generate all prime and check
def runEratosthenesSieve(upperBound):
	upperBoundRoot=int(upperBound**0.5)
	isComposite=[False for i in range(upperBound+1)]
	res=[]
	for m in range(2,upperBoundRoot+1):
		if not isComposite[m]:
			res.append(m)
			for k in range(m*m,upperBound+1,m):
				isComposite[k]=True
	for m in range(upperBoundRoot,upperBound+1):
		if not isComposite[m]:
			res.append(m)
	return res
#Find the next in order node of given node in binary tree. Write the program of same. pointer to parent node is given. successor
def getNextInorderNode(node):
	if node is None:
		return node
	tmp=node.right
	if tmp:
		while tmp.left:
			tmp=tmp.left
		return tmp
	tmp=node
	while tmp.parent and tmp.parent.right==tmp:
		tmp=tmp.parent
	if tmp.parent is None:
		return None
	elif tmp.parent.right!=tmp and tmp.parent.left==tmp:
		tmp.parent.left=tmp:
			return tmp.parent
#flatten a binary tree
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root:
            if root.left:
                self.flatten(root.left)
                curr=root.left
                while curr.right:
                    curr=curr.right
                curr.right=root.right
                root.right=root.left
                root.left=None
            if root.right:
                self.flatten(root.right)
#Write a function that given a sequence and a number b between [-10,10] return a new sequence. Sequences are generated by this: http://en.wikipedia.org/wiki/Look-and-say_sequence a number b if equal to 0 the function will return the input sequence Valid sequences: 1 11 21 1211 111221 ... Example: input: 1211, +1 output: 111221 Example: input: 111221, -1 output: 1211
class Solution:
    # @return a string
    def countAndSay(self, n):
        def count(s):
            t='';count=0;curr='#'
            for i in s:
                if i!=curr:
                    if curr!='#':
                        t+=str(count)+curr
                    curr=i
                    count=1
                else:
                    count+=1
            t+=str(count)+curr
            return t
        s='1'
        for i in range(2,n+1):
            s=count(s)
        return s
#find the deepest node in a binary tree
def findDeepest(root):
	def dfs(root,level):
		if root:
			res=max(res,level)
			dfs(root.left,level+1)
			dfs(root.right,level+1)
	res=0
	dfs(root,0)
	return res
#given an integer array, find the number in the array that is nearest to the average of the array.如果改成一个可能随时加数进去的list,怎么找最近的数.
#binary search+记录数字总和,数据结构用tree.
#given a set of pairs, there are two strings in each pair, assume we can construct a tree using these pairs, print this tree 
#set： (a,b)(b,c)(a,d)(d,e)(d,f)(d,g)
'''
a
[space]b
[space][space]c
[space]d
[space][space]e
[space][space]f
[space][space]g
'''
def printTree(pairs):
	spaceDict={}
	for i in pairs:
		first=i[0]
		if first not in spaceDict:
			spaceDict[first]=0
			print first
		second=i[1]
		if second not in spaceDict:
			spaceDict[second]=spaceDict[first]+1
			print '[space]'*spaceDict[second]+second
			
#binary tree serialization/de-serialization, each node contains a string
#inorder+preorder+serialization both
#de-serialization both+construct binary tree from inorder and preorder			
def serialize(arrs):
	res=[]
	res.append(str(len(arrs))+'#')
	for word in arrs:
		res.append(str(len(word))+'%')
	for word in arrs:
		res.append(word)
	return ''.join(res)
def deserialize(s):
	sizeContent=s.split('#')
	length=int(sizeContent[0])
	s=s[len(sizeContent[0])+1:]
	eachSize=s.split('%')
	size=[]
	total=0
	for i in range(length):
		size.append(int(eachSize[i]))
		total+=size[i]
	content=s[len(s)-total:len(s)]
	result=[]
	for i in range(length):
		result.append(content[:size[i]])
		content=content[size[i]:]
	return result
def buildTree(self, preorder, inorder):
    if inorder==[]:return None
    value=preorder[0]
    index=inorder.index(value)
    root=TreeNode(value)
    root.left=self.buildTree(preorder[1:index+1],inorder[:index])
    root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
    return root
#family tree(check whether two people have same ancestor)
def lowestCommonAncestor(root,x,y):
	if root is None:
		return False,False,None
	leftx,lefty,leftLca=lowestCommonAncestor(root.left,x,y)
	if leftLca:
		return True,True,leftLca
	rightx,righty,rightLca=lowestCommonAncestor(root.right,x,y)
	if rightLca:
		return True,True,rightLca
	foundx=leftx or rightx or (root is x)
	foundy=lefty or righty or (root is y)
	return foundx,foundy, root if foundx and foundy else None
#merge two quadtree
#https://github.com/phishman3579/java-algorithms-implementation/blob/master/src/com/jwetherell/algorithms/data_structures/QuadTree.java
#http://www.2cto.com/kf/201405/305427.html
#convert a binary tree into a doubly linked spiral list
#get the height of the binary tree

'''
Logic here is, we start at the bottom, the last not on the final doubly linked list would be added first to the head. Then we traverse the tree at every level from right to left or left to right depending on the flag ‘ltr’. When we visit a node we add it to the beginning of the list. This way our tree is not being destroyed and the conversion starts from the bottom.
'''
def transferToDoublyList(Node root):
	def height(Node n):
		if n is None:
			reutrn 0
		h=1
		leftH=height(n.left)
		rightH=height(n.right)
		return h+max(leftH,rightH)
	def toListLevelOrder():
		ltr=True
		height=height(root)
		for i in range(height,0,-1):
			toListGivenLevel(root,i,ltr)
			ltr=!ltr
	def toListGivenLevel(node,depth,ltr):
		if node is None:
			return None
		if depth==1:
			if head is None:
				head=node
				head.left=head
				head.right=head
			else:
				last=head.right
				node.left=head
				node.right=last
				head.right=node
				last.left=node
				head=node
		elif d>1:
			if ltr:
				toListGivenLevel(node.right,depth-1,ltr)
				toListGivenLevel(node.left,depth-1,ltr)
			else:
				toListGivenLevel(node.left,depth-1,ltr)
				toListGivenLevel(n.right,depth-1,ltr)
	head=None
	toListLevelOrder()
	return head
#binary search tree (add,search,delete)
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
class Tree:
	def __init__(self):
		self.root=None
	def find(self,key):
		current=self.root
		while current.data!=key:
			if key<current.data:
				current=current.left
			else:
				current=current.right
			if current is None:
				return None
		return current
	def insert(self,data):
		newNode=Node(data)
		if self.root is None:
			self.root=newNode
		else:
			current=self.root
			parent=None
			while True:
				parent=current
				if data<current.data:
					current=current.left
					if current is None:
						parent.left=newNode
						return
				else:
					current=current.right
					if current is None:
						parent.right=newNode
						return
	def delete(self,key):
		current=self.root
		parent=self.root
		isLeftChild=True
		while current.data!=key:
			parent=current
			if key<current.data:
				isLeftChild=True
				current=current.left
			else:
				isLeftChild=False
				current=current.right
			if current is None:
				return False
		#if no children, simply delete it
		if current.left is None and current.right is None:
			if current is root:
				root=None
			elif isLeftChild:
				parent.left=None
			else:
				parent.right=None
		#if no right child, replace with left subtree
		elif current.right is None:
			if current is root:
				root=current.left
			elif isLeftChild:
				parent.left=current.left
			else:
				parent.right=current.left
		#if no left child, replace with right subtree
		elif current.left is None:
			if current is root:
				root=current.right
			elif isLeftChild:
				parent.left=current.right
			else:
				parent.right=current.right
		#two children, so replace with inorder successor
		else:
			#get successor of node to delete (current)
			successor=self.getSuccessor(current)
			# connect parent of current to successor instead
			if current is root:
				root=successor
			elif isLeftChild:
				parent.left=successor
			else:
				parent.right=successor
			#connect successor to current's left child
			successor.left=current.left
		return True
	def getSuccessor(self,delNode):
		successorParent=delNode
		successor=delNode
		current=delNode.right
		while current:
			successorParent=successor
			successor=current
			current=current.left
		if successor!=delNode.right:
			successorParent.left=successor.right
			successor.right=delNode.right
		return successor
def validateBST(root):
	def isValid(root,minVal,maxVal):
		if root is None:
			return True
		if root.val<=minVal or root.val>=maxVal:
			return False
		return isValid(root.left,minVal,root.val) and isValid(root.right,root.val,maxVal)
	return isValid(root,2147483647,-2147483648)
#binary tree traversal
# @param root, a tree node
# @return a list of integers
def postorderTraversal(self, root):
    stack=[]
    pre=None
    res=[]
    while stack or root:
        if root is not None:
            stack.append(root)
            root=root.left
        else:
            peek=stack[-1]
            if peek.right and pre!=peek.right:
                root=peek.right
            else:
                stack.pop()
                res.append(peek.val)
                pre=peek
    return res
# @param root, a tree node
# @return a list of integers
def preorderTraversal(self, root):
	res=[]
	stack=[None]
	while root:
		res.append(root.val)
		if root.right:
			stack.append(root.right)
		if root.left:
			stack.append(root.left)
		root=stack.pop()
	return res
# @param root, a tree node
# @return a list of integers
def inorderTraversal(self, root):
	res=[]
	stack=[]
	while stack or root:
		if root:
			stack.append(root)
			root=root.left
		else:
			root=stack.pop()
			res.append(root.val)
			root=root.right
	return res
#build a BST from an array
class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num)==0:
            return None
        left=0;right=len(num)-1
        middle=(left+right)/2
        root=TreeNode(num[middle])
        root.left=self.sortedArrayToBST(num[:middle])
        root.right=self.sortedArrayToBST(num[middle+1:])
        return root
'''
HASH VS BST
The main difference between hash table and trees is on two aspects: Implementation details and  behaviors and performance under different circumstance.
1.Hash table uses hash function to assign index to input data and put data into array under corresponding index.Theoretically,time complexity of insertion and looking-up is constant time (O(1)).
1.If the tree is balanced, it always takes O(log(n)) time to insert a new node or look up.O(log(n)) is not as fast as constant time but rather fast.(RB Tree, AVL Tree)
HashTable Drawbacks
1. As more data input comes, there is huge probability that collision shows up(separate chaining, open addressing)
2. You have to know approximate size of input data before initializing hash table(or resize)
3. Elements are unsorted
BST Advantage
1. Never meets collision, always log(n)(balanced tree)
2. Expandable(don't need to know the size)
3. sorted
When to use hashtable 
know data size, enough size, unsorted, most operations are looking up
When to use BST
don't know data size, sorted, keep adding or removing
'''
#given one binary search tree, find the Kth minimum value
def findKthMin(root,k):
	def finding(root,k):
		if root:
			finding(root.left,k)
			count+=1
			if count==k:
				return root.val
			finding(root.right,k)
	count=0
	return finding(root,k)
#given one binary search tree, find the Kth maximum value
def findKthMax(root,k):
	def finding(root,k):
		if root:
			finding(root.right,k)
			count+=1
			if count==k:
				return root.val
			finding(root.right,k)
	count=0
	return finding(root,k)
'''
function Select(t, i)
    // Returns the i'th element (zero-indexed) of the elements in t
    r ← size[left[t]]
    if i = r
        return key[t]
    else if i < r1
        return Select(left[t], i)
    else
        return Select(right[t], i - (r + 1))
每次当你往一个节点的右子树方向走的时候，默认该节点和它的左子树都是在第i个之前的，所以你只要在该节点的基础上找第 i-(r+1) 大的节点就可以了
'''
#string to float
def strToFloat(str):
	num=str.split('.')
	if len(num)>2:return None
	first=0;second=0
	neg=False
	if len(num[0])>0:
		if num[0][0]=='-':
			neg=True
			num[0]=num[0][1:]
		elif num[0][0]=='+':
			num[0]=num[0][1:]
	for i in num[0]:
		first=first*10+int(i)
	if len(num)>1:
		for i in num[1]:
			second=second*10+int(i)
		res=first+second*1.0/(10**len(num[1]))
	else:
		res=first
	return -res if neg else res
'''
A rooted binary tree with keys in its nodes has the binary search tree 
property (BST property) if, for every node, the keys in its left 
subtree are smaller than its own key, and the keys in its right 
subtree are larger than its own key. It has the heap property if, for 
every node, the keys of its children are all smaller than its own key. 
You are given a set of n binary tree nodes that each contain an 
integer i and an integer j. No two i values are equal and no two j
values are equal. We must assemble the nodes into a single binary tree 
where the i values obey the BST property and the j values obey the
heap property. If you pay attention only to the second key in each
node, the tree looks like a heap, and if you pay attention only to the 
first key in each node, it looks like a binary search tree.Describe a 
recursive algorithm for assembling such a tree
'''
'''
1. Find nodes with biggest j (we call it pivot) in node array. 
2. Partition the array into two parts, all elements in left part have i smaller than i of pivot while all elements in right part have i bigger than i of pivot. 
3. Use pivot as root of tree. 
4. set left sub-tree of root as a tree built from left part of array. 
5. set right sub-tree of root as a tree built from right part of array. 
6. return root. 

Average time complexity: O(NlogN) 
Worst time complecity: O(N^2)
'''
#solution one
def partitinBST(bstVal,heapVal,left,right):
	k=left
	for i in range(left+1,right+1):
		if heapVal[i]>heapVal[k]:
			k=i
	heapVal[k],heapVal[right]=heapVal[right],heapVal[k]
	bstVal[k],bstVal[right]=bstVal[right],bstVal[k]
	i=left-1
	for j in range(left,right):
		if bstVal[j]<=bstVal[right]:
			i+=1
			bstVal[i],bstVal[j]=bstVal[j],bstVal[i]
			heapVal[i],heapVal[j]=heapVal[j],heapVal[i]
	i+=1
	bstVal[i],bstVal[right]=bstVal[right],bstVal[i]
	heapVal[i],heapVal[right]=heapVal[right],heapVal[i]
	return i
def buildBSTHeap(bstVal,heapVal,left,right):
	if left>right:
		return None
	elif left==right:
		return TreeNode(bstVal[left],heapVal[right])
	k=partitionBST(bstVal,heapVal,left,right)
	root=TreeNode(bstVal[k],heapVal[k])
	root.left=buildBSTHeap(bstVal,heapVal,left,k-1)
	root.right=buildBSTHeap(bstVal,heapVal,k+1,right)
	return root
#solution 2
def insert(root,nodeToInsert):
	if root is None:
		return nodeToInsert
	else:
		if nodeToInsert.i<=root.i:
			root.left=insert(root.left,nodeToInsert)
		else:
			root.right=insert(root.right,nodeToInsert)
		return root
def construct(arr,resultTree,size):
	if size==0:return
	ind=0;maxInd=0
	while ind<size:
		if arr[ind].j>arr[maxInd].j:
			maxInd=ind
		ind+=1
	resultTree=insert(result,arr[maxInd])
	arr[maxInd],arr[size-1]=arr[size-1],arr[maxInd]
	construct(arr,resultTree,size-1)
#现在有父母，夫妻，孩子，父母和孩子，兄弟姐妹这些关系，给两个人，怎么查出有没有血缘关系
#tree,lowest common ancestor
#给一个基本的bst写2个function, first:return minimum node, second: return next big node,用这两个function, print the whole tree out and give out runtime
#Time Complexity: O(h) where h is height of tree.
def getNextInorderNode(node):
	if node is None:
		return node
	#If right subtree of node is not NULL, then succ lies in right subtree. Do following.Go to right subtree and return the node with minimum key value in right subtree.
	tmp=node.right
	if tmp:
		while tmp.left:
			tmp=tmp.left
		return tmp
	#If right sbtree of node is NULL, then succ is one of the ancestors. Do following.Travel up using the parent pointer until you see a node which is left child of it’s parent. The parent of such a node is the succ
	tmp=node.parent
	while tmp and tmp.right==node:
		node=tmp
		tmp=tmp.parent
	return tmp
#search from root
#Time Complexity: O(h) where h is height of tree.
def inorderSuccessor(root,n):
	if node is None:
		return node
	#If right subtree of node is not NULL, then succ lies in right subtree. Do following.Go to right subtree and return the node with minimum key value in right subtree.
	tmp=node.right
	if tmp:
		while tmp.left:
			tmp=tmp.left
		return tmp
	succ=None
	# If right sbtree of node is NULL, then start from root and us search like technique. Do following.Travel down the tree, if a node’s data is greater than root’s data then go right side, otherwise go to left side.
	while root:
		if n.data<root.data:
			succ=root
			root=root.left
		elif n.data>root.data:
			root=root.right
		else:
			break
	return succ
#write a graph data structure
#http://www.python-course.eu/graphs_python.php
#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path