# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:30:58 2018

@author: Administrator
"""
import codecs

f1=codecs.open('./huizongdetails/apple_taobao.txt','r','utf-8')
for line in f1:
    a=line.strip().split(';')
    print(len(a))
    