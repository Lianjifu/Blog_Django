from ..models import Post,Category
from django import template


# 注册这个函数为模板标签
register = template.Library()


# 最新文章模板标签
# 获取数据库中前num篇文字，这里num默认为5
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month',order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()