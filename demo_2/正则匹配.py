from tools.address_api.address_filter import Address_filter
import addressparser
addr_filter = Address_filter()

def compile_addr(addr_data):
    for df in addr_data:
        address_dict = df
        province = address_dict["省"]
        city = address_dict["市"]
        district = address_dict["区"]
        data = addr_filter.filter(province,city,district)
        print(data)

location_str = ["010050 内蒙古自治区呼和浩特市金川开发区创业园1313号","010010内蒙古自治区呼和浩特市乌兰察布路内蒙古党校宿舍"]

df = addressparser.transform(location_str)
print(df)
compile_addr(df)


import re
import time
import sys
import csv
import pandas as pd
import numpy as np
import datetime
import time
import random
import requests
import os
############查询是否列表里面已经有MAC分配给了这个SN，有的话直接拿出来上传，无需自加分配##
csvFile = open('C:\\Users\\1187206\\Music\\MAC_record.csv', 'ab+')
reader = csv.reader(csvFile)
keywords = []
for row in reader:
    keywords.append(row)
# print(keywords)
for i in range(len(keywords)):
# All_SN = ",".join(keywords[i][0])
    if re.search(sys.argv[1],keywords[i][0])!=None:
    # print All_SN
        if sys.argv[1] in keywords[i][0]:
            print(keywords[i][1])
csvFile.close







