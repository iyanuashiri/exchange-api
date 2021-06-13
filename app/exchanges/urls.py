from django.urls import path

from . import views


app_name = 'exchanges'
urlpatterns = [
    path('quotes/', views.ExchangeListCreateView.as_view(), name='exchange-list-create'),

]
