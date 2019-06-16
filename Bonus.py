import matplotlib.pyplot as plt
import math

class Point:
    def __init__(self, x, y):
        """
        A point specified by (x,y) coordinates in the cartesian plane
        """
        self.x = x
        self.y = y


class Polygon:
    def __init__(self, points):
        """
        points: a list of Points in clockwise order.
        """
        self.points = points

    @property
    def edges(self):
        ''' Returns a list of tuples that each contain 2 points of an edge '''
        edge_list = []
        for i, p in enumerate(self.points):
            p1 = p
            p2 = self.points[(i + 1) % len(self.points)]
            edge_list.append((p1, p2))

        return edge_list

    def contains(self, point):
        """
        return whether the point inside or outside the polygon

        :param point: 2D point

        :type point: Point object
        .. warning::

            this function is empty. needs implementation.

        """


if __name__ == "__main__":
    points = [Point(20, 10),
              Point(50, 125),
              Point(125, 90),
              Point(150, 10)]
    q = Polygon(points)

    # Test 1: Point inside of polygon
    p1 = Point(75, 50)
    print("P1 inside polygon: " + str(q.contains(p1)))

    # Test 2: Point outside of polygon
    p2 = Point(200, 50)
    print("P2 inside polygon: " + str(q.contains(p2)))

    # Test 3: Point at same height as vertex
    p3 = Point(35, 90)
    print("P3 inside polygon: " + str(q.contains(p3)))

    # Test 4: Point on bottom line of polygon
    p4 = Point(50, 10)
    print("P4 inside polygon: " + str(q.contains(p4)))


    # draw polygon
    def connectPoints(points, p1, p2):
        """

        :param points:
        :return:
        """
        x_values = [point.x for point in points]
        y_values = [point.y for point in points]
        plt.plot([x_values[p1], x_values[p2]], [y_values[p1], y_values[p2]], 'k-')


    connectPoints(points, 0, 1)
    connectPoints(points, 1, 2)
    connectPoints(points, 2, 3)
    connectPoints(points, 3, 0)

    # draw check points
    check_points = [p1, p2, p3, p4]
    x_values = [point.x for point in check_points]
    y_values = [point.y for point in check_points]

    plt.scatter(x_values, y_values)

    plt.show()


