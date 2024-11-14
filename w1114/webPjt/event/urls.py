from django.urls import path, include
from . import views

#### 메인 URL ####
app_name = 'eventView'
urlpatterns = [
    path('eventView/', views.eventView, name='eventView'),
]
