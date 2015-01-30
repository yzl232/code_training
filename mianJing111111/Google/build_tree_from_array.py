# encoding=utf-8
'''
Complete the below function which takes an arraylist and displays the list in the expected output

public class TreePrinter {
public static void printTree(Iterable<Relation> rs) {
// your code

}
}

public static class Relation {
String parent;
String child;
public Relation(String parent, String child) { ... }
}
}

Example input:
List<Relation> input = newArrayList();

input.add(new Relation(“animal”, “mammal”));
input.add(new Relation(“animal”, “bird”));
input.add(new Relation(“lifeform”, “animal”));
input.add(new Relation(“cat”, “lion”));
input.add(new Relation(“mammal”, “cat”));
input.add(new Relation(“animal”, “fish”));

TreePrinter.printTree(input);

Expected output:
line 1: lifeform
line 2: animal
line 3: mammal
line 4: cat
line 5: lion
line 6: bird
line 7: fish
'''

#关键在于找到root


class Relation:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child

class Solution:  #可以用hashmap  build 简单的node: children属性。
    def buildTree(self, relations):
        d = {};  notRoot = set()
        for rs in relations:
            if d[rs[0]] not in d:  d[rs[0]] = []
            d[rs[0]].append(rs[1])
            notRoot.add(rs[1])
        roots=[ x  for x in d if x not in notRoot ]   # 找root
        self.d = d #build  tree   有了roots。 有了图。 算是已经建好了hashmap形式的tree了。
        for x in roots: self.dfs(x)

    def dfs(self, root):
        print root.val
        for child in self.d[root]:
            self.dfs(child)
