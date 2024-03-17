import math
"""
5. A(x1,y1) va B(x2,y2) nuq‟talar koordinatalari bilan
berilgan. Ular orasidagi masofani toping.
"""

# 5-topshiriq
class Masofa:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def hisoblash(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

x1 = float(input("A nuqtasining x koordinatini kiriting : "))
y1 = float(input("A nuqtasining y koordinatini kiriting : "))
x2 = float(input("B nuqtasining x koordinatini kiriting : "))
y2 = float(input("B nuqtasining y koordinatini kiriting : "))

masofa = Masofa(x1, y1, x2, y2)
print("A va B nuqtalari orasidagi masofa : ", masofa.hisoblash())