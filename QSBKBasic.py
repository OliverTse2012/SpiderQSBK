#一个简单的示例爬虫-糗事百科
#参考:林炳文Evankaka(博客：http://blog.csdn.net/evankaka/),Python爬虫学习系列教程

import urllib.request
import re

page = 1
weburl = "http://www.qiushibaike.com/hot/page/" + str(page)
webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=weburl, headers=webheader)
webPage=urllib.request.urlopen(req)
data = webPage.read()
data = data.decode('UTF-8')
#print(data)
#pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
#                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)

pattern = re.compile('<div.*?content">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
items = re.findall(pattern, data)
for item in items:
    haveImg = re.search("img", item[1])
    if not haveImg:
        print(item[0], item[1], item[2])