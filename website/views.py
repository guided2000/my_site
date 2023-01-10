from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import contact
from website.forms import NameForm , ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def index_views(request):
    return render(request,'website/index.html')

def portfolio_details_views(request):
    return render(request,'blog/portfolio_details.html')

def contact_view(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent. Thank you! :)')
            return HttpResponseRedirect('/#contact')
        else:
            messages.add_message(request, messages.WARNING, 'Your message was not sent')
            return HttpResponseRedirect('/#contact')
        
    else:
        form = ContactForm()
    return render(request, 'website/index.html',{'form':form})