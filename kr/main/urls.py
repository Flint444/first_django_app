from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contacts', views.GetUsers.as_view(), name = 'contacts'),
    path('signup', views.SignupView.as_view(), name = 'signup'),
    path('login', views.MyloginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(next_page = 'home'), name = 'logout'),
]
