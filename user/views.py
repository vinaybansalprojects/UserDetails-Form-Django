from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core import mail
from django.core.mail import  send_mail
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from.forms import *
from . models import *

# Create your views here.

def form(request):
	if request.method == 'POST':
		form = SnippetForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			birthday = form.cleaned_data['birthday']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			dateofbirth = birthday.strftime("%m/%d/%Y")
			content = ("Name : "+name+"\n"+"Date of Birth : "+dateofbirth+"\n"+"Email : "+email+"\n"+"Phone No. : "+phone)
			send_mail(
				'Your Details',
				content,
				settings.EMAIL_HOST_USER,
				[email],
				fail_silently=False,
				)

			form.save()

	form = SnippetForm()
	return render(request, 'user/form.html',{'form':form})
def showform(request):
	user = Snippet.objects.all()
	return render(request,'user/showform.html',{'user':user})