# builtin module

import random

print(random.randint(1, 10))


# third-party module

import requests

html = requests.get('https://www.google.com/')
print(html.text)


# custom module
import mytools as tool
from mytools import *
from mytools import random_str
