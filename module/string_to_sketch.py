import base64
import re
from operation.tricks import np, cv2, from_png_to_jpg


# 处理远程图片编码字符串成相应的jpg图片
def string_to_sketch(image, points):

    for _ in range(len(points)):
        points[_][1] = 1 - points[_][1]

    image = re.sub('^data:image/.+;base64,', '', image)
    image = base64.urlsafe_b64decode(image)
    sketch = np.fromstring(image, dtype=np.uint8)
    sketch = cv2.imdecode(sketch, -1)
    sketch = from_png_to_jpg(sketch)

    return sketch



