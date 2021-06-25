# coding =utf-8
import random


def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


def get_str(num):
    strs = [Unicode() for i in range(num)]
    return ''.join(strs)


def exist_object(key, data):
    if key in data.keys():
        return True
    else:
        return False
