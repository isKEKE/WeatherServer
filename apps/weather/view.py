# _*_ coding: utf-8 _*_
from flask import Blueprint
from flask import request
from flask import jsonify
from .module.WeatherSpider import WeatherSpider
from settings import VERIFY_KEY

# 蓝图
weatheBluePrint = Blueprint("weather", __name__)

# 异常信息
errorInfo = {
    "code": 500,
    "msg": "error"
}

@weatheBluePrint.route("/weather", methods=["GET", "POST"], endpoint="weather")
def weather():
    global errorInfo
    if request.method == "POST":
        # 增加一个简易的判断身份的form-data参数
        pwd = request.form.get("verify")
        if pwd != VERIFY_KEY:
            return errorInfo

        # 爬虫爬取数据
        ws = WeatherSpider()
        ws.sendGet()
        ws.parse()
        
        # 正确信息
        successInfo = {
            "code": 0,
            "msg": "success",
            "data": ws.weatherData.json()
        }

        # 返回JSON数据
        return jsonify(successInfo)

    else:
        return jsonify(errorInfo)
