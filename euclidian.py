import math


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def dot_product(self, other):
        """
            内積
        """
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)


    def cross_product(self, other):
        """
            外積
        """
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x

        return Vector(x, y, z)


    def linear_transform(self, mat):
        """
            f:A -> B
            return B
                B = Ax
        """
        x = mat[0][0]*self.x + mat[0][1]*self.y + mat[0][2]*self.z
        y = mat[1][0]*self.x + mat[1][1]*self.y + mat[1][2]*self.z
        z = mat[2][0]*self.x + mat[2][1]*self.y + mat[2][2]*self.z

        return Vector(x, y, z)


    def norme(self, nrm='l2'):
        """
            return L1 or L2 norme
        """
        if nrm == 'l1':
            return abs(self.x) + abs(self.y) + abs(self.z)
        elif nrm == 'l2':
            return math.sqrt(self.x**2 + self.y**2 + self.z**2)
        else:
            raise ValueError("Invalid Norme")


    def normalize(self):
        return self * (1 / self.norme()) 


    def proj(self, v):
        """
            proj_u(v) := (<u, v> / <u, u>) * u
        """
        return self * (self.dot_product(v) / self.dot_product(self))


    @staticmethod
    def approximate(vec):
        if not isinstance(vec, Vector):
            raise ValueError("Vector instance required")
        x = round(vec.x)
        y = round(vec.y)
        z  =round(vec.z)
        return Vector(x, y, z)


    @staticmethod
    def gram_schmidt(*args):
        """
            Less than 3 vectors is available.
            実数をあまり扱いたくない
        """

        units = [args[0]]
        for k in range(1, len(args)):
            tmp = Vector(0, 0, 0)
            for unit in units:
                tmp += unit.proj(args[k])
            units.append(args[k] - tmp)

        return units


    def __eq__(self, other):
        if other is None or type(self) != type(other): return False
        return self.__dict__ == other.__dict__


    def __ne__(self, other):
        return not self.__eq__(other)


    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Vector instance required")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Vector instance required")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other):
        return self.__add__(-1*other)


    def __isub__(self, other):
        return self.__add__(-1*other)


    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Zahl required")
        return Vector(self.x * other, self.y * other, self.z * other)


    def __imul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Zahl required")
        return Vector(self.x * other, self.y * other, self.z * other)


    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Zahl required")
        return Vector(self.x * other, self.y * other, self.z * other)


    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Zahl required")
        return Vector(self.x * (1/other), self.y * (1/other), self.z * (1/other))


    def __repr__(self):
        return "Vector({0}, {1}, {2})".format(self.x, self.y, self.z)

