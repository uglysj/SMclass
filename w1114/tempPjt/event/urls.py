from django.urls import path, include
from . import views

app_name = 'event'
urlpatterns = [
    ### url 주소, views.py 함수명, url 이름
    path('eventView/', views.eventView, name='eventView'),
]