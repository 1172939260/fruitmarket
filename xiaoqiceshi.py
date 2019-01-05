# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
import codecs

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

qiyihuizong={}
for m in {'apple','banana','boluo','caomei','cherry','ganju','lanmei','li','lizhi','mangguo','mihoutao','niuyouguo','putao','taozi'}:
    f=codecs.open('./URL/'+m+'_url_new.txt','r','utf-8')    
    a=qiyi[m]
    c=[]
    all=0
    lineqiyi=0
    for line in f:
        all=all+1
        line1=line.strip().split(',')
        line2=line1[0]
        http = re.findall(a, str(line2))
       
        c.append(http)
        if(len(http)>0):
            lineqiyi+=1
    youxiaonum=all-lineqiyi
    print(m+'all:',all)
    print(m+'shenyu:',youxiaonum)
    jieguo=[]
    for i in range(0,len(c)):
        for ii in range(0,len(c[i])):
            jieguo.append(c[i][ii])
    
    result = {}
    
    for i in set(jieguo):
        result[i] = jieguo.count(i)
    qiyinum=sum(result.values())
    #print(qiyinum)
   
    print(m,result)
    print('---------------------------------')
    qiyihuizong[m]=result

print(qiyihuizong)
    
