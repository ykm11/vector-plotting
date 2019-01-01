from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from euclidian import Vector

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")


class GraphPlot:

    @staticmethod
    def show():
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        plt.legend(loc='best')
        plt.show()


    @staticmethod
    def config_lim(lim):
        """
            xlim : [min, max]
            ylim : [min, max]
            zlim : [min, max]
        """
        ax.set_xlim(lim[0], lim[1])
        ax.set_ylim(lim[0], lim[1])
        ax.set_zlim(lim[0], lim[1])


    @staticmethod
    def plot(vector, originVec=Vector(0,0,0), **kargs):
        if not isinstance(originVec, Vector):
            raise ValueError("originVec should be Vector")

        plt.quiver(originVec.x, originVec.y, originVec.z, vector.x, vector.y, vector.z, **kargs)


def test():
    v1 = Vector(3,2,-1)
    v2 = Vector(-2,1,3)
    v3 = Vector(2,-3,1)

    u1, u2, u3 = Vector.gram_schmidt(v1, v2, v3)

    u1 = u1.normalize()
    u2 = u2.normalize()
    u3 = u3.normalize()

    GraphPlot.plot(v1, color="black", label="v1")
    GraphPlot.plot(v2, color="black", label="v2")
    GraphPlot.plot(v3, color="black", label="v3")

    GraphPlot.plot(u1, color="red", label="u1")
    GraphPlot.plot(u2, color="red", label="u2")
    GraphPlot.plot(u3, color="red", label="u3")

    GraphPlot.config_lim([-5, 5])
    GraphPlot.show()

if __name__ == '__main__':
    test()
