class Circle:
    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y
        self.perimeter = self.calcPerimeter() #init des différentes variables de la classe

    def calcPerimeter(self):
        self.perimeter = self.x + self.y #methode de la fonction


p = Circle(1,2,12)
p.calcPerimeter()
print(p.perimeter)
