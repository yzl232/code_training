class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack, tokens = [], path.split("/")
        for token in tokens:
            if token != ".." and token != "." and token:   stack.append(token)
            elif token=='..':
                if stack: stack.pop()
        return "/" + "/".join(stack)

'''
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        paths = path.split('/')
        results = ''
        for i in paths:
            if i!= '..' and i!='' and i!='.':
                results += '/'+i
            elif i=='..':
                if results != '':
                    results = '/'.join(results.split('/')[:-1])     #以前的方法用了O(n2)。  很不好
        return results if results !='' else '/'
'''