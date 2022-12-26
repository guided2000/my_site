from django.urls import path
from blog.views import *

app_name ='blog'

urlpatterns = [
    path('',blog_views,name='index'),
    # path('single' ,blog_single,name='single'),
    path('<int:pid>' ,blog_single,name='single'),
    path('category/<str:cat_name>',blog_views,name='category'),
    path('author/<str:author_username>',blog_views,name='author'),
    path('search/',blog_search,name='search')
]