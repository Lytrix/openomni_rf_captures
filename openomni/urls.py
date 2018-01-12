"""ibprojecten URL Configuration

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
from django.contrib import admin

# Added to open Files on dev server
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from openomni.api.views import (HomePageView, 
                                   RawCaptureViewSet, 
                                   ActionViewSet, 
                                   UserList,
                                   UserDetail,
                                   capture_list,
                                   )


router = DefaultRouter()
router.register(prefix='raw_captures', viewset=RawCaptureViewSet)
router.register(prefix='actions', viewset=ActionViewSet)

urlpatterns = router.urls

urlpatterns = [
    url(r'^openomni/admin/', admin.site.urls),
    url(r'^openomni/api/', include(router.urls)),
    url(r'^openomni/api/users/$', UserList.as_view()),
    url(r'^openomni/api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^openomni/$', capture_list)
    ]