import base64
import re
import cv2
import numpy as np
import time
from operation.tricks import *
from operation.ai import *
from image import *

image = image
points = points
path = 'image.jpg'


time1 = time.time()
for _ in range(len(points)):
    points[_][1] = 1 - points[_][1]
time2 = time.time()
print('task 1: ' + str(time2-time1))


image = re.sub('^data:image/.+;base64,', '', image)
image = base64.urlsafe_b64decode(image)
image = np.fromstring(image, dtype=np.uint8)
image = cv2.imdecode(image, -1)
time3 = time.time()
print('task 2: ' + str(time3-time2))

sketch = from_png_to_jpg(image)
improved_sketch = sketch.copy()

time4 = time.time()
print('task 3: ' + str(time4-time3))
improved_sketch = min_resize(improved_sketch, 512)
time5 = time.time()
print('task 4: ' + str(time5-time4))
improved_sketch = cv_denoise(improved_sketch)
time6 = time.time()
print('task 5: ' + str(time6-time5))

improved_sketch = sensitive(improved_sketch, s=5.0)
time7 = time.time()
print('task 6: ' + str(time7-time6))

improved_sketch = go_tail(improved_sketch)
time8 = time.time()
print('task 7: ' + str(time8-time7))

std = cal_std(improved_sketch)
time9 = time.time()
print('task 8: ' + str(time9-time8))

if std > 100.0:
    improved_sketch = go_passline(improved_sketch)
    time10 = time.time()
    print('task 9: ' + str(time10 - time9))
    improved_sketch = min_k_down_c(improved_sketch, 2)
    time11 = time.time()
    print('task 10: ' + str(time11 - time10))
    improved_sketch = cv_denoise(improved_sketch)
    time12 = time.time()
    print('task 11: ' + str(time12 - time11))
    improved_sketch = go_tail(improved_sketch)
    time13 = time.time()
    print('task 12: ' + str(time13 - time12))
    improved_sketch = sensitive(improved_sketch, s=5.0)
    time9 = time.time()
    print('task 13: ' + str(time9 - time13))


improved_sketch = min_black(improved_sketch)
time15 = time.time()
print('task 14: ' + str(time15-time9))
improved_sketch = cv2.cvtColor(improved_sketch, cv2.COLOR_BGR2GRAY)
time16 = time.time()
print('task 15: ' + str(time16-time15))
sketch_1024 = k_resize(improved_sketch, 64)
time17 = time.time()
print('task 16: ' + str(time17-time16))
sketch_256 = mini_norm(k_resize(min_k_down(sketch_1024, 2), 16))
time18 = time.time()
print('task 17: ' + str(time18-time17))
sketch_128 = hard_norm(sk_resize(min_k_down(sketch_1024, 4), 32))
time19 = time.time()
print('task 18: ' + str(time19-time18))

baby = go_baby(sketch_128, opreate_normal_hint(ini_hint(sketch_128), points, type=0, length=1))
time20 = time.time()
print('task 19: ' + str(time20-time19))
baby = de_line(baby, sketch_128)
time21 = time.time()
print('task 20: ' + str(time21-time20))

for _ in range(16):
    baby = blur_line(baby, sketch_128)
time22 = time.time()
print('task 21: ' + str(time22-time21))
baby = go_tail(baby)
time23 = time.time()
print('task 22: ' + str(time23-time22))
baby = clip_15(baby)
time24 = time.time()
print('task 23: ' + str(time24-time23))

composition = go_gird(sketch=sketch_256, latent=d_resize(baby, sketch_256.shape), hint=ini_hint(sketch_256))
time25 = time.time()
print('task 24: ' + str(time25-time24))
composition = go_tail(composition)
time26 = time.time()
print('task 25: ' + str(time26-time25))

painting_function = go_head
reference = None
alpha = 0
result = painting_function(
    sketch=sketch_1024,
    global_hint=k_resize(composition, 14),
    local_hint=opreate_normal_hint(ini_hint(sketch_1024), points, type=2, length=2),
    global_hint_x=k_resize(reference, 14) if reference is not None else k_resize(composition, 14),
    alpha=(1 - alpha) if reference is not None else 1
)
time27 = time.time()
print('task 26: ' + str(time27-time26))
result = go_tail(result)
time28 = time.time()
print('task 27: ' + str(time28-time27))
cv2.imwrite(path, result)
time29 = time.time()
print('task 28: ' + str(time29-time28))