# img stat
# 获取图片的大小, 并存到 json 文件里

import json
import imagesize
import os
os.chdir(os.path.dirname(__file__))
path = "../images/"

def picIsCorrect(basename):
    fileSuffix = os.path.splitext(basename)[1]
    if fileSuffix == ".png" or fileSuffix == ".jpg" or fileSuffix == ".jpeg":
        return True
    else:
        return False

images = [i for i in os.listdir("../images/") if picIsCorrect(i)]

stat = {img:imagesize.get(path+img) for img in images}

stat = dict(sorted(stat.items(), key=lambda d:d[1][1]-d[1][0], reverse = False))

with open("../assets/img-info.json", "w+") as f:
    json.dump(stat, f)