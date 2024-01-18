from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'youtubepages'

urlpatterns = [
    path('', views.signin, name='signin'),
    path('homepage/', views.homepage, name='homepage'),
    path('createvideo/', views.createvideo, name='createvideo'),
    path('createaccount/',views.createaccount, name="createaccount"),
    path('searchdisplay/',views.searchdisplay, name="searchdisplay"),
    # path('search/',views.Searchh,name="search")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)