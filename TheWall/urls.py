from django.urls import path
from . import views


# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path('new_user', views.register),
    path('login', views.login2),
    path('user_login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('new_message', views.new_message),
    path('new_comment/<int:id>', views.new_comment),
    path('message/<int:id>/delete', views.delete_message),

]
