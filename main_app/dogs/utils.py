import datetime
import math
import re

from django.utils.html import strip_tags


def count_dogs(html_string):
    # html_string = """
    # <h1>This is a title</h1>
    # """
    dog_string = strip_tags(html_string)
    matching_dogs = re.findall(r'\w+', dog_string)
    count = len(matching_dogs) 
    return count
