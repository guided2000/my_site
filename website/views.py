from django.shortcuts import render
# Create your views here.
def index_views(request):
    return render(request,'website/index.html')

def portfolio_details_views(request):
    return render(request,'blog/portfolio_details.html')