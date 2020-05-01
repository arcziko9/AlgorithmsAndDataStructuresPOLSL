class KMP:
    def partial(self, pattern):
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        partial, ret, j = self.partial(P), [], 0 
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]     
            if T[i] == P[j]: 
                j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
        return ret




kmp = KMP()

p1 = "aa"
t1 = "aaaaaaaa"

print(kmp.search(t1, p1))



p2 = "abc"
t2 = "abdabeabfabc"

print(kmp.search(t2, p2))



p3 = "aab"
t3 = "aaabaacbaab"

print(kmp.search(t3, p3))