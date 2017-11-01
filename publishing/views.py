# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView

from django.shortcuts import render
from .models import Publisher

# Create your views here.
def publisher_list(request):
	publisher_list = Publisher.objects.all()
	return render(request, 'publishing/publisher_list.html', {
		'publisher_list': publisher_list
		})

def publisher_detail(request,id):
	publisher = Publisher.objects.get(pk=id)
	return render(request, 'publishing/publisher_detail.html',{
			'publisher': publisher
		})

class PublisherListView(ListView):
	"""docstring for PublisherListView"""
	model = Publisher

class PublisherDetailView(DetailView):
	"""docstring for PublisherDetailView"""
	model = Publisher

	def get_context_data(self,**kwargs):
		context = super(PublisherDetailView, self).get_context_data(**kwargs)
		context['massage'] = 'Sebuah Pesan Dari luar angkasa'
		return context
		
		
