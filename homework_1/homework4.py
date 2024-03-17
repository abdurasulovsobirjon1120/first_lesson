import math
"""
4. Doiraning yuzi S. Uning radiusini toping.
"""

# 4-topshiriq 
class Doira:
    def __init__(self, S):
        self.S = S

    def radius(self):
        return math.sqrt(self.S / math.pi)

S = int(input("Doiraning yuzini kiriting : "))

doira = Doira(S)
print("Doira radiusi:", doira.radius())