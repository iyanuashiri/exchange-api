from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('auth/users/', views.AccountCreateView.as_view(), name='auth-create'),

    path('auth/token/login/', views.TokenCreateView.as_view(), name='auth-login'),
]
