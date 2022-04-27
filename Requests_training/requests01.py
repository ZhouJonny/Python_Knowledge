import requests


# 发送请求
response = requests.get('http://httpbin.org/get')
# 获取返回html的信息
# print(response.text)
print(response.headers)  # 返回头部信息
print(response.status_code)  # 请求状态码
print(response.content)  # 获取网页的二进制内容
print(response.url)  # 获取请求的url
print(response.cookies)  # 获取cookies