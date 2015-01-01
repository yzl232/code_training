#先解释idea。
# brute force。  check every ch if it is an vowel
#  xor。 然后check only one bit of the 8 bits is different.


def removeVowels(s):
    return ''.join(ch for ch in s if ch not in 'aeiouAEIOU')

def grayCode(byte1, byte2):
    return (byte1 ^ byte2)  in [1<<i for i in range(7)]
#方法2
'''
n =byte1 ^ byte2
return n!=0 and n&(n-1)==0
'''


'''
# stringBuilder 不可变长度。 string可变长度。

	public static String removeVowels(String s) {
		StringBuilder sb = new StringBuilder();
		String v1 = "aeiouAEIOU";
		for (int i = 0; i < s.length(); i++) {
			if (v1.indexOf(s.charAt(i)) > -1)
				continue;
			sb.append(s.charAt(i));
		}
		return sb.toString();
'''
#原理xor
'''
	public static int greyCode(byte element1, byte element2) {
		byte res = (byte) (element1 ^ element2);
		for (int i = 0; i <= 7; i++) {
			byte temp = (byte) (1 << i);
			if (temp == res) {
				return 1;
			}
		}
		System.out.println("No");
		return 0;
	}
'''
# amazon
'''
2) Given two hexadecimal numbers find if they can be consecutive in gray code
For example: 10001000, 10001001
return 1
since they are successive in gray code



def right(s1, s2):
    return s2 in s1+s1

	public static int rightRotate(String word1, String word2) {
		if (word1 == null || word2 == null || word1.length() == 0
				|| word2.length() == 0 || word1.length() != word2.length()) {
			return -1;
		}
		String str = word1 + word1;
		return str.indexOf(word2) != -1 ? 1 : -1;
	}
'''