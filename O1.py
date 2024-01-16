class Poligon:
    #osztályattribútum, minden példánynak azonos
    color = "piros"

    def __init__(self,sides,color2 = "red" ):
        self.sides = sides
        self.color2 = color2

        # konstruktor első paramétere mindig self
        # ha a paraméternek default értéke van a végére kell kerülnie


class Triangle:
    pass

my_polygon = Poligon(4)
print(my_polygon.sides)
print(my_polygon.color2)
print(my_polygon.color)


