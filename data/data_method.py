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

def get_int(num):
    new_num = ""
    for i in range(int(num)):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        new_num += ch
    return int(new_num)

if __name__ == "__main__":
    print(get_int(4))