from django.http  import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'publishing/index.html', {
		'site_name': 'Publishing',
		'title':'Apa kabar Dunia',
		'content':'Belajar Django'
				  'Malu sama Cewek'
		})

def hello_world(request):
	return HttpResponse('Hello, World!')