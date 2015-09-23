# cloud56
## 学习和使用scrapy框架爬取cloud56网车源数据
这次算是认真的学习了一下爬虫框架，以前爬取数据都是利用nodejs的request、superagent、urllib
或者是使用python的urllib2、requests模块来做一些小爬虫，没尝试过使用框架来做网络爬虫。
昨天看了一天的官方文档，也查阅了一些博客资料，终于对scrapy有了一个稍微清晰的认识，于是想着爬取一个网站来练练手。

之前选取了中国物通网，但是由于其使用了将手机号加密成图片的方式，尝试使用pytesser库进行图片文字识别，但是会多出一些数字，于是暂时放弃。其他的网站需要模拟用户登录，可能我选的不巧，登录都是经过了好几次跳转。

选择这个网站主要是因为仅仅用到了一个反防盗链的中间件，这样就可以正常爬取子页面的内容。

另外在xpath和css之间徘徊了好久，由于谷歌有个很好用的xpath插件
于是果断投入了xpath的怀抱。

# Use
1. 安装scrapy不用说
2. ```cd cloud56```
3. ```scrapy crawl cloudspider```
4. 等待命令行输出


# Todos:
1. 模拟用户登录
2. 防止被ban
3. redis或者mongo以及postgres接入
