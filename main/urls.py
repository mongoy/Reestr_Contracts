from django.urls import path
from .views import ContractsInfoView, ContractsListView, ContractDetail, DisplayPdfView, ContractDopListView, DopSListView

urlpatterns = [
    path('', ContractsInfoView.as_view(), name='index'),
    path('list/', ContractsListView.as_view(), name='contract-list'),
    path('pdf/<int:pk>/', DisplayPdfView.as_view(), name='pdf-view'),
    path('detail/<int:pk>/', ContractDetail.as_view(), name='contract-detail'),
    path('dop/', ContractDopListView.as_view(), name='contract-dop-list'),
    path('dops/', DopSListView.as_view(), name='dop-list'),
]

