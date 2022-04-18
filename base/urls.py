from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('auth/', views.authenticate_user, name='authenticate-user'),
    path('home/', views.home, name='home'),

    path('write-post/', views.write_post, name='write-post'),
    path('edit-post/<str:pk>/', views.edit_post, name='edit-post'),
    path('view-post/<str:pk>/', views.view_post, name='view-post'),

]
