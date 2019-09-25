from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'index/', views.check, name="loginProc"),
    url(r'navAdmin/', views.getNavigationAdmin, name="navAdmin"),
    url(r'logout', views.logout, name="logout"),
     url(r'calendar/', include('calender.urls'))
]