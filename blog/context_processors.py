from django.contrib.sites.models import Site # sites框架，用于管理多个站点

from blog.models import Category, Article

from blog.models import Setting

def get_setting():
    """ 模板全局变量各种值的设置"""
    if Setting.objects.count():    # 数据库中有值就返回第一个值，否则按照以下的默认值
        return Setting.objects.first()
    else:
        # 但站点内没有配置实例时候, 会默认创建一个
        s = Setting()
        s.name = 'Personal Blog'
        s.desc = 'django个人博客网站'
        s.keyword = 'python3, django2'
        s.article_desc_len = 250          # 文章描述的长度
        s.sidebar_article_count = 5       # 侧边栏最热文章的数量
        s.enable_multi_user = True        # 设置多用户后台，允许有is_staff权限的用户登录后台
        s.github_user = 'engoy-binbin'
        s.github_repository = 'Django-blog'

        s.save()  # 保存到数据库
        return s  # 返回这个模型对象

def context_setting(requests):
    """ 自定义一些模板全局变量，返回一个字典 """
    s = get_setting()
    site = Site.objects.first()
    return {
        'SITE_NAME': s.name,  # 站点名称
        'SITE_DESC': s.desc,  # 站点描述
        'SITE_KEYWORD': s.keyword,  # 站点关键字
        'SITE_URL': site.domain,  # 域名：example.com
        'ENABLE_PHOTO': s.enable_photo,  # 是否启动相册，默认是True
        'nav_pages': Article.objects.filter(type='p'),  # 所有需要导航的文章页面
        'nav_category_list': Category.objects.all(),  # 导航栏-> 所有分类，nav.html模板里调用

        'top_categorys': Category.top_objects.all()  # 对manager的应用，所有的一级分类
    }
