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

image = image
points = points

sketch = string_to_sketch(image=image, points=points)

sketch = sketch_blurry(sketch=sketch)

std = judge_improve(sketch=sketch)

sketch = continue_improve(sketch=sketch)

sketch = go_gray(sketch=sketch)

sketch_1024, sketch_256, sketch_128 = sketch_norm(sketch=sketch)

baby = baby_determine(sketch_128=sketch_128, points=points)

composition = composition_determine(sketch_256=sketch_256, baby=baby)

result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)

cv2.imshow('result', result)
cv2.waitKey(0)