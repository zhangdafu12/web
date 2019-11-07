# -*- coding: utf-8 -*-
# import operator
# from collections import Counter
# ids = [11,1,1,1,12,2,2,1,2,3,4,5,5,5,5,5]
# c_id = Counter(ids)
# ided = sorted(c_id.items(), key=operator.itemgetter(1), reverse=True)
# result = []
# if len(ided)>5:
#     for i in ided[0:5]:
#         result.append(i[0])
# else:
#     for i in ided:
#         result.append(i[0])
# print(result)
# def deal_word(word):
#     word = word.replace(' ','').replace('\n','').replace('\r\t','')
#     return word
#
#
# a = {'url': 'http://127.0.0.1:5000/news/detail/6864', 'mousemove': [['\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 3171], ['\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 1234], ['\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 1414]], 'mouseclick': [['click', '\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 1559669840965], ['click', '\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 1559669843606], ['click', '\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 1559669845734], ['click', '\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 1559669845902], ['dblclick', '\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 1559669845904], ['click', '\n                        数据显示：美国2017财年财政赤字创新高\n                    ', None, None, 1559669846069]], 'keyboard': [], 'locationarray': [[0, 500]], 'time': 100}
# print()
# def cal_interest():
#     result = set()
#     if '/news/detail/' in a['url']:
#         news_id = a['url'].replace('http://127.0.0.1:5000/news/detail/','')
#
#     for i in a['mousemove']:
#         result.add(deal_word(i[0]))
#     for i in a['mouseclick']:
#         result.add(deal_word(i[1]))
a = ['2008年10月汶川大地震，乔治带领45人的医疗团来到了四川，带去了大量资金和灾区急需的常备药，得到了社会各界的肯定和好评', '\u3000\u3000没想到让外国医生看了回病\u3000\u30002008年10月18日，由全科医生、理疗师、口腔等专家、教授组成的美国亚洲医疗服务交流中心的美国ROCK医疗队刚到达法库县就在法库县中心医院里设置诊室', '仅2008年10月19日当天，美国ROCK医疗队就为百名贫困农民进行了免费义诊', '\u3000\u3000医疗队全程自费义诊\u3000\u3000乔治是ROCK医疗队的队长，17年前第一次来到中国']
b = [[[], [], [], [], [], [], [], [], [], [], [('队员', '美国', '佛罗里达州')], [], [], [], [], [], [], [], []]]
{'白求恩': (0.75, 2), '乔治': (0.5, 5), '张老汉': (0.75, 2), '宿鲁': (0.5, 1)}, {}, {'ROCK': (1.0, 8)}
['美国佛罗里达州', '美国亚洲', '法库县', '沈阳市', '汶川', '四川', '中国']
{'红十字会': (1.0, 1), '美国ROCK医疗队': (2.25, 2), '美国亚洲医疗服务交流中心': (3.0, 1), '法库县中心医院': (1.75, 1), '沈阳市红十字会': (1.75, 1), '医疗队': (0.75, 1)}

