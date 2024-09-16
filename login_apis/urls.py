from django.contrib import admin
from django.urls import path,include
from .import views


from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
   path("register",views.register_user,name="register"),
   path("check_token",views.checktoken,name="check_token"),
   path("",TokenRefreshView.as_view(),name="token"),
   path("login",views.login,name="login"),
   path("email",views.send_custom_email,name="login"),
]