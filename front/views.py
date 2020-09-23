import markdown
from functools import reduce
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_GET, require_http_methods
from django.core.paginator import Paginator
from .models import Article, Tag, Category


# 获取基础信息
def _getBaseData(request):
    tags = Tag.objects.all()
    categorys = Category.objects.all()
    recent_articles = Article.objects.all().order_by('update_time')[0:5]
    archives = Article.objects.dates('create_time', 'month')
    temp_archives = []
    for i in archives:
        temp_archives.append({
            'date': i,
            'count': Article.objects.filter(create_time__year=i.year, create_time__month=i.month).count()
        })
    return {
        'tags': tags,
        'categorys': categorys,
        'recent_articles': recent_articles,
        'archives': temp_archives
    }


# 公共分页方法
def _pagination(request, querySet):
    paginator = Paginator(querySet, 10)  # Show 10  contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


# 标题，关键字，描述
def _gethead(*args):
    return {
        'title': args[0],
        'keywords': args[1],
        'description': args[2]
    }


# Create your views here.
@require_GET
def index(request):
    base_data = _getBaseData(request)
    article_lists = Article.objects.all().order_by('update_time')[0:10]
    return render(request, 'index.html', {
        **_gethead('lazycoding_王连杰的博客', 'python, javascript, 前端', '王连杰的博客-记录前端开发每一天'),
        **base_data,
        "article_lists": article_lists
    })


@require_GET
def category(request, pk):
    base_data = _getBaseData(request)
    articles = Article.objects.filter(category=pk).order_by('update_time')
    curr_category = Category.objects.get(pk=pk)
    page_obj = _pagination(request, articles)
    return render(request, 'category.html', {
        **_gethead(curr_category.name, curr_category.keywords, curr_category.description),
        **base_data,
        "page_obj": page_obj,
    })


@require_GET
def article(request, pk):
    base_data = _getBaseData(request)
    content = Article.objects.get(pk=pk)
    content.content = markdown.markdown(content.content,
                                        extensions=['markdown.extensions.toc', 'markdown.extensions.fenced_code'])
    return render(request, 'article.html', {
        **_gethead(content.title, reduce(lambda x, y: x.name + ',' + y.name, content.tags.all()), content.description),
        **base_data,
        "article": content
    })


@require_GET
def tag(request, pk):
    base_data = _getBaseData(request)
    current_tag = get_object_or_404(Tag, pk=pk)
    articles = current_tag.article_set.all().order_by('update_time')
    page_obj = _pagination(request, articles)
    return render(request, 'tag.html', {
        **_gethead(current_tag.name, current_tag.keywords, current_tag.description),
        **base_data,
        'page_obj': page_obj
    })


@require_GET
def archive_month(request, year, month):
    base_data = _getBaseData(request)
    articles = get_list_or_404(Article, create_time__year=year, create_time__month=month)
    page_obj = _pagination(request, articles)
    return render(request, 'archive.html', {
        **_gethead('{0}年{1}月文章归档'.format(year, month), '文章归档,', '文章归档整理'),
        **base_data,
        'page_obj': page_obj
    })


@require_GET
def archive_year(request, year):
    base_data = _getBaseData(request)
    articles = get_list_or_404(Article, create_time__year=year)
    page_obj = _pagination(request, articles)
    return render(request, 'archive.html', {
        **_gethead('{0}年文章归档'.format(year), '文章归档,', '文章归档整理'),
        **base_data,
        'page_obj': page_obj
    })


@require_GET
def search(request):
    base_data = _getBaseData(request)
    keywords = ''
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
    articles = get_list_or_404(Article, content__contains=keywords)
    page_obj = _pagination(request, articles)
    return render(request, 'search.html', {
        **_gethead('{0}的搜索结果'.format(keywords), '搜索页面,搜索结果', '{0}的搜索结果'.format(keywords)),
        **base_data,
        'page_obj': page_obj
    })
