from operation.ai import go_head, go_tail
from operation.tricks import k_resize, opreate_normal_hint, ini_hint


# 生成结果图片
def result_produce(sketch_1024, points, composition):
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
    result = go_tail(result)
    return result
