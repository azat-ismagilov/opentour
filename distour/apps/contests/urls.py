from django.urls import include
from django.urls import path

from . import views

app_name='contests'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contest_id>/', views.detail, name='detail'),
    path('<int:contest_id>/start', views.start_vc, name='start_vc'),
    path('results/<int:contest_id>/', views.results, name='results'),
]
