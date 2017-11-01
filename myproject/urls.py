"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myproject.views import hello_world,home
from publishing.views import publisher_list,publisher_detail,PublisherListView,PublisherDetailView

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^publishers/(?P<pk>\d+)',PublisherDetailView.as_view(),name='publisher_detail'),
	url(r'^publishers',PublisherListView.as_view(),name='publisher_list'),
	#url(r'^publishers/(?P<id>\d+)',publisher_detail,name='publisher_detail'),
	#url(r'^publishers',publisher_list,name='publisher_list'),
	url(r'^hello-world$', hello_world, name='hello_world'),
    url(r'^admin/', admin.site.urls),
]
