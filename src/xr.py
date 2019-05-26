import jinja2
import os
import json

def picIsCorrect(basename):
    filename, fileSuffix = os.path.splitext(basename)
    if fileSuffix == ".png" or fileSuffix == ".jpg" or fileSuffix == ".jpeg":
        return True
    else:
        return False

# 得到放置模板的目录
os.chdir(os.path.dirname(__file__))
path = os.path.abspath("../_includes")

# 创建一个加载器, jinja2 会从这个目录中加载模板
loader = jinja2.FileSystemLoader(path)
# print(loader.list_templates())

# 用加载器创建一个环境, 有了它才能读取模板文件
env = jinja2.Environment(loader=loader)
 
# 调用 get_template() 方法加载模板并返回
template = env.get_template('template.html')

# images = [i for i in os.listdir("./assets/img/portfolio") if picIsCorrect(i)]

with open("../assets/img-info.json", 'r') as f:
    stat = json.load(f)

images = stat.keys()

with open("../index.html", "w+") as f:
    f.write(template.render(images = images))
