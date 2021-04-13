from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about, name='about-me'),
    path('plate', views.table_thickness_ground_plate_view.as_view(), name='plate'),
    path('create', views.create_view.as_view(), name='create'),
    path('update/<int:pk>', views.update_view.as_view(), name='update'),
    path('delete/<int:pk>', views.delete_view.as_view(), name='delete'),
    path('pack-board', views.Pack_board_view.as_view(), name='pack-board'),
    path('create-pack-board', views.Pack_board_create_view.as_view(), name='create-board'),
    path('update-pack-board/<int:pk>', views.Pack_board_update_view.as_view(), name='update-board'),
    path('delete-pack-board/<int:pk>', views.delete_view.as_view(), name='delete-board'),



]