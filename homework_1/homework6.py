import math
"""
6. Tekislikda uchburchak uchlarining koordinatasi
A(x1,y1) , B(x2,y2) va S(x3,y3). Uchburchakning yuzini toping.
"""

# 6-topshiriq
class Uchburchak:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def uzunlik(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def yuza(self):
        AB = self.uzunlik(self.x1, self.y1, self.x2, self.y2)
        AC = self.uzunlik(self.x1, self.y1, self.x3, self.y3)
        BC = self.uzunlik(self.x2, self.y2, self.x3, self.y3)
        s = (AB + AC + BC) / 2
        return math.sqrt(s * (s - AB) * (s - AC) * (s - BC))

x1 = int(input("A nuqtasining x koordinatini kiriting : "))
y1 = int(input("A nuqtasining y koordinatini kiriting : "))
x2 = int(input("B nuqtasining x koordinatini kiriting : "))
y2 = int(input("B nuqtasining y koordinatini kiriting : "))
x3 = int(input("S nuqtasining x koordinatini kiriting : "))
y3 = int(input("S nuqtasining y koordinatini kiriting : "))

uchburchak = Uchburchak(x1, y1, x2, y2, x3, y3)
print("Uchburchakning yuzi : ", uchburchak.yuza())