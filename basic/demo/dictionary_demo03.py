"""
JSON格式的字符串
1、两个异构系统之间交换数据最好的选择是交换纯文本（可以屏蔽系统和编程语言的差异）
2、纯文本应该是结构化或半结构化的纯文本（有一定的格式）
- XML
- JSON
- YAML
3、如何将JSON格式转化为字典
    json 模块 ---> loads 函数
"""
import json
data = """{
  "code": 200,
  "msg": "success",
  "newslist": [
    {
      "title": "广东东莞报告2例无症状感染者",
      "hotnum": 7608117,
      "digest": "12月13日，广东东莞市大朗镇在对返莞人员核酸检测中，发现2例新冠肺炎无症状感染者。目前两人已转运至定点收治医院隔离治疗。"
    },
    {
      "title": "汉文帝霸陵确定为西安江村大墓",
      "hotnum": 4385084,
      "digest": "12月14日，国家文物局在北京召开线上会议，考古队员通过精细发掘和缜密分析，判断出“江村大墓”就是汉文帝的霸陵。"
    },
    {
      "title": "浙江新增本土确诊44例",
      "hotnum": 3491764,
      "digest": "12月13日0-24时，浙江新增确诊病例45例，其中杭州市2例、宁波市4例、绍兴市38例、境外输入1例(刚果金输入)。"
    }
  ]
}"""
# loads()函数可以将JSON格式的数据转成字典
new_dict = json.loads(data)
new_list = new_dict['newslist']
print(new_list)
for new in new_list:
    print(new['title'])
    print(new['digest'])