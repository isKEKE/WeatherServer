# _*_ coding: utf-8 _*_
import time
import requests
import json
import settings
from .WeatherStruct import WeatherStruct
from .UserAgent import UserAgent


class WeatherSpider(object):
    '''天气预报爬虫'''
    def __init__(self, city_id: str):
        self.api = f"http://d1.weather.com.cn/sk_2d/{city_id}.html"
        # 响应体
        self.__response = None
        # 数据存储
        self.weatherData = WeatherStruct()


    def setHeaders(self) -> dict:
        return {
            "User-Agent": UserAgent.random(),
            "Referer": "http://www.weather.com.cn/"
        }


    def setParams(self) -> dict:
        '''设置链接参数'''
        return {
            "_": f"{int(time.time() * 1000)}"
        }


    def sendGet(self) -> None:
        '''发送请求'''
        response = requests.get(
            url=self.api,
            headers=self.setHeaders(),
            params=self.setParams()
        )
        response.encoding = "utf-8"
        self.__response = response


    def parse(self) -> None:
        '''解析响应体'''
        datas = self.__response.text[len("var dataSK="):]
        datas = json.loads(datas)

        # 温度
        self.weatherData.today_temperature = datas.get("temp")
        # 天气
        self.weatherData.today_weather = datas.get("weather")
        # 凤向
        self.weatherData.today_wind_direction = datas.get("WD")
        # 风向级别
        self.weatherData.today_wind_direction_level = datas.get("WS")
        # 空气质量
        self.weatherData.today_air_quality = datas.get("aqi_pm25")
        # 相对湿度
        self.weatherData.today_relative_humidity = datas.get("sd")


    def go(self) -> None:
        '''测试'''
        self.sendGet()
        self.parse()
        print(self.weatherData.json())


if __name__ == "__main__":
    WeatherSpider().go()
