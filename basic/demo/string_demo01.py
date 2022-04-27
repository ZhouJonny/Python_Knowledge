"""
文字跑马灯
"""
import os
import time

content = 'life is short, I use python       '
while True:
    os.system('clear')
    print(content)
    time.sleep(0.5)
    content = content[1:] + content[0]