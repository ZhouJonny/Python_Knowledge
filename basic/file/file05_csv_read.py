"""
读取csv文件（逗号分隔值） ---> Comma Separated Value
"""
import csv

with open('Data/csv_file.csv', encoding='gb18030') as file:
    # content = file.readline()
    # while content:
    #     values = content.replace('\n', '').split(',')
    #     print(values)
    #     content = file.readline()

    # 效果同上
    # csv.reader(file, delimiter='\t', quotechar='"')
    # delimiter ---> 设置分隔符（默认是英文逗号）
    # quotechar ---> 包裹字符串的符号（默认是英文的双引号）
    reader = csv.reader(file)
    for row in reader:
        print(row)