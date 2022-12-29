from django.shortcuts import render,get_object_or_404
from blog.models import post 
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import NewsletterForm
# Create your views here.
def blog_views(request,**kwargs):
    posts = post.objects.filter(status=1)
    if kwargs.get  ('cat_name')!=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get  ('author_username')!=None:
       posts=posts.filter(author__username=kwargs['author_username']) 

    posts=Paginator(posts,3)

    try:
        page_number = request.GET.get('page')
        posts =posts.get_page(page_number)
    except PageNotAnInteger :
        posts =posts.get_page(1)
    except EmptyPage:
        posts =posts.get_page(1)
    context={'posts':posts}
    return render(request,'blog/portfolio_details.html',context)



def blog_single(request,pid=6):
    posts = get_object_or_404(post,pk=pid)
    context={'posts':posts}
    return render(request,'blog/single.html',context)


def blog_search(request):
    posts = post.objects.filter(status=1)
    if request.method == 'GET' :
        posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts':posts}
    return render(request,'blog/portfolio_details.html',context)

def newsletter_view (request):
    if request.method == 'POST':
        form =NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blog')
    else:
        return HttpResponseRedirect('/blog')