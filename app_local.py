import urllib3
import json
# with open('result.jpg', 'rb') as f:
    #     sketch = f.read()


def to_remote_string_to_sketch(image, points):
    url = 'http://localhost:8080/string_to_sketch'
    values = {'image': image, 'points': points}
    data = json.dumps(values).encode('utf-8')

    http = urllib3.PoolManager()
    res = http.request(
        'POST',
        url,
        body=data,
        headers={'Content-Type': 'application/json'}
    )
    return res.data


def to_remote_sketch_blurry(sketch, points):
    url = 'http://localhost:8080/sketch_blurry'
    http = urllib3.PoolManager()
    res = http.request(
        'POST',
        url,
        fields={
            'sketch': ('sketch.jpg', sketch, 'image/jpg'),
            'points': str(points),
        }
    )
    return res.data

# from image import *
# to_remote_string_to_sketch(image, points)


# with open('sketch.jpg', 'rb') as f:
#         sketch = f.read()
#
#
# from image import points
#
# points = points
# print(points)
# for _ in range(len(points)):
#     points[_][1] = 1 - points[_][1]

# to_remote_sketch_blurry(sketch, points)
'''
def to_remote_judge_improve():
    return res.data


def to_remote_continue_improve():
    return res.data


def to_remote_go_gray():
    return res.data


def to_remote_sketch_norm():
    return res.data


def to_remote_baby_determine():
    return res.data


def to_remote_composition_determine():
    return res.data


def to_remote_result_produce():
    return res.data
    
'''
