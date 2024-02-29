"""
当系统提供的int，float，等参数类型无法满足需求的时候，我们需要自己定义。
之所以int，float，path可以接收不同的数据类型，是因为系统已经提供好了对应的转换器了。

自定义转换器格式：
    1。定义类，继承自BaseConverter
    2。重写init方法
    3。初始化父类成员变量，子类自己的规则
    4。将转换器类，添加到系统默认的转换器列表中。
"""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 1。定义类，继承自BaseConverter
class MyRegexConverter(BaseConverter):
    # 直接指定规则不够灵活，具体匹配什么规则应该交给路由
    # regex = '\d{3}'

    # 2。重写init方法
    def __init__(self, map, regex):
        # 3。初始化父类成员变量，子类自己的规则
        super(MyRegexConverter, self).__init__(map)
        self.regex = regex


# 4。将转换器类，添加到系统默认的转换器列表中。
app.url_map.converters['test'] = MyRegexConverter


@app.route('/<test("\d{3}"):number>')
def three_number(number):
    return 'the three number is %s' % number


@app.route('/test("1[3-9]\d{9}"):phone')
def phone(phone):
    return 'the phone is %s' % phone


if __name__ == '__main__':
    app.run(debug=True)
