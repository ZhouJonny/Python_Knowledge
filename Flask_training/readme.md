# 一.flask框架介绍
- 安装
  > pip install flask
- 组成：werkzueg + jinja2
  >- werkzueg:专门来处理请求相关的内容。比如：地址
  > 
  >- jinja:用来做页面渲染
  > 
  >- 额外的拓展包：可以处理数据库的链接
- 路由的请求和响应
  > 浏览器地址栏输入的内容：http://192.168.0.103:8080/  ---> 服务器 ---> app ---> 有没有这个路由 ---> 
  > 就会执行路由匹配的函数 --> return "hello world" ---> response ---> 客户端的浏览器
  - 请求 request
    - 请求行
    >- 请求地址：http://192.168.0.103:8080/ 
    >- 请求方法：get / post
    - 请求头
    >- key：value形式
    >- Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9</br>
       Accept-Encoding: gzip, deflate</br>
       Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7</br>
       Cache-Control: max-age=0</br>
       Connection: keep-alive</br>
       Host: 192.168.0.103:8080</br>
       Upgrade-Insecure-Requests: 1</br>
       User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36
    - 请求体
    > get请求没有请求体
  - 响应 response
    - 响应行 ---> 状态码 
    >- 200 ok - 请求成功
    >- 404 not found - 请求的资源（网页不存在）
    >- 500 - 内部服务器错误
    >- 301 - 资源（网页等）被永久转移到其他url
    - 响应头
    - 响应体
