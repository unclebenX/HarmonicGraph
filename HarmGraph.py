import numpy as np
import cmath as c
import pylab as pl

class HarmGraph:
    graph = []
    signalList = []
    n = 0
    N = 40

    def __init__(self, edgeList):
        self.graph = edgeList
        self.n = len(edgeList)
        self.signalList = [np.array([0. for i in range(self.N)]) for i in range(self.n)]
        return

    def throwSignal(self, vertex):
        self.signalList[vertex] = np.array([np.cos(2*np.pi*k*vertex/(self.N)) for k in range(self.N)])
        return

    def spreadSignal(self):
        signalList = [np.array([0 for i in range(self.N)]) for i in range(self.n)]
        for vertex in range(self.n):
            for neighbour in self.graph[vertex]:
                signalList[neighbour] = signalList[neighbour] + self.signalList[vertex]
        self.signalList = signalList
        return

    def modulateSignal(self):
        for vertex in range(self.n):
            modulationSignal = np.array([np.cos(np.pi*k*2*vertex/self.N) for k in range(self.N)])
            self.signalList[vertex] = np.multiply(self.signalList[vertex], modulationSignal)
        return

    def normalize(self):
        """
        for vertex in range(self.n):
            ff = np.fft.fft(self.signalList[vertex])
            signal = np.array([0. for i in range(self.N)])
            for k in range(self.N):
                if abs(ff[k]) >= 1:
                    modulationSignal = np.array([np.cos(np.pi*k*2*vertex/self.N) for k in range(self.N)])
                    signal = signal + modulationSignal
            self.signalList[vertex] = signal
        """

    def signalPropagation(self,vertex):
        self.throwSignal(vertex)
        #x = np.linspace(0.,10.,100)
        #pl.plot(x,np.real(self.signalList[0]))
        #pl.show()
        x = np.linspace(0.,10.,self.N)
        for i in range(self.n - 1):
            self.spreadSignal()
            self.modulateSignal()
            self.normalize()
            print self.signalList[0]
        self.spreadSignal()
        #pl.plot(x,np.real(self.signalList[0]))
        #pl.show()
        ff = np.fft.fft(self.signalList[vertex])
        pl.plot(np.arange(self.N), ff)
        pl.show()
        return ff[self.n*(self.n+1)/2]

#graph = [[5,1],[0,2],[1,3],[2,4],[3,5],[4,0]]
graph = [[1,2,3,4],[0,2],[1,0],[0,4],[3,0]]
hG = HarmGraph(graph)
for i in range(len(graph)):
    print hG.signalPropagation(0)
