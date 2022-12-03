from django.urls import path
from website.views import *

app_name ='website'

urlpatterns = [
    path('',index_views,name='index'),
    path('portfolio',portfolio_details_views,name='portfolio')
]