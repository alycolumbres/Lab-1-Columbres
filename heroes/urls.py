"""willowisp URL Configuration

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

from .views import Heroes
from .views import Cloud
from .views import Sunflowey
from .views import Jester

urlpatterns = [
    url(r'^/heroes$', Heroes.as_view(), name='Heroes'),
    url(r'^/hero/cloud$', Cloud.as_view(), name='Cloud'),
    url(r'^/hero/sunflowey$', Sunflowey.as_view(), name='Sunflowey'),
    url(r'^/hero/jester$', Jester.as_view(), name='Jester'),
]
