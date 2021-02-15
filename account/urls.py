from . import views
from django.urls import path, include

urlpatterns = [

    path('main/', include('main.urls')),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page')


]