# _*_ coding: utf-8 _*_
import settings
from flask import Flask
from .weather.view import weatheBluePrint

def createApp() -> Flask:
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    app.config.from_object(settings)
    # 蓝图绑定
    app.register_blueprint(weatheBluePrint)
    return app