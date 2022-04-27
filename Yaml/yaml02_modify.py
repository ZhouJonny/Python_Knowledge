"""
修改yaml文件里value的值
如将data_dict.yaml 中age改为25
"""
import yaml


def set_state(key1, key2, state):
    with open(r'data/data_dict.yaml') as file:
        doc = yaml.load(file, Loader=yaml.FullLoader)

    doc[key1][key2] = state

    with open(r'data/data_dict.yaml', 'w') as file:
        yaml.dump(doc, file)


set_state('person', 'age', 25)
