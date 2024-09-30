class Viesis:
    def __init__(self, vards, parole):
        self.vards = vards
        self.parole = parole
        self.__id=3
    
    def drukaVardu(self):
        print("Viesis "+f"{self.vards}"+" izveidots")
    
    def drukaParoli(self):
        print("Lietotajs "+f"{self.parole}"+" parole izveidota")

    def izdrukaID(self):
        print(self.__id)

class Darbinieks(Viesis):
    def drukaVardu(self):
        print("Administrators " +f"{self.vards}"+" izveidots")

vards = "Elina"
parole = "eeeee"
viesis1 = Viesis(vards, parole)

vards = "Daina"
parole = "ddddddd"
darbinieks1 = Darbinieks(vards, parole)

visi = [viesis1, darbinieks1]
for x in visi:
    x.drukaVardu()
    x.drukaParoli()