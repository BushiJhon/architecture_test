from operation.ai import go_tail
from operation.tricks import min_resize, cv_denoise, sensitive


# 图片的模糊化
def sketch_blurry(sketch):
    improved_sketch = min_resize(sketch, 512)
    improved_sketch = cv_denoise(improved_sketch)
    improved_sketch = sensitive(improved_sketch, s=5.0)
    improved_sketch = go_tail(improved_sketch)

    return improved_sketch
