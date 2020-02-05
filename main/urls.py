from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ContractsInfoView, ContractsListView, ContractDetail, DisplayPdfView, \
    SearchResultsView, ContractUpdateView, ContractCreateView

urlpatterns = [
    path('', ContractsInfoView.as_view(), name='index'),
    path('list/', ContractsListView.as_view(), name='contract-list'),
    path('list/pdf/<int:pk>/', DisplayPdfView.as_view(), name='con-pdf-view'),
    path('list/detail/<int:pk>/', ContractDetail.as_view(), name='contract-detail'),
    # path('dop/', ContractDopListView.as_view(), name='contract-dop-list'),
    # path('dops/', DopSListView.as_view(), name='dop-list'),
    # path('dops/pdf/<int:pk>/', DisplayPdfView.as_view(), name='dop-pdf-view'),
    # path('dops/detail/<int:pk>/', DopDetail.as_view(), name='dop-detail'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('update/<int:pk>', ContractUpdateView.as_view(), name='contract-update'),
    path('create/', ContractCreateView.as_view(), name='contract-create'),
]
# только в режиме DEBUG для Upload
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
