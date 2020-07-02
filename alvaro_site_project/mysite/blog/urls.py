from django.urls import path
from . import views



urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('itf/', views.ItfView.as_view(), name='itf'),
    path('new-metcon-area/', views.MetconView.as_view(), name='metcon'),
    path('mybike/', views.MybikeView.as_view(), name='mybike'),
    path('dislexia/', views.DislexiaView.as_view(), name='dislexia'),
]
