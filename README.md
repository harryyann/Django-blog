
### Dajngo开发的个人博客系统
* 该博客系统参考于github上的开源项目engoy-binbin/Django-blog，做了一些修改，增加了一些功能

## 主要功能

* 使用了Django原生的admin和Xadmin两种后台管理，增加筛选器等等后台管理功能，用户可在后台编辑文章
* 增加伪多用户博客系统，每个用户只可以对自己文章的增删改查操作
* 文章编辑支持 `Markdown ` ， 文章详情支持`Markdown`，代码高亮
* 支持文章列表分页（写入缓存），文章评论留言
* 右侧侧边栏功能，最热文章，最新文章，标签云
* 文章根据添加时间进行归档
* 使用Django REST framework开发API
* 使用logging记录错误日志，
* 使用celery+redis支持一些异步任务的调度
* 相册功能，有两种样式，不喜欢的可以在admin设置里关闭，或者选其一，在base/nav.html里修改
* 支持RSS订阅，可以同过聚合阅读工具访问博客的更新

## 技术栈

* Django REST framework和  REST framework-jwt进行API开发
* 使用到django通用类视图，ListViewDetailView，FromView，RedirectView
* admin的扩展，ModelAdmin扩展，SimpleListFilter自定义过滤器
* 使用Xadmin创建更优美的后台管理系统
* 自定义LoginView，RegisterView，LogoutView，部分django自带auth用法
* context_processors自定义模板全局变量
* 文章内容和侧边栏内容使用 `mdeditor`支持`markdown`和`图片上传`
* templatetags 自定义模板标签 tags，支持markdown，代码高亮
* 使用haystack和whoosh实现的全文文章搜索功能，增加了jieba并修改whoosh_backends进行中文分词
* 使用django-compress压缩css/js
* django新版中间件的编写，显示页面加载时间
* 使用django自带的sitemap功能，生成站点地图
* python-memcached对部分视图进行缓存
* 自定义django.manage命令,create_fake_data，生成测试数据，clear_migrations清理迁移文件
* django中使用logging模块日志管理、message模块消息闪现
* 使用celery+redis进行异步任务调度

## 安装

1. 安装依赖（最好新建个虚拟环境）
   * pip install -Ur requirements -i https://pypi.douban.com/simple
   * pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
2. 设置数据库
  * 修改settings中的数据库配置
  * 创建本地数据库 

  * 在终端下进行数据迁移:

       ```
           ./manage.py makemigrations
           ./manage.py migrate
       ```

  * 创建测试数据 `./manage.py create_fake_data`

  * 运行 `./manage.py runserver 8000`

  * 浏览器打开 `127.0.0.1:8000`查看网站，打开`127.0.0.1:8000/admin`或者`127.0.0.1:8000/xadmin`进入后台管理
3. 配置项（更多设置看settings和blog.model.Setting模型）
