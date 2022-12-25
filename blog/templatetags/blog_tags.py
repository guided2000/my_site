from django import template
from blog.models import post ,category


register = template.Library()

@register.inclusion_tag('blog/widget3.html')
def latest_posts(arg=3):
    posts= post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}



@register.inclusion_tag('blog/widget1.html')
def post_categories():
    posts =post.objects.filter(status=1)
    categories =category.objects.all()
    cat_dict ={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}