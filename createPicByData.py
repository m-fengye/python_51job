from pyecharts import Geo


def getPic(keyw, data, minnum, maxnum, path):
    '''
    通过数据在指定位置生成文件
    :param keyw:要搜索的关键字
    :param data:数据
    :param path:生成文件路径+文件名
    :return:
    '''
    geo = Geo(keyw + '岗位工作需求城市统计图', 'data from 51job', title_color="#fff",
              title_pos="center", width=1350,
              height=608, background_color='#404a59', page_title=keyw + '岗位工作需求城市统计图')
    attr, value = geo.cast(data)
    geo.add("", attr, value, visual_range=[minnum, maxnum], maptype='china', visual_text_color="#fff",
            visual_type='color', symbol_size=15, is_visualmap=True)
    geo.render(path)

