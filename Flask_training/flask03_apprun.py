"""
参数1：host，IP地址 默认值127.0.0.1。一个ip对应一台机器
             若想让外网访问，需要将ip设置为：0.0.0.0。默认情况下只能是本机。
参数2：port，默认值5000。一个端口号对应的是一个程序。
参数3：debug，默认值False
    为True时：
        1。如果在运行过程中，直接改动代码，不需要重新启动程序,只要保存代码，就可以部署程序
run(host = 'ip地址', port = '端口号')
访问这台电脑（通过ip）的端口号对应的程序。
"""
from flask import Flask


app = Flask(__name__)


@app.route('/jonny')
def index():
    return 'this is index'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)

