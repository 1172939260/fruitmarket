#爬取url
import requests
#使用正则表达式
import re
#调用getcookies.py中Getcookies方法
from getcookies import Getcookies
#lxml是python的一个解析库，支持HTML和XML的解析，支持XPath解析方式
from lxml import etree
#使用json格式
import json
#codecs专门用作编码转换
import codecs
#from fake_useragent import UserAgent
#f=open('yingtao_url_new_all.txt','a')
#读取cookies.json文件

cookies={}
try:
    cookiefile = open('cookies.json', 'r', encoding='utf-8')
except FileNotFoundError:
    Getcookies()
    cookiefile = open('cookies.json', 'r', encoding='utf-8')
for cookie in json.load(cookiefile)["cookies"]:
    cookies[cookie["name"]] = cookie["value"]
cookiefile.close()

def get_tm_detail(url):
    r = requests.get(url, cookies=cookies, headers=headers)
    r.encoding = 'gb2312'
    # print(r.text)
    doc_tree = etree.HTML(r.text)
    detail = doc_tree.xpath('.//*[@id="J_AttrUL"]/li/text()')
    #print(detail)
    video=re.findall("video",r.text)
    if(len(video)>0):
        hasvideo=1
    else:
        hasvideo=0
    try:
        tmmailname = doc_tree.xpath('.//*[@class="slogo"]/a/strong/text()')[0]
    except IndexError:
        tmmailname='NA'
        f3.write(str(url)+'\n')
    try:
       tmmiaoshu = doc_tree.xpath('.//*[@class="main-info"]/div[1]/div[2]/span/text()')[0]
    except IndexError:
        tmmiaoshu='NA'
    try:
        tmfuwu = doc_tree.xpath('.//*[@class="main-info"]/div[2]/div[2]/span/text()')[0]
    except IndexError:
        tmfuwu='NA'
    try:
        tmwuliu = doc_tree.xpath('.//*[@class="main-info"]/div[3]/div[2]/span/text()')[0]
    except:
        tmwuliu='NA'
    return hasvideo,tmmailname,tmmiaoshu,tmfuwu,tmwuliu,detail

def get_tb_detail(url):
    r = requests.get(url, cookies=cookies, headers=headers)
    r.encoding = 'gb2312'
    #print(r.text)
    doc_tree = etree.HTML(r.text)
    video = re.findall("video", r.text)
    if (len(video) > 2):
        hasvideo = 1
    else:
        hasvideo = 0
    detail = doc_tree.xpath('.//*[@class="attributes-list"]/li/text()')
    try:
       tbmailname = doc_tree.xpath('.//*[@class="tb-shop-name"]/dl/dd/strong/a/@title')[0]
    except IndexError:
        tbmailname='NA'
        f3.write(str(url)+'\n')
    try:
        xinyu_url = doc_tree.xpath('.//*[@class="tb-shop-info-hd"]/div[2]/dl/dd/a/@href')[0]
    except IndexError:
        xinyu_url='NA'
    try:
        tbzhifubao = doc_tree.xpath('.//*[@class="tb-shop-icon"]/dl/dd/a[@class="tb-icon tb-icon-alipay-persion-auth"]/@title')[0]
    except IndexError:
        tbzhifubao = 'NA'
    try:
        tbfoodtezhong = doc_tree.xpath('.//*[@class="tb-shop-icon"]/dl/dd/a[@class="tb-icon tb-icon-food"]/@title')[0]
    except IndexError:
        tbfoodtezhong = 'NA'
    try:
        tbbaozhengjing = doc_tree.xpath('.//*[@class="tb-shop-icon"]/dl/dd/a[@class="tb-seller-bail"]/@title')[0]
    except IndexError:
        tbbaozhengjing = 'NA'
    try:
        tbmiaoshu = doc_tree.xpath('.//*[@class="tb-shop-rate"]/dl[1]/dd/a/text()')[0]
        tbmiaoshu = re.sub('\s', '', tbmiaoshu)
    except IndexError:
        tbmiaoshu = 'NA'
    try:
        tbfuwu = doc_tree.xpath('.//*[@class="tb-shop-rate"]/dl[2]/dd/a/text()')[0]
        tbfuwu = re.sub('\s', '', tbfuwu)
    except IndexError:
        tbfuwu = 'NA'
    try:
        tbwuliu = doc_tree.xpath('.//*[@class="tb-shop-rate"]/dl[3]/dd/a/text()')[0]
        tbwuliu = re.sub('\s', '', tbwuliu)
    except IndexError:
        tbwuliu = 'NA'
    return hasvideo,tbmailname,xinyu_url,tbzhifubao,tbfoodtezhong,tbbaozhengjing,tbmiaoshu,tbfuwu,tbwuliu,detail

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0'}


