from django.shortcuts import render,get_object_or_404
from blog.models import post
# Create your views here.
def blog_views(request,**kwargs):
    posts = post.objects.filter(status=1)
    if kwargs.get  ('cat_name')!=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get  ('author_username')!=None:
       posts=posts.filter(author__username=kwargs['author_username']) 
    context={'posts':posts}
    return render(request,'blog/portfolio_details.html',context)



def blog_single(request,pid=6):
    posts = get_object_or_404(post,pk=pid)
    context={'posts':posts}
    return render(request,'blog/single.html',context)