from django.urls import path
from . import views

urlpatterns = [

    path('register/',views.Register.as_view(), name = 'Register'),
    path('login/',views.Login.as_view(), name = 'Login'),
    path('reset-password/',views.ResetPassword.as_view(),name='ResetPassword')
]