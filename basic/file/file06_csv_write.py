"""
从文件中读入体温测量数据，显示体温不正常的病人信息

～ 37.2 以下 ---> 正常
～ 37。2～38。5 ---> 发热
～ 38。5以上 ---> 高烧
"""
import csv


with open('Data/temperature.txt', 'r') as file_read:
    #  写入中文时，设置编码为GBK，不然会乱码。
    with open('Data/csv_file.csv', 'w', encoding='GBK') as file_write:
        """
        1。创建writer对象来接收csv.writer()
        2。用writerow()写入数据，参数是元组或列表（代表一行中的所有数据，默认用逗号分隔）。
        """
        writer = csv.writer(file_write)
        writer.writerow(['ID', 'temperature', 'information'])  # 添加表头
        content = file_read.readline()
        while content:
            no, tem = content.split()
            tem = float(tem)
            if tem >= 37.2:
                if tem <= 38.5:
                    info = "发热"
                else:
                    info = "高烧"
                writer.writerow([no, tem, info])
            content = file_read.readline()

