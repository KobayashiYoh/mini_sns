from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
    path('other/<int:user_id>/', views.profile_view, name='profile'),
    path('post/<uuid:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<uuid:pk>/delete/', views.post_delete, name='post_delete'),
]