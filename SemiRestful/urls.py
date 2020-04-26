from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path('shows', views.all_shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create_new_show),
    path('shows/<int:id>', views.show_page),
    path('shows/<int:id>/edit', views.edit_page),
    path('shows/<int:id>/update', views.update_page),
    path('shows/<int:id>/delete', views.delete_page),

]
