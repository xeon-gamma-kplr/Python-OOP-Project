class Product():
    def __init__(self,cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque

class Meubles(Product):
    def __init__(self,cost,price,marque, materiaux,couleurs,dimensions):
        super().__init__(cost, price, marque)
        self.materiaux = materiaux
        self.couleurs = couleurs
        self.dimensions = dimensions

class Table(Meubles):
    def __init__(self,cost,price,marque, materiaux,couleurs,dimensions):
        super().__init__(cost, price, marque, materiaux, couleurs,dimensions)

class Canape(Meubles):
    def __init__(self,cost,price,marque, materiaux,couleurs,dimensions):
        super().__init__(cost, price, marque, materiaux, couleurs,dimensions)

class Chaise(Meubles):
    def __init__(self,cost,price,marque, materiaux,couleurs,dimensions):
        super().__init__(cost, price, marque, materiaux, couleurs,dimensions)


canape1 = Canape(1000, 2000, "OKLM", "Cuir", "Blanc", "200x100x80")

canape2 : Canape(800, 1600, "SIESTA", "Tissu", "Bleu", "150x90x70")

chaise1 : Chaise(50, 100, "PEPOUSE", "Plastique", "Rouge", "50x50x70")

chaise2 : Chaise(75, 150, "PEPOUSE", "Métal", "Gris", "60x60x80")


table2 : Table(250, 500, "TEX", "Bois", "Chêne", "150x80x75")

table1 : Table(350, 700, "TEX", "Verre", "Transparent", "120x60x75")



