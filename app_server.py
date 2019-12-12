from module.string_to_sketch import string_to_sketch, cv2
from module.sketch_blurry import sketch_blurry
from module.judge_improve import judge_improve
from module.continue_improve import continue_improve
from module.go_gray import go_gray
from module.sketch_norm import sketch_norm
from module.baby_determine import baby_determine
from module.composition_determine import composition_determine
from module.result_produce import result_produce

from bottle import *
BaseRequest.MEMFILE_MAX = 10000 * 1000
points_ping = []


@route('/string_to_sketch', method='POST')
def remote_string_to_sketch():
    data = request.json
    image = data['image']
    points = data['points']
    sketch = string_to_sketch(image=image, points=points)
    sketch = sketch_blurry(sketch=sketch)
    std = judge_improve(sketch=sketch)
    if std:
        sketch = continue_improve(sketch=sketch)
    sketch = go_gray(sketch=sketch)
    sketch_1024, sketch_256, sketch_128 = sketch_norm(sketch=sketch)
    baby = baby_determine(sketch_128=sketch_128, points=points)
    composition = composition_determine(sketch_256=sketch_256, baby=baby)
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


@route('/sketch_blurry', method='POST')
def remote_sketch_blurry():
    sketch = request.files.get('sketch')
    sketch.save('sketch_blurry.jpg')
    sketch = cv2.imread('sketch_blurry.jpg')
    points = points_ping
    sketch = sketch_blurry(sketch=sketch)
    std = judge_improve(sketch=sketch)
    if std:
        sketch = continue_improve(sketch=sketch)
    sketch = go_gray(sketch=sketch)
    sketch_1024, sketch_256, sketch_128 = sketch_norm(sketch=sketch)
    baby = baby_determine(sketch_128=sketch_128, points=points)
    composition = composition_determine(sketch_256=sketch_256, baby=baby)
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


@route('/judge_improve', method='POST')
def remote_judge_improve():
    sketch = request.files.get('sketch')
    sketch.save('judge_improve.jpg')
    sketch = cv2.imread('judge_improve.jpg')
    points = points_ping
    std = judge_improve(sketch=sketch)
    if std:
        sketch = continue_improve(sketch=sketch)
    sketch = go_gray(sketch=sketch)
    sketch_1024, sketch_256, sketch_128 = sketch_norm(sketch=sketch)
    baby = baby_determine(sketch_128=sketch_128, points=points)
    composition = composition_determine(sketch_256=sketch_256, baby=baby)
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


@route('/continue_improve', method='POST')
def remote_continue_improve():
    sketch = request.files.get('sketch')
    sketch.save('continue_improve.jpg')
    sketch = cv2.imread('continue_improve.jpg')
    points = points_ping
    sketch = continue_improve(sketch=sketch)
    sketch = go_gray(sketch=sketch)
    sketch_1024, sketch_256, sketch_128 = sketch_norm(sketch=sketch)
    baby = baby_determine(sketch_128=sketch_128, points=points)
    composition = composition_determine(sketch_256=sketch_256, baby=baby)
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


@route('/go_gray', method='POST')
def remote_go_gray():
    sketch = request.files.get('sketch')
    sketch.save('go_gray.jpg')
    sketch = cv2.imread('go_gray.jpg')
    points = points_ping
    sketch = go_gray(sketch=sketch)
    sketch_1024, sketch_256, sketch_128 = sketch_norm(sketch=sketch)
    baby = baby_determine(sketch_128=sketch_128, points=points)
    composition = composition_determine(sketch_256=sketch_256, baby=baby)
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


@route('/sketch_norm', method='POST')
def remote_sketch_norm():
    sketch = request.files.get('sketch')
    sketch.save('sketch_norm.jpg')
    sketch = cv2.imread('sketch_norm.jpg')
    points = points_ping
    sketch_1024, sketch_256, sketch_128 = sketch_norm(sketch=sketch)
    baby = baby_determine(sketch_128=sketch_128, points=points)
    composition = composition_determine(sketch_256=sketch_256, baby=baby)
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


@route('/baby_determine', method='POST')
def remote_baby_determine():
    sketch_128 = request.files.get('sketch_128')
    sketch_256 = request.files.get('sketch_256')
    sketch_1024 = request.files.get('sketch_1024')
    sketch_128.save('sketch_128.jpg')
    sketch_256.save('sketch_256.jpg')
    sketch_1024.save('sketch_1024.jpg')
    sketch_128 = cv2.imread('sketch_128.jpg')
    sketch_256 = cv2.imread('sketch_256.jpg')
    sketch_1024 = cv2.imread('sketch_1024.jpg')
    points = points_ping
    baby = baby_determine(sketch_128=sketch_128, points=points)
    composition = composition_determine(sketch_256=sketch_256, baby=baby)
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


@route('/composition_determine', method='POST')
def remote_composition_determine():
    baby = request.files.get('baby')
    sketch_256 = request.files.get('sketch_256')
    sketch_1024 = request.files.get('sketch_1024')
    points = request.json['points']
    composition = composition_determine(sketch_256=sketch_256, baby=baby)
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


@route('/result_produce', method='POST')
def remote_result_produce():
    composition = request.files.get('composition')
    sketch_1024 = request.files.get('sketch_1024')
    points = request.json['points']
    result = result_produce(sketch_1024=sketch_1024, points=points, composition=composition)
    cv2.imwrite('result.jpg', result)
    return static_file('result.jpg', root='.')


run(host='localhost', port=8080)