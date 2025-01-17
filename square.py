#!/usr/bin/python3

class square():
    width = 0
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return self.width * 4

    def __str__(self):
        return str(self.width)

if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.PermiterOfMySquare())
