"""music_controller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#where the main url is sent 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')), # whatever url is sent here resolve it in api.urls
    path('',include('frontend.urls')) # whenever we type a url that isnt api or admin we send it to frontend.urls
]

'domain.com/hello' # after the / is sent to this, and is 
'domain.com/admin/....', #whatever is after /admin/ is sent to admin.site.urls to handle
