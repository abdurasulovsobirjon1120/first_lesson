"""
1. Ixtiyoriy ikkita son berilgan. Ularning yig„indisini,
ayirmasini, ko’paytmasini va nisbatini toping.
"""

# 2-topshiriq
class Uchburchak:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimetr(self):
        c = (self.a ** 2 + self.b ** 2) ** 0.5
        return self.a + self.b + c

    def yuzasi(self):
        return (self.a * self.b) / 2

a = int(input("Uchburchakning birinchi katetini kiriting : "))
b = int(input("Uchburchakning ikkinchi katetini kiriting : "))

uchburchak = Uchburchak(a, b)
print("Uchburchakning perimetri :", uchburchak.perimetr())
print("Uchburchakning yuzasi :", uchburchak.yuzasi())