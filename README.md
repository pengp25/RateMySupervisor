# RateMySupervisor
永久免费开源的导师评价数据、数据爬虫、无需编程基础的展示网页以及新信息补充平台

# 如果你对编程没有了解、只想检索数据

我写了一个简单的UI方便检索，可以通过如下方式访问：

+ 在线浏览：**可以直接访问这个[GitHub Pages页面](https://kgco.github.io/RateMySupervisor/)，打开即可在线浏览数据**。网页前端加载出来之后，要加载一个20MB左右的js数据文件，由于网络原因可能速度比较慢，所以会有一小段时间下拉列表里没有数据，请耐心等待。
+ 离线浏览：点击右上方Code按钮中的Download ZIP，下载文件，然后打开`html/index.html`即可浏览数据。由于调用了`bootstrap`和`jquery`，所以打开的时候最好保持网络连接（不打开也行啦，就是UI可能有点乱）。

小TIP：

+ 如果对GitHub不太熟悉，请直接选择在线浏览。
+ 如果考虑到各种不可抗因素，离线浏览的方式更加安全（毕竟也不知道github有没有不能访问的一天）。

# 手机应用

为了支持离线浏览，也可以转换成相关的应用app。
- [x] 安卓APK，有朋友在[这条issue](https://github.com/kgco/RateMySupervisor/issues/6)下提供了将此静态网页转换为安卓APK的工具及转换成品，有需要的朋友可以前往查看和下载。
- [ ] 苹果App，暂时还不支持，欢迎各位提供相关的技术

# 其他相关链接

- [mysupervisor_save](https://github.com/wangzhiye-tiancai/mysupervisor_save) 与高校研究生导师评价相关资源搜集

# 获取原始数据
`data`目录下储存了原始数据，其中：
- `urfire.json`是从[导师推荐网](https://www.urfire.com/) 获取的原始数据，~~该网站目前正常运作，各位也可以前往支持，**本平台开源存储数据以备各种你懂得的不可抗力因素**~~。**该网站目前已停止服务**，但目前已经有一些在本repo数据基础上完成的网站，详情参见issue部分。**本repo仍然为大家永久提供数据存储、下载和查询服务**。
- `comments_data.json`是将数据转换为如下格式的`json`数据
```
[
  {
    "school_cate": "", 
    "university": "", 
    "department": "", 
    "supervisor": "", 
    "rate": 0, 
    "description": ""
  }
]
```

# 爬虫工具
`src/urfire.py`是[导师推荐网](https://www.urfire.com/)的爬虫工具，并包含了一个并行爬取的实例。另有将原始格式转换为上述`comments_data.json`格式的函数。

# UI工具
`html/index.html`是使用`bootstrap`和`jquery`完成的简易的检索页面。数据存储在`html/data.js`中，由`src/html_render.py`通过`comments_data.json`生成。

# 新的数据
我会不定期继续爬取其他数据，有数据的地方也烦请告知。  
另外，朋友们也可以在本平台撰写评价，请前往这条issue：[在本issue下补充导师评价信息](https://github.com/kgco/RateMySupervisor/issues/1)，发帖请使用如下格式，方便爬虫爬取：
>学校类型：985/211/研究机构/其他/(海外院校请用英文直接填写国家名称，如：Japan)
>学校名称：示例：清化大学/Cambridge University  
>院系：示例：化学化工学院/无  
>导师姓名：示例：王五  
>评分：(1-5分制，乐意的话可以填写小数，如：4.8)  
>评价：示例：对学生很好，尽职尽责  

我也会不定期爬取issue数据添加进来。

# 匿名评价
GiHub平台匿名评价比较麻烦，可以考虑使用[匿名评论公用账号](https://github.com/kgco/RateMySupervisor/issues/18)

**祝各位都能有一个顺利美好的研究生生活。**

# 关于捐赠
虽然维护这个repo需要一定的时间，但是我乐意为大家做这件事，而且大家也随时可以给我发pull request一起维护这个repo。而且**这些数据的主体来源是每一位辛苦的科研工作人员的宝贵经验和建议**，而不是我的，我只是把他们的数据收集储存起来，因此**这个repo不打算接受任何捐赠**。

目前urfire网站已经关站，**如果任何一位朋友（或者未来如果我有空的话）愿意重新建站，我希望TA能够在TA的网站上开放捐赠，用来维持服务器的租用成本**，如果需要用到这个repo的数据，备注数据来源后直接引用就可以。

最后，如果未来建站，欢迎大家通过比对网站数据、查阅commit历史的方式监督数据的使用，这样可以杜绝因为利益问题删除部分评论的事情发生。

# 关于贡献新信息
如果您认为这个项目中有的信息有错误，或者有的评价显失公允，您可以考虑为本项目提供新的信息，很高兴有人愿意为这个项目贡献信息。

但是，出于对既有信息的保护考虑，对数据任何形式的修改都是不安全的，尽管您提供的信息是完全正确（因为**我们需要防范有人恶意提交错误信息**），所以我认为可以考虑添加而不是修改，因为我没有能力甄别这些信息是不是绝对正确。

我有以下尝试性建议，相关讨论可以参见[Issue #35](https://github.com/kgco/RateMySupervisor/issues/35)，您可以进一步参与讨论。

## 操作原则

- 如果您认为某个导师的信息有误，您可以**新建一个信息正确的导师词条**发表评论，您可以非常贴心地在导师信息错误的词条下发表评论指明正确的信息在哪里，或者如果有较多这样的工作，您可以联系我，我来批量完成。
- 如果您认为某个导师的某条评价有误，或者显失公允，您可**以直接补充一条评价指出其他评价的错误**。

## 操作方法

- 如果您对于相关技术比较熟悉，您可以直接在json文件里添加评论并发起pull request（当然我只会接受不包含内容删除的pull request）
- 您也可以直接发布在[Issue #1](https://github.com/kgco/RateMySupervisor/issues/1)中，或如果您认为您的新信息构成独立讨论，可以发布新的Issue

最后，感谢每一位希望对本项目做出贡献的朋友，上述内容不是对您的信息不信任，只是作为以往大量导师评价信息的最后一块保留地，作为repo维护者的我只能谨慎再谨慎，十分抱歉！

# 其他备份
## Docker：
```
docker pull apachecn0/ratemysupervisor
docker run -tid -p <port>:80 apachecn0/ratemysupervisor
# 访问 http://localhost:{port} 查看文档
```

## PYPI：
```
pip install ratemysupervisor
ratemysupervisor <port>
# 访问 http://localhost:{port} 查看文档
```

## NPM：
```
npm install -g ratemysupervisor
ratemysupervisor <port>
# 访问 http://localhost:{port} 查看文档
```

# \*敏感commit列表
以下列出所有对数据文件有直接修改的commit，以备有需要的朋友查阅已经各位关于数据公正性的监督
- 125da269003558d6fe1b84d4b7b7f8c01acc6249 通过爬虫脚本获取的原始数据
- eb53d8b4b88595038537d11241ac424681880217 对json数据做格式化
- c53d2614f98a465148bb3070c9104777116b4b62 去除重复评价
