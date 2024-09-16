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
    def drukaaVardu(self):
        print("Administrators " +f"{self.vards}"+" izveidots")


vards = "Elina"
parole = "eeeee"
viesis1 = Viesis(vards, parole)
viesis1.drukaVardu()
viesis1.drukaParoli()
#viesis1.izdrukaID()
#print(viesis1.__id)

vards = "Daina"
parole = "ddddddd"
darbinieks1 = Darbinieks(vards, parole)
darbinieks1.drukaVardu()
darbinieks1.drukaParoli()
darbinieks1.izdrukaID()
#print(darbinieks1.__id)

visi = [viesis1, darbinieks1]
for x in visi:
    x.drukaVardu()
    x.drukaParoli()

print(isinstance(darbinieks1, Viesis))
print(isinstance(darbinieks1, Darbinieks))
print(isinstance(viesis1, Viesis))
print(isinstance(viesis1, Darbinieks))