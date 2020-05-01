from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def nowa_krawedz(self, poczatek, koniec):
        self.graph[poczatek].append(koniec)

    def bfs(self, s):
        odwiedzony = [False] * (len(self.graph))
        kolejka = []
        kolejka.append(s)
        odwiedzony[s] = True
        while kolejka:
            s = kolejka.pop(0)
            print(s, end=" ")
            for i in self.graph[s]: 
                if odwiedzony[i] == False:
                    kolejka.append(i)
                    odwiedzony[i] = True


graf = Graph()
graf.nowa_krawedz(0, 1)
graf.nowa_krawedz(0, 2)
graf.nowa_krawedz(1, 2)
graf.nowa_krawedz(2, 0)
graf.nowa_krawedz(2, 3)
graf.nowa_krawedz(3, 3)
graf.bfs(0)
