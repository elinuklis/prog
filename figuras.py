class Figuras:
    def __init__(self, nosaukums, malas):
        self.nosaukums = nosaukums
        self.malas = malas

    def drukaNosaukumuUnMalas(self):
        print(f"{self.nosaukums}" + ", "+f"{self.malas}"+" malas")

nosaukums = "kvadrats"
malas = 4
kvadrats=Figuras(nosaukums, malas)

nosaukums = "taisnstūris"
malas = 4
taisnsturis=Figuras(nosaukums, malas)

nosaukums = "trijstūris"
malas = 3
trijsturis=Figuras(nosaukums, malas)

visi = [kvadrats, taisnsturis, trijsturis]
for x in visi:
    x.drukaNosaukumuUnMalas()

