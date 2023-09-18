from django.urls import path, include
from host_authentication_system import views


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.user_login, name="login"),
    path('wait/', views.waitpage, name="waitpage"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.host_logout, name="logout"),
    path('changepassword/', views.change_password, name="changepassword"),
]