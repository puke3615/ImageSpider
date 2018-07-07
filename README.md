# ImageSpider
*百度图片爬虫*

* 配置`ImageSpider/spiders/BaiduImageSpider.py`文件
  * 更改`IMAGES_STORE`配置为图片存储路径
  * 更改`KEYWORDS`为搜索关键词
  * `python setup.py`直接运行即可



以`古风`为关键词，爬的效果如下

![](images/spider.png)



还有`json`、`text`、`markdown`形式的导出，如下

**json**

```json
{
  "fromPageTitle": "<strong>古风</strong>美男 中国风 手绘",
  "thumbURL": "http://img0.imgtn.bdimg.com/it/u=318340784,2667811132&fm=27&gp=0.jpg",
  "objURL": "http://img5q.duitang.com/uploads/item/201506/08/20150608192332_XLm5C.jpeg"
},
{
  "fromPageTitle": "充满<strong>古风</strong>意蕴的散散之笔, 细致入微的人物刻画 带你走进一个全新古典",
  "thumbURL": "http://img5.imgtn.bdimg.com/it/u=2673515744,2774212201&fm=27&gp=0.jpg",
  "objURL": "http://img1.3lian.com/2015/a1/54/d/52.jpg"
},
{
  "fromPageTitle": "<strong>古风</strong>",
  "thumbURL": "http://img3.imgtn.bdimg.com/it/u=527217728,2884200961&fm=27&gp=0.jpg",
  "objURL": "http://img5.duitang.com/uploads/blog/201405/24/20140524150831_kTJEA.thumb.700_0.jpeg"
}
```

**text**

```text
fromPageTitle : <strong>古风</strong>
thumbURL      : http://img5.imgtn.bdimg.com/it/u=1822799899,152357902&fm=27&gp=0.jpg
objURL        : http://cdn.duitang.com/uploads/item/201601/03/20160103203235_yfwtL.thumb.700_0.jpeg

fromPageTitle : 求<strong>古风</strong>的动漫图
thumbURL      : http://img5.imgtn.bdimg.com/it/u=363594260,3917306499&fm=27&gp=0.jpg
objURL        : http://c.hiphotos.baidu.com/zhidao/pic/item/9d82d158ccbf6c81921e8b90ba3eb13533fa4098.jpg

fromPageTitle : <strong>古风</strong>头像 醉生梦死烟花烫
thumbURL      : http://img5.imgtn.bdimg.com/it/u=356411596,2828866357&fm=27&gp=0.jpg
objURL        : http://img4.duitang.com/uploads/item/201509/17/20150917121843_hQjJU.jpeg
```

**markdown**

```markdown
[<strong>古风</strong>美男 中国风 手绘](http://img5q.duitang.com/uploads/item/201506/08/20150608192332_XLm5C.jpeg)
![](http://img0.imgtn.bdimg.com/it/u=318340784,2667811132&fm=27&gp=0.jpg)

[充满<strong>古风</strong>意蕴的散散之笔, 细致入微的人物刻画 带你走进一个全新古典](http://img1.3lian.com/2015/a1/54/d/52.jpg)
![](http://img5.imgtn.bdimg.com/it/u=2673515744,2774212201&fm=27&gp=0.jpg)

[<strong>古风</strong>](http://img5.duitang.com/uploads/blog/201405/24/20140524150831_kTJEA.thumb.700_0.jpeg)
![](http://img3.imgtn.bdimg.com/it/u=527217728,2884200961&fm=27&gp=0.jpg)
```

