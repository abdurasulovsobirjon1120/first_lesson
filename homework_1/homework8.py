import math
"""
8. To’g’ri to’rtburchak diagonali uchlarining
koordinatalari berilgan. Uning yuzini toping.
"""

# 8-vaifa 
class Tortburchak:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def orta_nuqta(self):
        xm = (self.x1 + self.x2) / 2
        ym = (self.y1 + self.y2) / 2
        return xm, ym
    
    def uzunlik(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        
    
    def yuzi(self):
        a = self.uzunlik()
        return (a**2) / 2

x1 = int(input("1-diaganol koordinatasi : "))
y1 = int(input("2-diaganol koordinatasi : "))
x2 = int(input("3-diaganol koordinatasi : "))
y2 = int(input("4-diaganol koordinatasi : "))

tortburchak = Tortburchak(x1, y1, x2, y2)

yuz = tortburchak.yuzi()
print("To'g'ri to'rtburchak yuzi : ", yuz)
