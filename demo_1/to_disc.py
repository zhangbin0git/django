#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-4-1 0:38 
# @Author : Mark 
# @Site :  
# @File : to_disc.py 
# @Software: PyCharm Community Edition

import pandas as pd
df=pd.read_excel('company.xlsx')
company_data=[]
for i in df.index:
    print(i)
    #获取行号的索引，并对其进行遍历：
    #根据i来获取每一行指定的数据 并利用to_dict转成字典
    row_data=df.ix[i, ['id', 'lng', 'lat', 'mapCity', 'mapDistrict', 'mapProvince', 'userName']].to_dict()
    company_data.append(row_data)
print("最终获取到的数据是：{0}".format(company_data))
print(len(company_data))
with open('result.txt', 'w') as f:
    f.write(str(company_data))
