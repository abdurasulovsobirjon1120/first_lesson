import math
"""
1. Ixtiyoriy ikkita son berilgan. Ularning yig„indisini,
ayirmasini, ko’paytmasini va nisbatini toping.
"""
# # 1-topshiriq 
class Calc:
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2
    
    def qoshish(self):
        return self.son1 + self.son2
    
    def ayirish(self):
        return self.son1 - self.son2

    def kopaytirish(self):
        return self.son1 * self.son2
    
    def bolish(self):
        if self.son2 != 0:
            return self.son1 / self.son2
        else:
            return "Nolga bo'lib bo'lish mumkin emas"

son1 = int(input("Birinchi sonni kiriting : "))
son2 = int(input("Ikkinchi sonni kiriting : "))

hisob = Calc(son1, son2)

print("Qo'shish :", hisob.qoshish())
print("Ayirish :", hisob.ayirish())
print("Ko'paytirish :", hisob.kopaytirish())
print("Bo'lish :", hisob.bolish())