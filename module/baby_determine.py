from operation.ai import go_baby, go_tail
from operation.tricks import de_line, blur_line, clip_15, opreate_normal_hint, ini_hint


# baby模型的训练
def baby_determine(sketch_128, points):
    baby = go_baby(sketch_128, opreate_normal_hint(ini_hint(sketch_128), points, type=0, length=1))
    baby = de_line(baby, sketch_128)

    for _ in range(16):
        baby = blur_line(baby, sketch_128)

    baby = go_tail(baby)
    baby = clip_15(baby)
    return baby
