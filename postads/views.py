from django.shortcuts import render
import time
from django.contrib.auth.models import User
from .models import PostAd
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse
from django.views.generic import FormView
from .models import PostAd
from .forms import PostAdForm

class PostAdPage(FormView):
	template_name = 'post_ad.html'
	success_url = 'awesome'
	form_class = PostAdForm

	def form_valid(self,form):
		form.save()
		return HttpResponseRedirect('/successful')

def successful(request):
	render(request,'successful.html')
	time.sleep(30)
	return HttpResponseRedirect('/user/{ user.name }')
def users(request,name):
	 user = PostAd.objects.get(name=name)
	 conext = {'user':user,}
	 return render (request,'user.html',conext)
