
import codecs

for m in {'lanmei','lizhi','mangguo','mihoutao','taozi','banana','putao','apple','caomei','ganju','niuyouguo','li','boluo','cherry'}:    
    
    f1=codecs.open('./newdetails/'+m+'_taobao_information.txt','r','utf-8')
    set1=['标题', '发货地', '价格', '收货数', 'URL', '视频介绍','商店名称', 'xinyu_url', '淘宝支付宝', '淘宝食品特种', '淘宝保证金', '淘宝描述', '淘宝服务', '淘宝物流', 
          '套餐份量', '货号', '储藏方法', '质地', '直径', '拿包方式', '厂家联系方式', '厂址', 
          '材质工艺', '港澳台', '省份', '系列', '食品品种', '同城服务', '包装方式', '套餐周期', 
          '厂名', '是否为有机食品', '产品标准号', '苹果果径', '水果种类', '箱包硬度', '城市', '是否含糖', 
          '生产许可证编号', '食品添加剂', '单箱规格', '套餐', '适用对象', '单果重量', '价格', '提拎部件类型', 
          '成色', '热卖时间', '果径', '生鲜储存温度', '肩带样式', '配料表', '净含量', '食品工艺', 
          '原产地', '配送频次', '颜色分类', '背包方式', '品牌', '款式', '流行元素', '图案', 
          '规格', '流行款式名称', '里料材质', '内部结构', '适用场景', '商品条形码', '是否可折叠', '售卖方式', 
          '产地', '大小', '产品名称', '闭合方式', '有无夹层', '食品口味', '重量(g)', '形状', 
          '保质期', '县乡镇', '风格', '箱包外袋种类', '特产品类']#83
    set2=['套餐份量', '货号', '储藏方法', '质地', '直径', '拿包方式', '厂家联系方式', '厂址', 
          '材质工艺', '港澳台', '省份', '系列', '食品品种', '同城服务', '包装方式', '套餐周期', 
          '厂名', '是否为有机食品', '产品标准号', '苹果果径', '水果种类', '箱包硬度', '城市', '是否含糖', 
          '生产许可证编号', '食品添加剂', '单箱规格', '套餐', '适用对象', '单果重量', '价格', '提拎部件类型', 
          '成色', '热卖时间', '果径', '生鲜储存温度', '肩带样式', '配料表', '净含量', '食品工艺', 
          '原产地', '配送频次', '颜色分类', '背包方式', '品牌', '款式', '流行元素', '图案', 
          '规格', '流行款式名称', '里料材质', '内部结构', '适用场景', '商品条形码', '是否可折叠', '售卖方式', 
          '产地', '大小', '产品名称', '闭合方式', '有无夹层', '食品口味', '重量(g)', '形状', 
          '保质期', '县乡镇', '风格', '箱包外袋种类', '特产品类']#69
    f2=codecs.open('./huizongdetails/'+m+'_taobao.txt','a','utf-8')
    k=0
    if(k==0):
        k+=1
        for i in range(0,len(set1)):
            f2.write(set1[i])
            if(i<len(set1)-1):
               f2.write(',')
        f2.write('\n')
    
     
    for line in f1:
      list1={}
      line1=line.strip().split(';')
      len1 = len(line1)
      for i in range(0,14):
          f2.write(str(line1[i])+';')
    
      for j in range(13, len1):
          attr = line1[j].split(':')
          
          try:
             list1[attr[0]]=attr[1]
          except IndexError:
              continue
          
      len2=len(set2)    
      for a in range(0,len2-1):
          if(set2[a] in list1.keys()):
              f2.write(str(list1[set2[a]])+';')
          else:
              f2.write('NA'+';')
      
      #最后一项单独写
      if(set2[len2-1] in list1.keys()):
          f2.write(str(list1[set2[len2-1]]))
      else:
          f2.write('NA')
      f2.write('\n')
    
    f1.close()
    f2.close()
    
    
    
    f3=codecs.open('./newdetails/'+m+'_tianmao_information.txt','r','utf-8')
    set3=['标题', '发货地', '价格', '收货数', 'URL', '视频介绍', '商店名称', '天猫描述',  '天猫服务','天猫物流',
          '套餐份量', '货号', '储藏方法', '执行标准号', '直径', '质地', '上市时间', '饮片名称', 
          '厂家联系方式', '性状', '厂址', '材质工艺', '港澳台', '省份', '系列', '是否为有机食品', 
          '同城服务', '包装方式', '套餐周期', '厂名', '食品品种', '产品标准号', '包装规格', '水果种类', 
          '城市', '是否含糖', '生产许可证编号', '食品添加剂', '单箱规格', '套餐', '适用对象', '单果重量', 
          '价格', '成色', '果径', '热卖时间', '销售渠道类型', '生鲜储存温度', '肩带样式', '功能主治', 
          '配料表', '净含量', '原产地', '绿色食品认证编号', '配送频次', '食品工艺', '背包方式', '颜色分类', 
          '品牌', '甜度', '款式', '流行元素', '规格', '图案', '里料材质', '流行款式名称', 
          '生产企业', '内部结构', '适用场景', '商品条形码', '存储方法', '是否可折叠', '售卖方式', '产地', 
          '大小', '喜欢吃脆的冰箱保鲜', '闭合方式', '食品口味', '重量(g)', '形状', '保质期', '县乡镇', 
          '风格', '成熟度', '苹果果径', '特产品类']#86
    set4=['套餐份量', '货号', '储藏方法', '执行标准号', '直径', '质地', '上市时间', '饮片名称', 
          '厂家联系方式', '性状', '厂址', '材质工艺', '港澳台', '省份', '系列', '是否为有机食品', 
          '同城服务', '包装方式', '套餐周期', '厂名', '食品品种', '产品标准号', '包装规格', '水果种类', 
          '城市', '是否含糖', '生产许可证编号', '食品添加剂', '单箱规格', '套餐', '适用对象', '单果重量', 
          '价格', '成色', '果径', '热卖时间', '销售渠道类型', '生鲜储存温度', '肩带样式', '功能主治', 
          '配料表', '净含量', '原产地', '绿色食品认证编号', '配送频次', '食品工艺', '背包方式', '颜色分类', 
          '品牌', '甜度', '款式', '流行元素', '规格', '图案', '里料材质', '流行款式名称', 
          '生产企业', '内部结构', '适用场景', '商品条形码', '存储方法', '是否可折叠', '售卖方式', '产地', 
          '大小', '喜欢吃脆的冰箱保鲜', '闭合方式', '食品口味', '重量(g)', '形状', '保质期', '县乡镇', 
          '风格', '成熟度', '苹果果径', '特产品类']#76
    
    f4=codecs.open('./huizongdetails/'+m+'_tianmao.txt','a','utf-8')
    k=0
    if(k==0):
        k+=1
        for i in range(0,len(set3)):
            f4.write(set3[i])
            if(i<len(set3)-1):
               f4.write(',')
        f4.write('\n')
    
     
    for line in f3:
      list3={}
      line3=line.strip().split(';')
      len3 = len(line3)
      for i in range(0,10):
          f4.write(str(line3[i])+';')
    
      for j in range(9, len3):
          attr = line3[j].split(':')
          
          try:
             list3[attr[0]]=attr[1]
          except IndexError:
              continue
          
      len4=len(set4)    
      for a in range(0,len4-1):
          if(set4[a] in list3.keys()):
              f4.write(str(list3[set4[a]])+';')
          else:
              f4.write('NA'+';')
      
      #最后一项单独写
      if(set4[len4-1] in list3.keys()):
          f4.write(str(list3[set4[len4-1]]))
      else:
          f4.write('NA')
      f4.write('\n')
    
    f3.close()
    f4.close()
    


