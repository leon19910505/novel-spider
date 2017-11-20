# 顶点免费小说爬虫
使用scrapy, mongodb,berkeley-db实现的一个小说爬虫,底层存储mongodb,支持去重berkeley-db，scrapy-deltafetch，scrapy-magicfields。

# Install 
* scrapy  基于Python的爬虫框架
```
    pip install scrapy 
```
* berkeley-db 一个高性能的key-value 嵌入式数据库，这里用来存储url记录，去重过滤，当然也可以用redis实现
```
    brew install berkeley-db4
```
* bsddb3, 用来连接 berkeley-db 的 py 模块，安装的时候有可能报找不到berkeley-db驱动的错误，所以前面加上了BERKELEYDB_DIR=$(brew --cellar)/berkeley-db@4/4.8.30，这里是mac下通过brew安装后的berkeley-db路径，实际操作改为自己的路径
```
    BERKELEYDB_DIR=$(brew --cellar)/berkeley-db@4/4.8.30 pip install bsddb3
```     
* scrapy-deltafetch，一个已经写好的middleware 过滤，安装后通过配置进行去重
```
    pip install scrapy-deltafetch
```
* scrapy-magicfields ，用于配置去重的验证字段，可以通过自定义字段来定义去重规则
```
    pip install scrapy-magicfields
```
Python ，mongodb 的安装就不列出了，可自行百度

# Config
* 设置settings.py：
```
    添加去重的 middleware ，顺序要在pipline之前
    SPIDER_MIDDLEWARES = {
   'scrapy_deltafetch.DeltaFetch': 50, 
   'scrapy_magicfields.MagicFieldsMiddleware': 51,
    }
    DELTAFETCH_ENABLED = True
    MAGICFIELDS_ENABLED = True
    去重使用到的字段，这里是通过url去重，爬过的url不会再爬
    MAGIC_FIELDS = {
        "url": "$response:url",
    }

```
# Run
```
    scrapy crawl dingdian
```
# 去重效果展示
![](https://github.com/leon19910505/novel-spider/raw/master/show.png) 
