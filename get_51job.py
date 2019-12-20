import requests
import re


__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}


def getPageNum(keyw):
    '''
    获取指定关键字的总页数
    :param keyw: 要搜索的关键字
    :return: 总页数
    '''
    try:
        res = requests.get('https://search.51job.com/list/000000,000000,0000,00,9,99,'+keyw+',2,1.html', __headers)
    except Exception as ex:
        return -1
    res = res.text.encode(res.encoding).decode('gbk')
    pattren = re.compile('<span class="td">共(.*?)页，到第</span>')
    pageNum = re.findall(pattren, res)
    try:
        return int(pageNum[0])
    except Exception as ex:
        return  0


def getPageInfo(keyw, pageIndex):
    '''
    获取指定页码的职位信息
    :param keyw: 要搜索的关键字
    :param pageIndex: 要查询的页码
    :return: 指定页码的列表集合
    '''
    try:
        res = requests.get('https://search.51job.com/list/000000,000000,0000,00,9,99,' + keyw + ',2,' + str(pageIndex) + '.html')
    except Exception as ex:
        return None
    res = res.text.encode(res.encoding).decode('gbk')
    # 职位名
    pattren = re.compile('<a target="_blank" title="(.*)" href=".*"  onmousedown="">')
    post = re.findall(pattren, res)
    # 公司名
    pattren = re.compile('<span class="t2"><a.*?>(.*?)</a></span>')
    company = re.findall(pattren, res)
    # 工作地点
    pattren = re.compile('<span class="t3">(.*?)</span>')
    address = re.findall(pattren, res)
    # 薪资
    pattren = re.compile('<span class="t4">(.*?)</span>')
    wages = re.findall(pattren, res)
    # 发布时间
    pattren = re.compile('<span class="t5">(.*?)</span>')
    date = re.findall(pattren, res)
    pageInfo = []
    for j in range(0, len(post)):
        postInfo = []
        postInfo.append(post[j])
        postInfo.append(company[j])
        postInfo.append(address[j+1])
        postInfo.append(wages[j+1])
        postInfo.append(date[j+1])
        pageInfo.append(tuple(postInfo))
    return pageInfo

