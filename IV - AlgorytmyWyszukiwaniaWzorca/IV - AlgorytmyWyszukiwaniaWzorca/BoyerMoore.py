class BoyerMoore:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)
        self.skip = []
        for i in range(256): self.skip.append(-1)
        for i in range(self.m): self.skip[ord(pattern[i])] = self.m

    def search(self):
        for i in range(self.n + self.m + 1):
            skip = 0
            for j in range(self.m-1, -1, -1):
                if self.text[i+j] != self.pattern[j]:
                    skip = j - self.skip[ord(self.text[i+j])]
                    if skip < 1: skip = 1
                    break

            if skip == 0:
                print(f"Znaleziono na indexie: {i}")
                return

            i += skip

        print("Brak w przykładu w tekście")
        return


p1 = "aa"
t1 = "aaaaaaaa"
bm = BoyerMoore(t1, p1)
bm.search()

p2 = "abc"
t2 = "abdabeabfabc"
bm = BoyerMoore(t2,p2)
bm.search()

p3 = "aab"
t3 = "aaabaacbaab"
bm = BoyerMoore(t3,p3)
bm.search()