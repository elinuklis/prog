# class Virsklase:
#     def __init__(self, vards):
#         self.vards = vards
#         print(f"Virsklases vārds: {self.vards}")

# class Apaksklase(Virsklase):
#     def __init__(self, vards, vecums):
#         super().__init__(vards)
#         self.vecums = vecums
#         print(f"Apakšklases vecums:  {self.vecums}")

# objekts = Apaksklase("Jānis", 25)

# class KlaseA:
#     def __init__(self):
#         super().__init__()
#         print("Klase A konstruktors")

# class KlaseB:
#     def __init__(self):
#         print("Klase B konstruktors")

# class ApvienotaKlase(KlaseB, KlaseA):
#     def __init__(self):
#         super().__init__()
#         print("Apvienotas klases konstruktors")

# objekts =  ApvienotaKlase()

class Doktorats:
    def __init__(self, nosaukums="nav nosaukums", skaits=0):
        self.nosaukums = nosaukums
        self.skaits = skaits

    def inputNosaukums(self):
        self.nosaukums = input("Ievadiet doktorāta nosaukumu: ")

    def inputSkaits(self):
        self.skaits = int(input("Ievadiet doktorāta pacientu skaitu: "))

    def teksts(self):
        print(f"Doktorāts {self.nosaukums} apkalpo {self.skaits} pacientus.")

dokatorats1 = Doktorats()

dokatorats1.inputNosaukums()
dokatorats1.inputSkaits()
dokatorats1.teksts()