import urllib3
import json
from image import *
from PIL import Image
from io import BytesIO


def http_post():
    url = 'http://localhost:8080/string_to_sketch'
    values = {'image': image, 'points': points}
    jdata = json.dumps(values).encode('utf-8')

    http = urllib3.PoolManager()
    res = http.request(
        'POST',
        url,
        body=jdata,
        headers={'Content-Type': 'application/json'}
    )
    return res.data


image = http_post()
bytes_stream = BytesIO(image)
image = Image.open(bytes_stream)
image.show()
