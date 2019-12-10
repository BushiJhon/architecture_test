from operation.ai import go_gird, go_tail
from operation.tricks import d_resize, ini_hint


# composition的训练生成
def composition_determine(sketch_256, baby):
    composition = go_gird(sketch=sketch_256, latent=d_resize(baby, sketch_256.shape), hint=ini_hint(sketch_256))
    composition = go_tail(composition)
    return composition
