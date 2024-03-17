import math
"""
7. Ikki sonning o’rta arifmetik va o’rta geometrik
q‟iymatlarini toping.
"""

# # 7-vazifa
class Son:
    def __init__(self , son1 , son2):
        self.son1 = son1
        self.son2 = son2

    def ortaArifmetik(self ):
        return (son1 + son2) / 2 

    def ortaGeometrik(self):  
        return math.sqrt(self.son1 * self.son2)
    
son1 = int(input("Son 1 : "))
son2 = int(input("Son 2 : "))

orta = Son(son1 , son2)

ortaA = orta.ortaArifmetik()
ortaG = orta.ortaGeometrik()

print("O'rta arifmetik : " ,ortaA)
print("O'rta geometrik : " , ortaG)