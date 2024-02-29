"""
使用第三方库speedtest-cli来执行实际下载和上传的速度
"""

import speedtest
import time
from datetime import datetime
import os

i = True

def run_prog():
    print("Please wait While programe runs it's checks...")

    try:
        print("now datatime")
        now_datetime = datetime.now()
        date = now_datetime.strftime("%Y-%m-%d %H:%M:%S") # 格式化成 年月日 时分秒 格式
        print(date)
        
    except:
        print("Connection Lost!")
        
print('test')        
run_prog()