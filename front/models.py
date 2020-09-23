from django.db import models


class Tag(models.Model):
    name = models.CharField('名称', max_length=50)
    keywords = models.CharField('关键字', max_length=50, default='lazycoding')
    description = models.CharField('描述', max_length=200, default='lazycoding')
    url = models.SlugField('url', unique=True)
    important = models.BooleanField('重要', default=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '标签'


class Category(models.Model):
    name = models.CharField('名称', max_length=50)
    keywords = models.CharField('关键字', max_length=50, default='lazycoding')
    description = models.CharField('描述', max_length=200, default='lazycoding')
    url = models.SlugField('url', unique=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '分类'


class Article(models.Model):
    title = models.CharField('标题', max_length=30)
    description = models.TextField('摘要')
    content = models.TextField('内容')
    tags = models.ManyToManyField('Tag', verbose_name='标签集')
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='分类')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = '文章'
