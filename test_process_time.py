from module.string_to_sketch import string_to_sketch, cv2
from module.sketch_blurry import sketch_blurry
from module.judge_improve import judge_improve
from module.continue_improve import continue_improve
from module.go_gray import go_gray
from module.sketch_norm import sketch_norm
from module.baby_determine import baby_determine
from module.composition_determine import composition_determine
from module.result_produce import result_produce
from image import *

import time

image = image
points = points

time_sign = time.time()
sketch = string_to_sketch(image=image, points=points)
process_time = time.time() - time_sign
print('图片字符串解码处理时间：' + str(process_time))

time_sign = time.time()
sketch = sketch_blurry(sketch=sketch)
process_time = time.time() - time_sign
print('图片模糊去噪处理时间：' + str(process_time))

time_sign = time.time()
std = judge_improve(sketch=sketch)
process_time = time.time() - time_sign
print('计算像素点算术平均值时间：' + str(process_time))

time_sign = time.time()
sketch = continue_improve(sketch=sketch)
process_time = time.time() - time_sign
print('图片再次进行模糊去噪操作时间：' + str(process_time))

time_sign = time.time()
sketch = go_gray(sketch=sketch)
process_time = time.time() - time_sign
print('图片进行灰度化处理：' + str(process_time))

time_sign = time.time()
sketch_1024, sketch_256, sketch_128 = sketch_norm(sketch=sketch)
process_time = time.time() - time_sign
print('图片进行归一化处理时间：' + str(process_time))

time_sign = time.time()
baby = baby_determine(sketch_128=sketch_128, points=points)
process_time = time.time() - time_sign
print('baby模型训练生成时间：' + str(process_time))

time_sign = time.time()
composition = composition_determine(sketch_256=sketch_256, baby=baby)
process_time = time.time() - time_sign
print('composition模型训练生成时间：' + str(process_time))

time_sign = time.time()
result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
process_time = time.time() - time_sign
print('上色图片生成时间：' + str(process_time))