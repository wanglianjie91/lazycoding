from django import template

register = template.Library()


# 判断是否是当前的category
def active_cat(value, cat_id):
    temp = value.split('/')
    return temp[len(temp)-2] == str(cat_id)


register.filter('active_cat', active_cat)
