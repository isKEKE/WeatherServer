# _*_ coding: utf-8 _*_
import types

class WeatherStruct(object):
    '''天气预报数据结构'''
    '''今日数据'''
    # 温度
    today_temperature = None
    # 天气
    today_weather = None
    # 凤向
    today_wind_direction = None
    # 风向级别
    today_wind_direction_level = None
    # 空气质量
    today_air_quality = None
    # 相对湿度
    today_relative_humidity = None


    def json(self) -> dict:
        '''转json数据'''
        _Json_Datas = {}
        for attrName in dir(WeatherStruct):
            attr = getattr(self, attrName)
            if type(attr) == types.MethodType:
                pass
            elif attrName[:2] == "__":
                pass
            else:
                _Json_Datas[attrName] = attr
        else:
            return _Json_Datas


if __name__ == "__main__":
    print(WeatherStruct().json())
