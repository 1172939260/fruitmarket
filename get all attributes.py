import codecs
import re
#查看14种水果属性集合

set1=set()
set2=set()
for m in {'lanmei','lizhi','mangguo','mihoutao','taozi','banana','putao','apple','caomei','ganju','niuyouguo','li','boluo','cherry'}:
    f1=codecs.open('./newdetails/'+m+'_taobao_information.txt','r','utf-8')
    f2=codecs.open('./newdetails/'+m+'_tianmao_information.txt','r','utf-8')
    
    
    for line in f1:
        line1=line.strip().split(';')
        len1=len(line1)
        for i in range (14,len1):
            line11=line1[i]
            attr=line11.split(':')[0]
            if(attr!=''):
                set1.add(attr)
    #print('taobao',set1,len(set1))
    #print('---------------------\n')
    f1.close()
   
    
    for line2 in f2:
        line2=line2.strip().split(';')
        len2=len(line2)
        for i in range (10,len2):
            line22=line2[i]
            attr=line22.split(':')[0]
            match=re.search('：',str(attr))
            if(match):
                attr=attr.split('：')[0]
            if(attr!=''):
                set2.add(attr)
    #print('tianmao',set2,len(set2))
    #print('---------------------\n')
    f2.close()
    
print('taobao',set1,len(set1))
print('---------------------\n')
print('tianmao',set2,len(set2))


'''
#查看各水果属性集合
for m in {'lanmei','lizhi','mangguo','mihoutao','taozi','banana','putao','apple','caomei','ganju','niuyouguo','li','boluo','cherry'}:
    f1=codecs.open('./newdetails/'+m+'_taobao_information.txt','r','utf-8')
    f2=codecs.open('./newdetails/'+m+'_tianmao_information.txt','r','utf-8')
    set1=set()
    set2=set()
    
    for line in f1:
        line1=line.strip().split(';')
        len1=len(line1)
        for i in range (14,len1):
            line11=line1[i]
            attr=line11.split(':')[0]
            if(attr!=''):
                set1.add(attr)
    print(m,'taobao',set1,len(set1))
    print('---------------------\n')
    f1.close()
   
    
    for line2 in f2:
        line2=line2.strip().split(';')
        len2=len(line2)
        for i in range (10,len2):
            line22=line2[i]
            attr=line22.split(':')[0]
            match=re.search('：',str(attr))
            if(match):
                attr=attr.split('：')[0]
            if(attr!=''):
                set2.add(attr)
    print(m,'tianmao',set2,len(set2))
    print('---------------------\n')
    f2.close()
'''    