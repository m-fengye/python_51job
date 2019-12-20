import time
import pymysql
import re
from tkinter import _flatten
from collections import Counter
from pyecharts import Geo
from pyecharts.base import Base

t1 = time.time()
conn = pymysql.connect("localhost", "root", "woaini17899589ai", "51job_python", charset='utf8')
t2 = time.time()
cursor = conn.cursor()
sql = "select address from 51job"
cursor.execute(sql)
add = cursor.fetchall()
# print(add)
add_list = list(map(list, add))
# print(add_list)
add_list1 = list(_flatten(add_list))
#print(add_list1)
city_cubs = ['海门', '鄂尔多斯', '招远', '舟山', '齐齐哈尔', '盐城', '赤峰', '青岛', '乳山', '金昌', '泉州', '莱西', '日照',
             '胶南', '南通', '拉萨', '云浮', '梅州', '文登', '上海', '攀枝花', '威海', '承德', '厦门', '汕尾', '潮州', '丹东',
             '太仓', '曲靖', '烟台', '福州', '瓦房店', '即墨', '抚顺', '玉溪', '张家口', '阳泉', '莱州', '湖州', '汕头', '昆山',
             '宁波', '湛江', '揭阳', '荣成', '连云港', '葫芦岛', '常熟', '东莞', '河源', '淮安', '泰州', '南宁', '营口', '惠州',
             '江阴', '蓬莱', '韶关', '嘉峪关', '广州', '延安', '太原', '清远', '中山', '昆明', '寿光', '盘锦', '长治', '深圳',
             '珠海', '宿迁', '咸阳', '铜川', '平度', '佛山', '海口', '江门', '章丘', '肇庆', '大连', '临汾', '吴江', '石嘴山',
             '沈阳', '苏州', '茂名', '嘉兴', '长春', '胶州', '银川', '张家港', '三门峡', '锦州', '南昌', '柳州', '三亚', '自贡',
             '吉林', '阳江', '泸州', '西宁', '宜宾', '呼和浩特', '成都', '大同', '镇江', '桂林', '张家界', '宜兴', '北海',
             '西安', '金坛', '东营', '牡丹江', '遵义', '绍兴', '扬州', '常州', '潍坊', '重庆', '台州', '南京', '滨州', '贵阳',
             '无锡', '本溪', '克拉玛依', '渭南', '马鞍山', '宝鸡', '焦作', '句容', '北京', '徐州', '衡水', '包头', '绵阳',
             '乌鲁木齐', '枣庄', '杭州', '淄博', '鞍山', '溧阳', '库尔勒', '安阳', '开封', '济南', '德阳', '温州', '九江',
             '邯郸', '临安', '兰州', '沧州', '临沂', '南充', '天津', '富阳', '泰安', '诸暨', '郑州', '哈尔滨', '聊城', '芜湖',
             '唐山', '平顶山', '邢台', '德州', '济宁', '荆州', '宜昌', '义乌', '丽水', '洛阳', '秦皇岛', '株洲', '石家庄',
             '莱芜', '常德', '保定', '湘潭', '金华', '岳阳', '长沙', '衢州', '廊坊', '菏泽', '合肥', '武汉', '大庆']
shengfens = ['重庆市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省',
             '山东省', '河南省', '湖北省', '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省']
for i in range(0, len(add_list1)):
    for city_cub in city_cubs:
        pattren = re.compile(str(city_cub) + '.*[\u4e00-\u9fa5]*', re.S)
        add_list1[i] = re.sub(pattren, city_cub, add_list1[i])
for shengfen in shengfens:
    while shengfen in add_list1:
        add_list1.remove(shengfen)

while '异地招聘' in add_list1:
    add_list1.remove('异地招聘')
while '临沧' in add_list1:
    add_list1.remove('临沧')
while '宣城' in add_list1:
    add_list1.remove('宣城')
while '怒江' in add_list1:
    add_list1.remove('怒江')
while '来宾' in add_list1:
    add_list1.remove('来宾')
while '池州' in add_list1:
    add_list1.remove('池州')
while '达州' in add_list1:
    add_list1.remove('达州')
while '迪庆' in add_list1:
    add_list1.remove('迪庆')

count = Counter(add_list1)
count_dict = dict(count)
x, y = Base.cast(count_dict)
# print(x)
# print(y)

geo = Geo("python岗位工作需求城市统计图", "date:10.20--11.20", title_color="#fff",
          title_pos="center", width=1500,
          height=850, background_color='#404a59')

geo.add("", x, y, visual_range=[50, 2500], maptype='china', visual_text_color="#fff",
        visual_type='color', symbol_size=15, is_visualmap=True)
geo.render()
print('success')