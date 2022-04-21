# _*_ coding: utf-8 _*_
from apps import createApp
from settings import PORT
if __name__ == "__main__":
    app = createApp()
    app.run(port=PORT)
