from numpy.lib.scimath import log2
from operator import itemgetter
import math

Shannon_Fano_dict = {}


def Shannon_Fano_coding(seq, code):
    a = {}
    b = {}
    if len(seq) == 1:
        Shannon_Fano_dict[seq.popitem()[0]] = code
        return 0
    for i in sorted(seq.items(), key=itemgetter(1), reverse=True):
        if sum(a.values()) < sum(b.values()):
            a[i[0]] = seq[i[0]]
        else:
            b[i[0]] = seq[i[0]]
    Shannon_Fano_coding(a, code + "0")
    Shannon_Fano_coding(b, code + "1")


message = "example skh mw dcok"
print(message)
count = {}
for c in message:
    if c not in count:
        count[c] = 1
    else:
        count[c] += 1
for c in sorted(count):
    print(c, "=>", count[c] / len(message))

print("Count od symbols: ", len(count))
print("Shannon-Fano: ")
Shannon_Fano_coding(count, "")
for i in sorted(Shannon_Fano_dict):
    print(i, "=", Shannon_Fano_dict[i])
code_mes = ""
for i in message:
    code_mes += Shannon_Fano_dict[i]
print("Len: ", len(code_mes), "\nCode: ", code_mes)