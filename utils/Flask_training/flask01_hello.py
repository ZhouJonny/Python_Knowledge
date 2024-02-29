# 从flask模块中导入Flask类
from flask import Flask

# 创建Flask对象
# 参数1：__name__ ---> 如果从当前文件启动，那么值是__main__。如果是从其他模块调用运行，那么值是模块的名字。
# 参数2：static_url_path ---> 表示静态资源的访问地址：图片，js文件等
# 参数3：static_folder ---> 用来存储静态资源，默认名字是static。需要创建一个static文件夹，在这个文件夹下保存静态资源。
# 参数4：template_folder ---> 模版文件夹，默认的值是templates。
app = Flask(__name__)


# 装饰器的作用：使用app，通过路由（route）绑定一个视图函数
# 注意：视图函数一定要有返回值
@app.route('/')
def hellow_world():
    return 'hello world Flask'


# 判断是否直接使用当前模块运行程序
if __name__ == '__main__':
    app.run()