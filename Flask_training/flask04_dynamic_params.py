"""
变量规则
在访问路由时指定参数：

- 格式：@app.route('/<类型：变量名>')
* 变量名一定要和视图函数里的参数一样
- 常见参数类型：
    · 整数 int
    · 小数 float
    · 字符串 path（默认值），整数和小数都可以被当作字符串
"""
from flask import Flask

from Flask_training import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/<int:number>')
def get_int(number):
    return 'the int is %s' % number


@app.route('/<float:number>')
def get_float(number):
    return 'the float is %s' % number


@app.route('/<number>')
def get_path(number):
    return 'the path is %s' % number


data = {'a': 'beijing', 'b': 'shanghai', 'c': 'shenzhen'}


@app.route('/getcity/<key>')
def get_city(key):
    return data[key]


if __name__ == '__main__':
    app.run(debug=True)
