# -*- coding: utf-8 -*-
##天气查看
import urllib.request as r
import json
city = input("please input city's pingyin:")
print(city)
address = "http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996"
print("当前城市天气地址：\n"+address.format(city))
print("1.查看当前天气城市2.查看其他城市天气3.保存当前城市")
menu = input("请输入菜单：")
if menu == "1":
    print("1.查看当前天气城市")
if menu == "2":
    print("2.查看其他城市天气")
if menu == "3":
    print("3.保存当前城市")
info = r.urlopen(address.format(city)).read().decode("utf - 8","ignore")
print(info)
wea_data = json.loads(info)
temp = wea_data["main"]["temp"]
temp_max = wea_data["main"]["temp_max"]
pressure = wea_data["main"]["pressure"]
description = wea_data["weather"][0]["description"]
city_name = wea_data["name"]
print("当前城市：{}\n天气情况:{}\n气压为{}\n温度为{}\n最高温{}".format(city_name,description,pressure,temp,temp_max))