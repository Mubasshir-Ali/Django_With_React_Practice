"""
URL configuration for IIIMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from iiimsApp import views
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('iiims/', admin.site.urls),
    path('',include('iiimsApp.urls')),
    path('api/user/get-token/', obtain_auth_token),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

admin.site.index_title = 'IIIMS'
admin.site.site_header = 'IIIMS Admin'
admin.site.site_title = 'IIIMS Education System'
