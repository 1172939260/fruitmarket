# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:09:25 2018

@author: xiaoyuan
"""
# -*- coding: utf-8 -*-
import re
from getcookies import Getcookies
import codecs
import json
import time
import requests

print(time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time())))
start = time.clock()
print(start)
#参考https://blog.csdn.net/weixin_39523034/article/details/80152833
#from fake_useragent import UserAgent
#proxies=json.load(open("proxies.json", 'r', encoding='utf-8'))
f=codecs.open('apple_url_new.txt','a','utf-8')
cookies={}
try:
    cookiefile = open('cookies.json', 'r', encoding='utf-8')
except FileNotFoundError:
    Getcookies()
    cookiefile = open('cookies.json', 'r', encoding='utf-8')
for cookie in json.load(cookiefile)["cookies"]:
    cookies[cookie["name"]] = cookie["value"]
cookiefile.close()

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0'}
#User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1
#for N in range(2,101):
#i=23

#i=1
i=77
q=0
for N in range(i,100):
    #翻页该url是有规律可循的，其主要变量在data-value、时间戳_ksTS、callback以及s
    #进行翻页模拟需要引入time
    ktsts = time.time()
    _ksTS = '%s_%s' % (int(ktsts * 1000), str(ktsts)[-3:])
    callback = "jsonp%s" % (int(str(ktsts)[-3:]) + 1)
    data_value = 44 * N
    s=44*N
    xiaoliangurl='https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS={}\
        &callback={}&q=苹果+水果&imgfile=&js=1&stats_click=search_radio_all%3A1\
        &initiative_id=staobaoz_20181223&ie=utf8&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s={}'.format(data_value,_ksTS,callback,s)
    #print(xiaoliangurl)
    #使用requests爬取得到类似json文件，然后使用正则进行筛选，爬数据时最好先打印出来再进行筛选
    r = requests.get(xiaoliangurl, cookies=cookies, headers=headers).text
    g_page_config = re.compile(r'[(](.*)[)]', re.S)
    
    gg = re.findall(g_page_config, r)[0]
    #print(gg)
    data = json.loads(gg)
    #print(data)
    print(time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time())))
    #time.sleep(5)
    #print(time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time())))
    #获取信息列表
    try:
        page_item = data['mods']['itemlist']["data"]["auctions"]
        #查看店铺数目
        print(len(page_item))
        for i in range(0, len(page_item)):
            #提取店铺标题，发货地点，价格，付款人数，商品URL
            title = page_item[i]['raw_title']
            item_loc = page_item[i]['item_loc']
            view_price = page_item[i]['view_price']
            view_sales = page_item[i]['view_sales']
            a=re.match(r'([0-9].*)人收货', view_sales, re.M|re.I)
            a=a.group(1)
            print(str(a))
            if str(a)>'0':
                detail_url = page_item[i]['detail_url']
            #print(detail_url)
            #写入到txt中，以后可以考虑写入到excel中
                f.write(str(title) + ',' + str(item_loc) + ',' + str(view_price) + ',' + str(view_sales) + ',' + detail_url + '\n') 
            else:
                q=1
                break
        print("0ver:",N)
    except:
        end = time.clock()
        print(end)
        print(time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time())))
        print("被攻击了,"+"程序运行时间：%d second"%(end-start))
        break
    
    if q==1:
        print("第%d页有付款人数为0"%(N+1))
        break