"""
查看哪些路由（地址）可以访问
- 格式：使用app.url_map，返回的是app装饰的所有路由和路径之间的映射关系。
- 注意：只有被app.url_map包含进来的路由才能被访问。
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "this is index"


@app.route('/jonny')
def jonny():
    return 'this is jonny'


if __name__ == '__main__':
    print(app.url_map)
    app.run()