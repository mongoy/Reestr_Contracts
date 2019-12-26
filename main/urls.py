from django.urls import path
from .views import RoadInfoView, RoadListView

urlpatterns = [
    path('', RoadInfoView.as_view(), name='index'),
    path('list/', RoadListView.as_view(), name='contract-list'),
]

