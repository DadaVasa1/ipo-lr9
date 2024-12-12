import CorrectRect
def intersectionAreaRect(arr1, arr2):
    x1, y1, x2, y2 = arr1[0][0], arr1[0][1], arr1[1][0], arr1[1][1]
    x3, y3, x4, y4 = arr2[0][0], arr2[0][1], arr2[1][0], arr2[1][1]
    for i in [arr1, arr2]:
        if not CorrectRect.isCorrectRect(i):
            raise ValueError("прямоугольник некоректный")
    s1 = (min(x2, x4) - max(x1, x3))
    s2 = (min(y2, y4) - max(y1, y3))
    s_result = s1 * s2    
    return s_result


