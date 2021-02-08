from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about, name='about-me'),
    path('plate', views.table_thickness_ground_plate_view.as_view(), name='plate'),
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update_table, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),


]