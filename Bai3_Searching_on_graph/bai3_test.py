import csv
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

array_words  = []
with open('sgb-words.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        array_words.append(row[0])

def list_incident(word_index, array_words):
    array = []
    word = array_words[word_index]
    for w_index in range(len(array_words)):
        w = array_words[w_index]
        if w_index != word_index:
            cnt = 0
            for i in range(len(word)):
                if i != 0 and word[i] in w:
                    if word[1:].count(word[i]) <= w.count(word[i]):
                        cnt += 1
            if cnt == 4:
                array.append(w_index)
    return array


class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices
        self.graph = defaultdict(list)
   
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def DFSUtil(self,v,visited): 
        visited[v]= True
        print(v, end=" ")
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited) 
  
  
    def fillOrder(self,v,visited, stack): 
        visited[v]= True
        # print("fill__",v)
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack = stack.append(v) 
      

    def getTranspose(self): 
        g = Graph(self.V) 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g

    def countSCCs(self):

        stack = []
        count = 0
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        gr = self.getTranspose()
        visited =[False]*(self.V)
        while len(stack) > 0:
            i = stack.pop()
            if visited[i]==False:
                count+=1
                gr.DFSUtil(i, visited)
                print(" ")
        return count

g = Graph(len(array_words))
for w_index in range(len(array_words)):
    array = list_incident(w_index, array_words)
    for v in array:
        g.addEdge(w_index, v)


print(g.countSCCs())







# print ("Following are strongly connected components " +
#                            "in given graph") 
# g.printSCCs() 
#This code is contributed by Neelam Yadav 