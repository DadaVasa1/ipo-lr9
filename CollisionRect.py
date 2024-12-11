import CorrectRect
def isCollisionRect(arr1, arr2):
    for i in [arr1, arr2]:
        if not CorrectRect.isCorrectRect(i):
            raise ValueError("1й прямоугольник некоректный")
        
    return not (arr1[1][0] < arr2[0][0] or arr1[0][0] > arr2[1][0] or arr1[1][1] < arr2[0][1] or arr1[0][1] > arr2[1][1])



print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]))


