from flask import Flask

from Flask_training import settings

app = Flask(__name__)
app.config.from_object(settings)  # 通过这代码将独立的两个文件绑定在一起，将配置信息放在settings.py中降低耦合性


@app.route('/')
def index():
    return 'hello,world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
