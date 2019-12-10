from operation.tricks import go_passline, min_k_down_c, cv_denoise, sensitive
from operation.ai import go_tail


# 进一步降噪模糊
def continue_improve(sketch):
    improved_sketch = go_passline(sketch)
    improved_sketch = min_k_down_c(improved_sketch, 2)
    improved_sketch = cv_denoise(improved_sketch)
    improved_sketch = go_tail(improved_sketch)
    improved_sketch = sensitive(improved_sketch, s=5.0)

    return improved_sketch
