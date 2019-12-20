import get_51job as g
import mySqlHelper as mysql
import createPicByData as cpd
import convertData as cData
import webbrowser
import urllib.parse
import string

# ------------------------------开始爬取完成------------------------------

keyw = input('请输入职位名：')
encode_new_keyw = urllib.parse.quote(keyw, safe=string.printable)
allInfo = []
pageNum = g.getPageNum(encode_new_keyw)
if pageNum == -1:
    print('[-]网络出现问题，请检查网络')
    exit(0)
elif pageNum == 0:
    print('[-]未获取到页数')
    exit(0)
i = 0
while i < pageNum:
    i += 1
    print('[*]正在爬取第' + str(i) + '页（共' + str(pageNum) + '页）数据')
    pageInfo = g.getPageInfo(encode_new_keyw, i)
    if pageInfo is not None:
        allInfo.extend(pageInfo)
    else:
        print('[-]网络错误，未爬取到第'+str(i)+r'页数据，输入y重试：', end='')
        if input() == 'y':
            i -= 1
        else:
            exit(0)
print('[+]爬取完成，共'+str(len(allInfo))+'条数据')
# ------------------------------爬取数据完成------------------------------
# ------------------------------开始写入数据------------------------------
print('[*]准备写入mysql...')
rows = mysql.resetTable("localhost", "root", "woaini17899589ai", "51job_python", 'utf8', '51job')
if rows == -2:
    print('[-]连接数据库失败')
elif rows == -1:
    print('[-]重置表数据失败')
elif rows == 0:
    print('[+]重置表数据成功')
print('[*]正在写入mysql...')
rows = mysql.insertDB("localhost", "root", "woaini17899589ai", "51job_python", 'utf8', '51job', allInfo)
if rows == -2:
    print('[-]连接数据库失败，未写入本次数据')
elif rows == -1:
    print('[-]写入数据失败，未写入本次数据')
elif rows >= 0:
    print('[+]写入数据库成功，共写入'+str(rows)+'条数据')
# ------------------------------写入数据完成------------------------------
# ------------------------------读取数据开始------------------------------
print('[*]正在读取mysql...')
data = mysql.selectDB("localhost", "root", "woaini17899589ai", "51job_python", 'utf8', '51job','address')
if data == -2:
    print('[-]连接数据库失败')
elif data == -1:
    print('[-]读取数据失败')
else:
    print('[+]读取数据成功')
# ------------------------------读取数据开始------------------------------
# ------------------------------生成文件开始------------------------------
    print('[*]正在生成文件...')
    data = cData.convert(data)
    if data:
        minnum, maxnum = data[min(data, key=data.get)], data[max(data, key=data.get)]
    else:
        minnum, maxnum = 0, 0
    cpd.getPic(keyw, data, minnum, maxnum, 'render.html')
    print('[+]生成文件成功')
    webbrowser.open("render.html")
# ------------------------------生成文件结束------------------------------
