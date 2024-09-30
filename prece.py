class Prece:
    def __init__(self, nosaukums, cena, daudzums="Nav informācijas"):
        self.nosaukums = nosaukums
        self.cena = cena
        self.daudzums = daudzums

    def cena_ar_pvn(self, pvn=21):
        return self.cena * (1 + pvn / 100)

prece1 = Prece("datoru", 1000)
prece2 = Prece("televizoru", 500, "10")

print("Tu nopirki " + f"{prece1.nosaukums}" + ", kura sākotnējā cena ir " + f"{prece1.cena}" + "€" + ", bet ar PVN " + f"{prece1.cena_ar_pvn()}" + "€" +", pieejamās preces: " + f"{prece1.daudzums}")
print("Tu nopirki " + f"{prece2.nosaukums}" + ", kura sākotnējā cena ir " + f"{prece2.cena}" + "€" + ", bet ar PVN " + f"{prece2.cena_ar_pvn()}" + "€" +", pieejamās preces: " + f"{prece2.daudzums}")
        