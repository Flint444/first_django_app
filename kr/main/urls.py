from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contacts', views.contacts, name = 'contacts'),
    path('signup', views.SignupView.as_view(), name = 'signup'),
    path('login', views.loginView, name = 'login'),
]
