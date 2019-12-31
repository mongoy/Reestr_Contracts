from django.urls import path
from .views import ReestrInfoView, ReestrListView, ReestrDetail

urlpatterns = [
    path('', ReestrInfoView.as_view(), name='index'),
    path('list/', ReestrListView.as_view(), name='contract-list'),
    path('detail/<int:pk>', ReestrDetail.as_view(), name='contract-detail'),
]

