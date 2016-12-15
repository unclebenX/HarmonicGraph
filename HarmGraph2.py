import numpy as np
import pylab as pl

class HarmGraph:
    graph = []
    signalList = []
    n = 0
    N = 40

    def __init__(self, edgeList):
        self.graph = edgeList
        self.n = len(edgeList)
        self.signalList = [[] for i in range(self.n)]
        return

    def add(self,s1,s2):
        return s1 + list(set(s2) - set(s1))

    def throwSignal(self, vertex):
        self.signalList[vertex] = [vertex]
        return

    def spreadSignal(self):
        signalList = [[] for i in range(self.n)]
        for vertex in range(self.n):
            for neighbour in self.graph[vertex]:
                signalList[neighbour] = self.add(signalList[neighbour], self.signalList[vertex])
        self.signalList = signalList
        return

    def modulateSignal(self):
        for vertex in range(self.n):
            self.signalList[vertex] = [a + vertex for a in self.signalList[vertex]]
        return

    def signalPropagation(self,vertex):
        self.signalList = [[] for i in range(self.n)]
        self.throwSignal(vertex)
        for i in range(self.n - 1):
            self.spreadSignal()
            self.modulateSignal()
        self.spreadSignal()
        return self.signalList[vertex]

#graph = [[5,1],[0,2],[1,3],[2,4],[3,5],[4,0]]
graph = [[1,2,3,4],[0,2],[1,0,3],[0,4],[3,0]]
hG = HarmGraph(graph)
for i in range(len(graph)):
    print hG.signalPropagation(i)
    print len(graph)*(len(graph)-1)/2 in hG.signalPropagation(i)
