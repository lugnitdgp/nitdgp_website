"""backend URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from base.views import APIRoot, archives
from root import settings

admin.site.site_header = 'NIT Durgapur Administration'
admin.site.site_title = 'NIT Durgapur'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('dashboard.urls')),
    url(r'^', include('department.urls')),
    url(r'^', include('administration.urls')),
    url(r'^', include('academics.urls')),
    url(r'^', include('facilities.urls')),
    url(r'^', include('information.urls')),
    url(r'^', include('activities.urls')),
    url(r'^', include('faculty.urls')),
    url(r'^$', APIRoot.as_view(), name='root-view'),
    url(r'^archives/$', archives, name='archives')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