#'banana'，'putao','apple','caomei','ganju','niuyouguo','li','boluo','cherry'
for m in {'lanmei','lizhi','mangguo','mihoutao','taozi','banana','putao','apple','caomei','ganju','niuyouguo','li','boluo','cherry'}:
    print("start:",m)
    f1=codecs.open('./newdetails/'+m+'_tianmao_information.txt','a','utf-8')
    f2=codecs.open('./newdetails/'+m+'_taobao_information.txt','a','utf-8')
    f3=codecs.open('./newdetails/'+m+'_no get url.txt','a','utf-8')#存取get 信息失败的url
    f4=codecs.open('./newdetails/'+m+'_qiyi.txt','a','utf-8')
    f=codecs.open('./URL/'+m+'_url_new.txt','r','utf-8')
    k=0
    qiyi = {
        'apple':'苹果干|手机|iPhone|罐头|饮料|果汁',
        'banana':'香蕉片|速冻|罐头|饮料|果汁',
        'boluo':'菠萝蜜|菠萝干|真皮|斜挎包|斜跨包|速冻|罐头|饮料|果汁',
        'caomei':'零食|草莓干|草莓脆|草莓碎粒|草莓丁|烘焙|速冻|罐头|饮料|果汁',
        'cherry':'樱桃干|小番茄|小西红柿|零食|圣女果|罐头|速冻|键盘|罐头|饮料|果汁',
        'ganju':'果干|速冻|罐头|饮料|果汁',
        'lanmei':'蓝莓干|蓝莓果干|零食|蓝莓酵|水果干|速冻|罐头|饮料|果汁',
        'li':'梨干|速冻|罐头|饮料|果汁',
        'lizhi':'荔枝干|荔枝粉|荔枝酥|速冻|罐头|饮料|果汁',
        'mangguo':'芒果干|芒果丁|芒果粉|干芒果|烘焙|罐头|速冻|饮料|果汁',
        'mihoutao':'猕猴桃干|猕猴桃汁|饮料|果干|速冻|罐头|饮料|果汁',
        'niuyouguo':'果泥|速冻|冷冻|罐头|饮料|果汁',
        'putao':'葡萄干|葡萄汁|葡萄酒|速冻|罐头|饮料|果汁',
        'taozi':'桃干|桃子干|弥猴桃|速冻|罐头|饮料|果汁',
        }
    a = qiyi[m]
    
    for line in f:
        print(a)
        k+=1
        line1=line.strip().split(',')
        line2=line1[4]
        yiwen=line1[0]
        qiyi = re.findall(a, str(yiwen))
        if(qiyi):
            print("标题有歧义")
            f4.write(str(yiwen)+';'+qiyi[0]+';'+line2+'\n')
        else:
            http = re.search('https', str(line2))
            #print(http)
            if(http):
                url=str(line2)
                print(url)
                #print('ok')
                #url='https://item.taobao.com/item.htm?id=564458907267&ns=1&abbucket=11#detail'
                #url='http://detail.tmall.com/item.htm?id=582875433053&ns=1&abbucket=11'
                res = re.search('detail', url)
                if (res):
                    f2.write(str(line1[0]) + ';' + str(line1[1]) + ';' + str(line1[2]) + ';' + str(line1[3]) + ';' + str(
                        line1[4]) + ';')
                    hasvideo, tbmailname, xinyu_url, tbzhifubao, tbfoodtezhong, tbbaozhengjing, tbmiaoshu, tbfuwu, tbwuliu, detail= get_tb_detail(url)
                    f2.write(str(hasvideo) + ';' +str(tbmailname) + ';'+ str(xinyu_url) + ';' + str(tbzhifubao) + ';' + str(tbfoodtezhong) + ';' + str(tbbaozhengjing) + ';' + str(tbmiaoshu) + ';' + str(tbfuwu) + ';' + str(tbwuliu)+ ';')
                    for i in range(0, len(detail)):
                        f2.write(str(detail[i]) + ';')
                    f2.write('\n')
                    
                else:
                    f1.write(str(line1[0]) + ';' + str(line1[1]) + ';' + str(line1[2]) + ';' + str(line1[3]) + ';' + str(
                        line1[4]) + ';')
                    hasvideo, tmmailname, tmmiaoshu, tmfuwu, tmwuliu,detail=get_tm_detail(url)
                    f1.write( str(hasvideo) + ';'+str(tmmailname) + ';' +str(tmmiaoshu) + ';' + str(tmfuwu) + ';' + str(tmwuliu)+ ';')
                    for i in range(0, len(detail)):
                        f1.write(str(detail[i]) + ';')
                    f1.write('\n')
                    
        
            else:
                url = 'http:' + str(line2)
                print(url)
                # url='https://item.taobao.com/item.htm?id=564458907267&ns=1&abbucket=11#detail'
                # url='http://detail.tmall.com/item.htm?id=582875433053&ns=1&abbucket=11'
                res = re.search('tmall', url)
                res1 = re.search('taobao', url)
                #print(res1)
                if (res):
                    f1.write(str(line1[0]) + ';' + str(line1[1]) + ';' + str(line1[2]) + ';' + str(line1[3]) + ';' + str(
                        line1[4]) + ';')
                    hasvideo, tmmailname, tmmiaoshu, tmfuwu, tmwuliu, detail = get_tm_detail(url)
                    f1.write( str(hasvideo) + ';'+str(tmmailname) + ';' +str(tmmiaoshu) + ';' + str(tmfuwu) + ';' + str(tmwuliu)+ ';')
                    for i in range(0, len(detail)):
                        f1.write(str(detail[i]) + ';')
                    f1.write('\n')
                    
                elif (res1):
                    f2.write(str(line1[0]) + ';' + str(line1[1]) + ';' + str(line1[2]) + ';' + str(line1[3]) + ';' + str(
                        line1[4]) + ';')
                    hasvideo, tbmailname, xinyu_url, tbzhifubao, tbfoodtezhong, tbbaozhengjing, tbmiaoshu, tbfuwu, tbwuliu, detail = get_tb_detail(
                        url)
                    f2.write(str(hasvideo) + ';' +str(tbmailname) + ';'+ str(xinyu_url) + ';' + str(tbzhifubao) + ';' + str(tbfoodtezhong) + ';' + str(tbbaozhengjing) + ';' + str(tbmiaoshu) + ';' + str(tbfuwu) + ';' + str(tbwuliu)+ ';')
                    for i in range(0, len(detail)):
                        f2.write(str(detail[i]) + ';')
                    f2.write('\n')
                    
        print(m,k,'\n')
        print("-----------------------------\n")            
    print(m+' 搞定\n')
'''
f1.close()
f2.close()
f3.close()
f4.close()
'''   