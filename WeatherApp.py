# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:30:48 2018

@author: lenovo
"""

# -*- coding: utf-8 -*-
import urllib.request as r
import json
import time
print('''亲爱的小主人欢迎来到***天气预报频道***\n''')
time.sleep(3)
print('''下面将为您播报未来四天09:00:00天气情况''')
city = input("please input city's pingyin:")
address = "http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
#print("当前城市天气地址：\n"+address.format(city))
print("1.查看\"{}\"天气城市2.查看其他城市天气3.保存当前城市".format(city))
menu = input("请输入菜单：")
if menu == "1":
    print("1.查看当前天气城市")
if menu == "2":
    print("2.查看其他城市天气")
if menu == "3":
    print("3.保存当前城市")
info = r.urlopen(address.format(city)).read().decode("utf - 8","ignore")
wea_data = json.loads(info)
for i in range(32)[:-1:8]:
    dt_txt = wea_data["list"][i]["dt_txt"]
    temp = wea_data["list"][i]["main"]["temp"]
    temp_max = wea_data["list"][i]["main"]["temp_max"]
    pressure = wea_data["list"][i]["main"]["pressure"]
    description = wea_data["list"][i]["weather"][0]["description"]
    city_name = wea_data["city"]["name"]
    print("当前城市：{}\n时间:{}\n当前天气:{}\n气压为:{}\n温度为:{}\n最高温:{}\n\t".format(city_name,dt_txt,description,pressure,temp,temp_max))
    print("*****当日天气播报结束*****\n")
print("当前城市天气播报完毕，感谢您的使用！")

time.sleep(20)






