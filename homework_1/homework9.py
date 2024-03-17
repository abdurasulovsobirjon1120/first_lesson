"""
9. Uch xonali butun son berilgan. Bu son raqamlarining
yig’indisini va ko’paytmasini toping.
"""

# 9-topshiriq
class Uchxonalison:
    def __init__(self ,son ):
        self.son = son

    def aniqlash1(self):
        birlik = son % 10 
        onlik = (son // 10) % 10
        yuzlik = son // 100
        return birlik + onlik + yuzlik
    
    def aniqlash2(self):
        birlik = son % 10 
        onlik = (son // 10) % 10
        yuzlik = son // 100
        return birlik * onlik * yuzlik

son = int(input("3 xonali son kiriting : ")) 

javob = Uchxonalison(son)

yigindi = javob.aniqlash1()
kopaytma = javob.aniqlash2()
print("Yig'inisi = ", yigindi )
print("Ko'paytmasi = " , kopaytma)