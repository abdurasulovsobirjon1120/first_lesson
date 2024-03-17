import math
"""
3. Radiusi R bo’lgan aylananing uzunligini va doiraning
yuzini toping.
"""

# 3-topshiriq 
class Aylana:
    def __init__(self, R):
        self.R = R

    def uzunlik(self):
        return 2 * math.pi * self.R

    def yuza(self):
        return math.pi * self.R ** 2

R = int(input("Aylananing radiusini kiriting : "))

aylana = Aylana(R)
print("Aylananing uzunligi : ", aylana.uzunlik())
print("Doiraning yuzasi : ", aylana.yuza())