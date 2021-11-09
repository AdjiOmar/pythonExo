"""
Class Cercle
"""



class Point:
    """les coordonnes d'un point"""

    def __init__(self, x, y):
        self.abscisse = x
        self.ordonnee = y


class Cercle:
    """Représente un Cercle"""
    def __init__(self, pt, r):
        if r < 0:
            raise ValueError("Le rayon du cercle doit etre positif")
        self.point = pt
        self.rayon = r

    def get_perimetre(self):
        """Renvoie le perimetre du cercle"""
        return 2 * 3.14 * self.rayon

    def get_surface(self):
        """Renvoie la surface du cercle"""
        return 3.14 * self.rayon **2

    def deplacer(self, x, y):
        """Permet de deplacer le cercle vers un nouveau centre"""
        self.abscisse = x
        self.ordonnee = y

    def augmenter(self):
        """Augmente le rayon du cercle de +1"""
        self.rayon += 1

    def diminuer(self):
        """Diminue le rayon du cercle de -1"""
        self.rayon -= 1

    def __str__(self):
        """Une representation comprehensive de l'objet par l'humain"""
       # return f"Abscisse: {self.abscisse}\nOrdonnee: {self.ordonnee}\nRayon: {self.rayon}"
        return f"Point: {self.point.abscisse},{self.point.ordonnee}\nRayon: {self.rayon}"






if __name__=="__main__":
    pt = Point(5, 3)
    cercle = Cercle(pt, 25)
    #cercle.abscisse = 25
    #cercle.ordonnee = 30

   # print(f"Coordonnees du cercle {cercle.abscisse} {cercle.ordonnee}")
    #print(f"Rayon du cercle {cercle.rayon}")
    print(cercle)
    print(f"perimetre du cercle: {cercle.get_perimetre()} cm")
    print(f"Surface du cercle: {cercle.get_surface()} cm2")