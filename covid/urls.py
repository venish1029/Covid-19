from django.urls import path
from . import views 
urlpatterns=[
    path('',views.index),
    path('state/<str:state_name>/',views.state)
]