from operation.tricks import cv2, min_black


# 图像灰度化
def go_gray(sketch):
    improved_sketch = min_black(sketch)
    improved_sketch = cv2.cvtColor(improved_sketch, cv2.COLOR_BGR2GRAY)
    return improved_sketch