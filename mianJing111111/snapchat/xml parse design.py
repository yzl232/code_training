# encoding=utf-8

'''

xml parse不是让你设计一个真正的复杂的parser. 比如给你一个xml
<a>
    <b>
        <c>foo</c>
        <c>bar</c>
    </b>
    <d>abc</d>
</a>

让你自己定义结构，构建成一个类似于树的形式，返回根节点，在这里根节点就是a，至于怎么定义节点，类里面有什么这些都由你设计。


现在有一个Tokenizer，返回的Token都是XML标签或者内容，比如(open, html)(inner, hello)(close, html)表示<html>hello</html>，每一个括号及其内容是一个Token，请问如何表示这个XML文件。
这题首先要想清楚的是，如何表示XML，因为XML是典型的一父多子，我们用树来表示比较好。然后分析下如何用Tokenizer，Tokenizer有点像Iterator，每当我们用Tokenizer拿到一个Token时，如果这是一个Open的Token，我们需要新建一个节点，这个新节点下面也有可能有新节点。如果是一个Inner的Token，我们也需要新建一个节点，但这个节点下面不会有新的节点。如果是一个Close的Token，我们不需要新节点，而且需要保证上一个Open节点不再接纳新节点了，而对于新节点则要附在上一层的节点后面。这里，我们用栈可以保留上一层的节点信息，帮助我们建树。如果这是一个Open的Token，我们需要新建一个节点加入上一层节点后面，并加入栈中。如果是一个Inner的Token，我们也需要新建一个节点加到上一层节点后面，但不加入栈中。如果是一个Close的Token，则把上一层节点弹出栈。

XML parser, build a map to represent XML given tokenizer.Next() -> (open,name), (inner,content), (close,name), 就是一个 tree transversal
given a string, return whether can use the character to construct target string, 裸hashmap



XML parser 是求map structure output,  为什么LZ 只有一个build function?
Input = [(open, a), (inner, 1) ,(open, b), (inner, 2), (open, c), (inner, 3), (close, c), (close, b),  (open, d), (inner, 4), (close, d) (close, a)]. 鍥磋鎴戜滑@1point 3 acres
Output => ?  . from: 1point3acres.com/bbs
Should it be following

a: (content = 1, {b: XMLMap, d: XMLMap})
b: (content = 2, {c: XMLMap}
c: (content = 3, {}).鐣欏璁哄潧-涓€浜�-涓夊垎鍦�
d: (content = 4, {})

这题首先要想清楚的是，如何表示XML，因为XML是典型的一父多子，我们用树来表示比较好。然后分析下如何用Tokenizer，Tokenizer有点像Iterator，每当我们用Tokenizer拿到一个Token时，如果这是一个Open的Token，我们需要新建一个节点，这个新节点下面也有可能有新节点。如果是一个Inner的Token，我们也需要新建一个节点，但这个节点下面不会有新的节点。如果是一个Close的Token，我们不需要新节点，而且需要保证上一个Open节点不再接纳新节点了，而对于新节点则要附在上一层的节点后面。这里，我们用栈可以保留上一层的节点信息，帮助我们建树。如果这是一个Open的Token，我们需要新建一个节点加入上一层节点后面，并加入栈中。如果是一个Inner的Token，我们也需要新建一个节点加到上一层节点后面，但不加入栈中。如果是一个Close的Token，则把上一层节点弹出栈。
'''

class XMLMap:
    def __init__(self, type, val):
        self.val = val
        self.children = []
        self.type = type
        
class Parser:
    def parse(self, s):
        tokens = s.split(")")
        tokens = [x[1:].split(",") for x in tokens][:-1]
        if len(tokens)<1: return
        root = XMLMap(tokens[0][0], tokens[0][1])
        stack = [root]
        i = 1; n=len(tokens)
        while stack and i<n:
            cur = XMLMap(tokens[i][0], tokens[i][1])
            parent = stack[-1]
            if cur.type == "open":
                parent.children.append(cur)
                stack.append(cur)
            elif cur.type == "close":  stack.pop()
            elif cur.type == "inner":   parent.children.append(cur)
            i+=1
        return root


s = Parser()
def printTree(root, depth):
    print root.type, root.val, depth
    for x in root.children:   printTree(x, depth+1)

printTree(s.parse("(open,html)(open,head)(inner,welcome)(close,head)(open,body)(close,body)(close,html)"), 1)

'''
public class XMLParser {

    public static void main(String[] args){
        XMLParser xml = new XMLParser();
        XMLNode root = xml.parse("(open,html)(open,head)(inner,welcome)(close,head)(open,body)(close,body)(close,html)");
        xml.printXMLTree(root, 0);
    }

    public XMLNode parse(String str){
        // 以右括号为delimiter
        StringTokenizer tknz = new StringTokenizer(str, ")");
        Stack<XMLNode> stk = new Stack<XMLNode>();
        // 将第一个open节点作为根节点压入栈中
        XMLNode root = convertTokenToTreeNode(tknz.nextToken());
        stk.push(root);
        while(!stk.isEmpty()){
            if(!tknz.hasMoreTokens()){
                break;
            }
            XMLNode curr = convertTokenToTreeNode(tknz.nextToken());
            // 得到上一层节点
            XMLNode father = stk.peek();
            // 根据当前节点的类型做不同处理
            switch(curr.type){
                // 对于Open节点，我们把它加入上一层节点的后面，并加入栈中
                case "open":
                    father.children.add(curr);
                    stk.push(curr);
                    break;
                // Close节点直接把上一层Pop出来就行了，这样就不会有新的节点加到上一层节点后面
                case "close":
                    stk.pop();
                    break;
                // Inner节点只加到上一层节点后面
                case "inner":
                    father.children.add(curr);
                    break;
            }
        }
        return root;
    }

    private XMLNode convertTokenToTreeNode(String token){
        token = token.substring(1);
        String[] parts = token.split(",");
        return new XMLNode(parts[0], parts[1]);
    }

    private void printXMLTree(XMLNode root, int depth){
        for(int i = 0; i < depth; i++){
            System.out.print("-");
        }
        System.out.println(root.type + ":" + root.value);
        for(XMLNode node : root.children){
            printXMLTree(node, depth + 1);
        }
    }
}

class XMLNode {
    String type;
    String value;
    List<XMLNode> children;

    XMLNode(String type, String value){
        this.type = type;
        this.value = value;
        this.children = new ArrayList<XMLNode>();
    }
}
'''