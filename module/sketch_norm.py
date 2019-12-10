from operation.tricks import k_resize, mini_norm, hard_norm, min_k_down, sk_resize


# 图像的归一化
def sketch_norm(sketch):
    sketch_1024 = k_resize(sketch, 64)
    sketch_256 = mini_norm(k_resize(min_k_down(sketch_1024, 2), 16))
    sketch_128 = hard_norm(sk_resize(min_k_down(sketch_1024, 4), 32))
    return sketch_1024, sketch_256, sketch_128
