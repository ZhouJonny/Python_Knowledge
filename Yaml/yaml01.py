import yaml


# 读取文件
file_list = open('/basic/Yaml/data/data_list.yaml', 'r', encoding='utf-8')
datas = yaml.load(stream=file_list, Loader=yaml.FullLoader)
# 数据内容展示
print(datas)
print(datas[0][1])
# 数据类型展示
print(type(datas))

file_dict = open('/basic/Yaml/data/data_dict.yaml', 'r', encoding='utf-8')
datas_dict = yaml.load(stream=file_dict, Loader=yaml.FullLoader)
print(datas_dict)