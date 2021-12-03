# WeatherServer# <天气预报服务端搭建和使用>

## 一、本章前言

> 本脚本是桌面挂件天气预报UI应用而搭建的前置。当然了搭建其他flask服务也可以使用此方式。

## 二、系统环境

- ubuntu18.04
- python3.8+以上
- Nginx

- requests
- flask

## 三、代码安装

```python
# ubuntu安装git
sudo apt-get install git
# 使用git指令，它会在当前路径下下载git仓库里面代码
git clone https://github.com/isKEKE/WeatherServer.git
```

## 四、Python环境搭建

> python简易相关操作。

```python
'''
请先查看服务器默认Python3的版本。
为什么要python3.8以上，因为作者
我编写环境是python3.8.10.当然低
版本应该也可以。'''
# 这个搭建只适合不懂linux相关指令的.大佬可直接自己编译python源码。
# 安装Python3.8. 当安装完成之后进入python3.8的指令是python3.8。
# 如果链接 python3 or python 这种软路径，请百度。
sudo apt-get install python3.8

# 安装flask。注意：ubuntu服务端是否有安装pip3，没有请查询相关安装操作。
# 为什么是pip3,而非pip, 因为ubuntu我的系统pip3绑定的python3
pip3 install flask

# 安装requests
pip3 install requests
```

## 五、Nginx的搭建

> Nginx, 我这里只是简单配置。

```python
# 安装
sudo apt-get install nginx

# 查看是否安装
nginx -v

# 启动nginx, 这个时候你可以使用远程浏览器通过host访问查看。
service nginx start

'''
现在要进行一个反向代理，即：端口转发。为什么要这样做？
当我们浏览器通过host或域名访问服务器时，默认不写端口
是80，流程：http://hostname/ -访问> 服务器 -80>
nginx -转发> python-flask-weather(端口)，最直观
好处，你访问你服务器域名不用写端口。哈哈，当然真实不
是这样的，nginx这种高并发内存消耗小服务器反代理插件
好处很多，可以百度详细查询。
'''
# 打开nginx配置文件，默认都是这个
sudo vi /etc/nginx/sites-enabled/default

# 在 server{...} 前添加。这种操作一般在多服务器上使用
upstream flask_weather{
    server HOSTNAME:PORT;
}

# 在server{...}找到 location / {...}，其中添加一条
# 并注释掉try_files $uri $uri/ =404; 语句
proxy_pass http://flask_weather;

# nginx 重启
sudo systemctl reload nginx
```

- 安装成功展示

![](https://github.com/isKEKE/ImgLib/blob/main/%E6%9D%82%E9%A1%B9/66a5378e4cf9900de33c445a69e5f64.png?raw=true)

## 六、Screen 搭建

> 当我们需要服务器长时间运行一个程序就需要这个。

```python
# 安装
sudo apt-get install screen

# 创建一个screen会话
screen -S weather[会话名称]

# 创建若干个窗口, 先按ctrl+a, 然后松开按c
ctrl+a c

# 查看后台
screen -ls

# 查看窗口情况，快捷键：
ctrl+a w

# 进入某下一个窗口，或某序号窗口
ctrl+a n | ctrl+a 序号

# 关闭当前窗口
ctrl+a k

# 脱离screen会话
ctrl+a d

# 重新进入screen
screen -r weather[会话名称]
```

## 七、代码介绍

> 这里作者默认认为你已经进入screen会话中，且前面相关已经搭建完成。

- 代码结构

```python
WeatherServer
|__apps			# 核心代码
    |__`__init__.py` 	# 封装代码
    |__weather 			# 天气预报蓝图
     	|__view.py			# 蓝图文件
    	|__module			# 蓝图功能
        	|_...
        
|__apps.py 		# 运行文件

|__settings.py 	# 配置文件
```



- 代码配置

```python
'''先进入代码所在更目录'''
# 修改settings.py中的配置
POST = None # <- 服务器端口，根据前面nginx转发为8999，那么这里尽量也8999

# 中国天气网：http://www.weather.com.cn/weather/101010100.shtml
CITY_ID = None # <- 地区ID，中国天气网查找所在ID

# 验证密钥，为了防止其他人通过链接获取数据。因为它最终服务于我写的桌面挂件UI。
VERIFY_KEY = None # <- 这里只是一个简单的验证操作，设置成你自己的验证字串。

# 运行脚本, 为什么python3.8, 因为apt安装python3.8，默认指令是这个。
python3.8 apps.py
# ok现在你可以通过链接访问服务器了
```

- 测试代码

```python
# _*_ coding: utf-8 _*_
import requests

def main() -> None:
    url = "http://hostname/weather"
    data = {
        "verify": "VERIFY_KEY"
    }
    response = requests.post(url, data=data)
    print(response.json())

if __name__ == "__main__":
    main()
```

- 测试图片

![](https://github.com/isKEKE/ImgLib/blob/main/%E6%9D%82%E9%A1%B9/294823a05e8eb6fc95d84572d544ed9.png?raw=true)

## 八、作者注释

- 作者

  `珂珂`

- 邮箱

  `li_99999@126.com`

- 注释

  这个说明文档可能不是很详细，它也只是一个简单的关于ubuntu系统服务端搭建flask+nginx的简易概括，详细还请百度查看相关资料。其中若有错误可以指出发送到我邮箱。关于桌面挂件的说明文档我有时间会尽量写完，那个东西有点多，而且我本人写文档和语言组织也不好，请见谅。

  
