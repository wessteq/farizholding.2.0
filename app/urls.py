from django.urls import path
from .import views

urlpatterns = [
    path('index_view/', views.index_view, name='index_view'),
    path('register/',views.user_register , name='user_register'),
    path('login/',views.user_login_view,name='login'),
    path('logout/',views.user_logout_view,name='logout')
]