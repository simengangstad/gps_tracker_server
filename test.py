import requests
from random import randint
import time

URL = "http://127.0.0.1:5000/data"

for i in range(0, 10):
    data = {
        "lat": randint(0, 90),
        "lon": randint(0, 360)
    }

    r = requests.post(URL, data)

    time.sleep(2)
