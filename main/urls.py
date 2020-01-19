from django.urls import path
from .views import ContractsInfoView, ContractsListView, ContractDetail, DisplayPdfView, ContractDopListView\
    , DopSListView, DopDetail

urlpatterns = [
    path('', ContractsInfoView.as_view(), name='index'),
    path('list/', ContractsListView.as_view(), name='contract-list'),
    path('list/pdf/<int:pk>/', DisplayPdfView.as_view(), name='con-pdf-view'),
    path('list/detail/<int:pk>/', ContractDetail.as_view(), name='contract-detail'),
    # path('dop/', ContractDopListView.as_view(), name='contract-dop-list'),
    path('dops/', DopSListView.as_view(), name='dop-list'),
    path('dops/pdf/<int:pk>/', DisplayPdfView.as_view(), name='dop-pdf-view'),
    path('dops/detail/<int:pk>/', DopDetail.as_view(), name='dop-detail'),
]

