from django.urls import path
from .views import ReestrInfoView, ReestrListView, ReestrDetail, pdf, DisplayPDFView

urlpatterns = [
    path('', ReestrInfoView.as_view(), name='index'),
    path('list/', ReestrListView.as_view(), name='contract-list'),
    path('pdf/<int:pk>', DisplayPDFView.as_view(), name='pdf-view'),
    path('detail/<int:pk>', ReestrDetail.as_view(), name='contract-detail'),
]

