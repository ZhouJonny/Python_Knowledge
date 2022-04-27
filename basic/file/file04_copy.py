"""
文件复制
"""
# with open('ScreenShot.png', 'rb') as source_file:
#     with open('/Users/zhouyujie/Desktop/copy.png', 'wb') as target_file:
#         data = source_file.read(512)
#         while data:
#             target_file.write(data)  # 读到的数据直接写到新文件中
#             data = source_file.read(512)


def file_copy(source, target):
    """
    文件拷贝

    :param source: 要拷贝的文件
    :param target: 拷贝后的新文件
    :return: None
    """
    with open(source, 'rb') as source_file:
        with open(target, 'wb') as target_file:
            data = source_file.read(512)
            while data:
                target_file.write(data)
                data = source_file.read(512)


file_copy('ScreenShot.png', '/Users/zhouyujie/Desktop/copy2.png')