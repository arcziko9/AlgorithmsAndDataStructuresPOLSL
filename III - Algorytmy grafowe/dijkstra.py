import networkx as nx


def trasa(rodzic, start, koniec):
    sciezka = [koniec]
    while sciezka[-1] != start:
        sciezka.append(rodzic[sciezka[-1]])
    sciezka.reverse()
    return sciezka


def dijkstra(graf, poczatek, koniec):
    kolejka = []
    odwiedzone = {}
    dyst = {}
    najkr_dyst = {} 
    rodzic = {}
    for wierzcholek in range(len(graf)):
        dyst[wierzcholek] = None
        odwiedzone[wierzcholek] = False
        rodzic[wierzcholek] = None
        najkr_dyst[wierzcholek] = float("inf")

    kolejka.append(poczatek)
    dyst[poczatek] = 0
    while len(kolejka) != 0:
        aktualny = kolejka.pop(0)
        odwiedzone[aktualny] = True
        if aktualny == koniec:
            print(trasa(rodzic, poczatek, koniec))

        for sasiad in graf[aktualny]:
            if not odwiedzone[sasiad]:
                dyst[sasiad] = dyst[aktualny] + 1
                if dyst[sasiad] < najkr_dyst[sasiad]:
                    najkr_dyst[sasiad] = dyst[sasiad]
                    rodzic[sasiad] = aktualny
                    kolejka.append(sasiad)
    print(dyst)
    print(najkr_dyst)
    print(rodzic)
    print(koniec)


graf = nx.Graph()
graf.add_weighted_edges_from([(0, 1, 0), (1, 2, 0)])
dijkstra(graf, 0, 2)
nx.draw(graf)
