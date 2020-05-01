from collections import defaultdict


class Graph:

    def __init__(self):
        self.graf = defaultdict(list)

    def nowa_krawedz(self, poczatek, koniec):
        self.graf[poczatek].append(koniec)

    def dfs(self, koniec):
        odwiedzone = [False] * (len(self.graf))
        self.temp(koniec, odwiedzone)

    def temp(self, koniec, odwiedzone):
        odwiedzone[koniec] = True 
        print(koniec, end=' ')
        for i in self.graf[koniec]:
            if odwiedzone[i] == False:
                self.temp(i, odwiedzone)


graf = Graph()
graf.nowa_krawedz(0, 1)
graf.nowa_krawedz(0, 2)
graf.nowa_krawedz(1, 2)
graf.nowa_krawedz(2, 0)
graf.nowa_krawedz(2, 3)
graf.nowa_krawedz(3, 3)
graf.dfs(0)
