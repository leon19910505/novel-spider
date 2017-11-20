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

