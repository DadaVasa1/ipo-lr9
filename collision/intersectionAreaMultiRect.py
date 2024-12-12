import CorrectRect
def intersectionAreaMultiRect(arr1):
    for i in arr1:
        if not CorrectRect.isCorrectRect(i):
            raise ValueError("прямоугольник некоректный")

    x1 = max(rect[0][0] for rect in arr1) 
    y1 = max(rect[0][1] for rect in arr1) 
    x2 = min(rect[1][0] for rect in arr1) 
    y2 = min(rect[1][1] for rect in arr1) 

    return (x2 - x1) * (y2 - y1)

