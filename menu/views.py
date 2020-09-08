from django.shortcuts import render
from django.http import HttpResponse 
from .models import Menu, MenuElement


def test(request, **kwargs):

	url = ''
	for couple in kwargs.items():
		url += couple[1] + '/'

	context = {
		'url': url,
		'data': kwargs  # You could set any data from backend here
	}


	if request.is_ajax():
		return render(request, 'ajax_data.html', {'context': context})
	else:
		return render(request, 'test.html', {'context': context})

