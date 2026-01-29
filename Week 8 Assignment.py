class Square:
    def __init__(self, side):
        self.side = side
        print("Square constructor called")

    def getPeri(self):
        return 4 * self.side

    def getArea(self):
        return self.side * self.side


class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
        print("Cube constructor called")

    def getArea(self):
        return 6 * self.side * self.side

    def getVolume(self):
        return self.side ** 3


# Test the classes
side = float(input("Enter side length: "))
cube = Cube(side)

print("Square Perimeter:", cube.getPeri())
print("Square Area:", super(Cube, cube).getArea())
print("Cube Surface Area:", cube.getArea())
print("Cube Volume:", cube.getVolume())