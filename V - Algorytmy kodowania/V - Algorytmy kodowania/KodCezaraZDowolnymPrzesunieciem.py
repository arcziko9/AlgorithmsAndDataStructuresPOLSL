import string

class Cesar:
    def __init__(self, tab):
        self.tab = tab.upper()

    def Cesar(self, text):
        key = 1
        alphabet = string.ascii_uppercase
        code = alphabet[key:] + alphabet[:key]
        tab = str.maketrans(alphabet, key)
        return text.translate(tab)

    def Cesar_u(self, text):
        key = 1
        alphabet = string.ascii_uppercase
        code = alphabet[:key] + alphabet[key:]
        tab = str.maketrans(alphabet, key)
        return text.translate(tab)

    def __str__(self):
        result = "Słowo: "+self.tab +"\n"
        result+= "Zaszyfrowane: " + self.Cesar(self.tab) + "\n"
        result += "Odszyfrowane: " + self.Cesar_u(self.tab) + "\n\n"
        return wynik


file = open('cezar.txt','r')
line = file.readline()
data = []
while line:
    dane.append(line.strip())
    line=file.readline()

for text in data:
    print(Cesar(text), end = " ")