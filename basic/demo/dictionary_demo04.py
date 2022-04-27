"""
 联网获取JSON格式的数据并解析出需要的内容
 修改第三方库的下载来源为国内的镜像网站 ---> pip config set global.index-url https://pypi.doubanio.com/simple
 三方库 ---> requests ---> pip install requests

 协议 ---> 通信双方需要遵守的会话规则
 HTTP / HTTPS ---> 通过URL访问网络资源的协议
 请求（requests） - 响应 （response）
"""
import json

import requests
# 请求服务器，服务器就会返回JSON
resp = requests.get('http://api.tianapi.com/guonei/index?key=ab860ab6d233922b9f9857b15207c10a&num=20')
print(resp.text)
# new_dict = json.loads(resp.text)
new_dict = resp.json()  # 等价于上述写法
for new in new_dict['newslist']:
    print(new['title'])
    print(new['url'])