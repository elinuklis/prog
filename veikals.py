# class Darbinieks:
#     def __init__(self, vards, uzvards, adrese):
#         self.vards = vards
#         self.uzvards = uzvards
#         self.adrese = adrese

#     def pievienot_preci(self):
#         print("Pievieno preci.")

#     def nonemt_preci(self):
#         print("Noņem preci.")

#     def iegut_vardu(self):
#         return self.vards

#     def iegut_uzvardu(self):
#         return self.uzvards

#     def iegut_adresi(self):
#         return self.adrese

# darbinieks1 = Darbinieks("Elina", "Berzina", "Jaunā iela")
 
# print(darbinieks1.iegut_vardu())
# print(darbinieks1.iegut_uzvardu())
# print(darbinieks1.iegut_adresi())
# darbinieks1.pievienot_preci()
# darbinieks1.nonemt_preci()
class Administrators:
    def __init__(self, vards, uzvards, parole):
        self.vards = vards
        self.uzvards = uzvards
        self.parole = parole

    def nonemt_kontu(self):
        print("Noņem kontu.")

    def nomainit_paroli(self):
        print("Nomaina paroli.")

    def iegut_vardu(self):
        return self.vards

    def iegut_uzvardu(self):
        return self.uzvards

    def iegut_paroli(self):
        return self.parole

admin1 = Administrators("Līna", "Ziņa", "Vecā iela")
 
print(admin1.iegut_vardu())
print(admin1.iegut_uzvardu())
print(admin1.iegut_paroli())
admin1.nonemt_kontu()
admin1.nomainit_paroli()