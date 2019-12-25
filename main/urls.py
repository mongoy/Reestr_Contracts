from django.urls import path
from .views import RoadInfoView

urlpatterns = [
    path('', RoadInfoView.as_view(), name='index'),
]