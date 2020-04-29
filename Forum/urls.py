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
    path('post_message', views.post_message),
    path('profile/<int:id>', views.profile),
    path('edit/<int:id>', views.edit_account),
    path('delete_post/<int:user_id>', views.delete),
    path('update/<int:id>/account', views.update),

    #
]
