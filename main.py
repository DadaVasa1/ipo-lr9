from collision.CorrectRect import isCorrectRect
from collision.CollisionRect import isCollisionRect
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect
from collision.intersectionAreaRect import intersectionAreaRect
print("Exersice 2")
print(isCorrectRect([(-3.4, 1),(9.2, 10)]))
print("Exersice 3")
print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]))
print("Exersice 4")
print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))
print("Exersice 5")
print(intersectionAreaMultiRect([
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]))