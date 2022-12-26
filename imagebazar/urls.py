from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

from django.views.static import serve
from django.template.defaulttags import url
# from django.conf.urls import url

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('aboutus/', show_about_page),
                  path('home/', show_home_page),
                  path('', show_home_page),
                  path('category/<int:cid>', show_category_page),

                  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
