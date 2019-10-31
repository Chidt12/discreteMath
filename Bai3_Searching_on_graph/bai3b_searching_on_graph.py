import csv
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

array_words  = []
with open('sgb-words.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        array_words.append(row[0])

def list_incident(word, array_words):
    array = []
    for w in array_words:
        cnt = 0
        for i in range(len(word)):
            if i != 0 and word[i] in w:
                if word.count(word[i]) == w.count(word[i]):
                    cnt += 1
        if cnt == 4:
            array.append(w)
    return array

class GraphDirected:

    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self,word, incident):
        self.graph[word].append(incident)

    def DFS(self, start, discovered, stack = None):
        for v in self.graph[start]:
            if v not in discovered:
                discovered[v] = [start, v]
                self.DFS(v, discovered)
        if stack is not None:
            stack.append(start)


    def getTranpose(self):
        g = GraphDirected()
        for w in self.graph.keys():
            for u in self.graph[w]:
                g.add_edge(u, w)
        return g

    def countandfindSCCs(self, word = None):
        stack = []
        discovered = {}
        for w in self.graph.keys():
            if w not in discovered:
                discovered[w] = None
                self.DFS(w, discovered,stack)
        graph = self.getTranpose()
        discovered = {}
        count = 0
        while len(stack) > 0:
            i = stack.pop()
            if i not in discovered:
                discovered[i] = None
                graph.DFS(i, discovered)
                count += 1
        if word is not None:
            array = []
            if word in discovered:
                root_word = word
                walk_edge = discovered[word]
                while walk_edge is not None:
                    walk = walk_edge[0]
                    root_word = walk
                    walk_edge = discovered[walk]
                small_discovered = {}
                small_discovered[root_word] = None
                graph.DFS(root_word, small_discovered)

                for w in small_discovered.keys():
                    array.append(w)
            return array
        return count

g = GraphDirected()
for word in array_words:
    array_incident = list_incident(word, array_words)
    for w in array_incident:
        g.add_edge(word, w)

# print(g.countandfindSCCs("arses"))
# LIst các từ trong cùng liên thông mạnh với input là từ


print(g.countandfindSCCs())
# số liên thông mạnh trong đồ thị g