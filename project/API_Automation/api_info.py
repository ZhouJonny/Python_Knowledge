import requests

resp_get = requests.get(
    "https://www.baidu.com/",
    headers={},  # 请求头
    cookies={},  # cookies鉴权
    params={},  # 查询字符串
    data={},  # 表单参数
    json={},  # JSON参数
    files={},  # 文件上传
)

resp_post = requests.post(
    "https://www.baidu.com/",
    headers={},  # 请求头
    cookies={},  # cookies鉴权
    params={},  # 查询字符串
    data={},  # 表单参数
    json={},  # JSON参数
    files={},  # 文件上传
)

# 接口返回了哪些
"""
1.用tcpdump在服务端抓包

2.可以看到接口返回了以下内容：
    -状态码: 200 300 400 500
    -响应头： 文件大小（200M）,是否被压缩，cookie
    -响应正文：接口数据（json格式），小说（text），电影、音乐（content，二进制流）
"""
print(resp_post)

print(resp_post.status_code)
print(resp_post.headers)
print(resp_post.json())

# 接口断言，根据接口文档
# 比如
# 1.断言 success 出现在json中
assert 'success' == resp_post.json()['state']  # 优先，判断的更严谨
assert 'success' in resp_post.text  # 只是判断接口返回中有success字段
