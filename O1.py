class Poligon:
    def __init__(self,sides,color = "red" ):
        self.sides = sides
        self.color = color

        # konstruktor első paramétere mindig self
        # ha a paraméternek default értéke van a végére kell kerülnie


class Triangle:
    pass

my_polygon = Poligon(4)
print(my_polygon.sides)
print(my_polygon.color)


