from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about, name='about-me'),
    path('plate', views.table_thickness_ground_plate_view.as_view(), name='plate'),
    path('create', views.create_view.as_view(), name='create'),
    path('update/<int:pk>', views.update_view.as_view(), name='update'),
    path('delete/<int:pk>', views.delete_view.as_view(), name='delete'),


]