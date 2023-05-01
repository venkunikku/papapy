import sys
from platform import python_version
import math


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    # This is backup for str. Incase that is not defined this will be called by print.
    def __repr__(self) -> str:
        print("This is backup for __str__")
        return f'Vector({self.x!r},{self.y!r})'

    # comment this method to see __repe__ getting called. 
    def __str__(self) -> str:
        print("Coming to String but will go to repre as fall back")
        return f'Vector({self.x!r},{self.y!r})'

    def __abs__(self):
        # print("abs called")
        return math.hypot(self.x, self.y)
    
    def __bool__(self) -> bool:
        # print("bool called")
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)


if __name__ == "__main__":
    print("test", sys.version)
    print("*"*150)
    print(python_version())

    vec = Vector(2, 3)
    print(vec)
    print(abs(vec))
    print(bool(vec))

    vec2 = Vector(3,2)
    vec3 = vec + vec2
    print(vec3); print(bool(vec3))

    print(vec3*10)

    print(F'Using Str instead of repr: {vec}')

    