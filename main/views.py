import datetime
import os

from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Sum, Count, Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views.generic.base import View
from django.views.generic.detail import BaseDetailView
from .forms import ContractCreatForm, ContractForm
# пагинация
from django.shortcuts import render, get_object_or_404

from .models import Contracts
from django.http import FileResponse, Http404


class ContractsInfoView(View):
    """ Сводная информация на главной странице """

    # def get(self, request, *args, **kwargs):
    @staticmethod
    def get(request):
        # рабочие контракты без допов
        info = Contracts.objects.all().filter(work_contract=True).exclude(type_doc=3).aggregate(Count('id', distinct=True), Sum('c_contract'))
        qs = Contracts.objects.all().filter(work_contract=True, type_doc=1)
        d_today = datetime.date.today()
        summ_ost = 0
        for rw in qs:
            summ_ost += rw.c_contract
        info['ogk__sum'] = summ_ost
        info['date__today'] = d_today
        return render(request, 'index.html', context=info)


class ContractsListView(ListView):
    """ Перечень контрактов для просмотра """
    model = Contracts
    # рабочие контракты без КС
    queryset = Contracts.objects.all().filter(work_contract=True).exclude(type_doc=3)

    template_name = 'main/contract_list.html'
    paginate_by = 5


# class DopSListView(ListView):
#     """ Перечень допов для просмотра """
#     model = Contracts
#     # рабочие допы
#     queryset = Contracts.objects.all().filter(work_contract=True, type_doc=2)
#     template_name = 'main/dop_list.html'
#     paginate_by = 5


class ContractDetail(DetailView):
    """ Информация о контракте """
    model = Contracts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d_today = datetime.date.today()
        context['d_today'] = d_today
        # period = kwargs['object'].period
        # broad = kwargs['object'].broad
        # oroad = kwargs['object'].oroad
        # am_month = ammort(period, broad)
        # summ_ost = oroad - am_month * d_today.month
        context['summ_ost'] = 666
        objkey = self.kwargs.get('pk', None)
        c_num = Contracts.objects.filter(work_contract=True, id=objkey).exclude(type_doc=3)
        # context['dops'] = Contracts.objects.filter(work_contract=True, type_doc=2, num_contract=c_num)
        # if self.request.user.is_authenticated:
        #     return context
        # else:
        #     return Contracts.objects.none()
        return context


class DisplayPdfView(BaseDetailView):
    """ Вывод на экран скана контракта в формате PDF"""
    def get(self, request, *args, **kwargs):
        objkey = self.kwargs.get('pk', None)  # обращение к именованному аргументу pk, переданному по URL-адресу
        pdf = get_object_or_404(Contracts, id=objkey)  # Эта строка получает фактический объект модели pdf
        # if pdf.type_doc_id == 1:
        # file_name = pdf.y_contract + '\\' + pdf.num_contract + '.pdf'  # Папка год + имя файла + расширение
        file_name = pdf.y_contract + '\\' + str(pdf.file_obj)  # Папка год + имя файла
        # else:
        #     file_name = pdf.y_contract + '\\' + pdf.num_contract + '.' + pdf.name_object + '.pdf'
            # Папка год + имя файла + расширение
        path = os.path.join(settings.MEDIA_ROOT, file_name)  # полный путь к файлу
        response = FileResponse(open(path, 'rb'), content_type="application/pdf")
        response["Content-Disposition"] = "filename={}".format(file_name)
        return response


# class ContractDopListView(ListView):
#     """ Перечень дополнительных соглашений к контрактам """
#     model = Contracts
#
#     queryset = Contracts.objects.all().filter(work_contract=True, type_doc=2)
#     template_name = 'main/contract_dop_list.html'
#     paginate_by = 10


# class DopDetail(DetailView):
#     """ Информация о допе """
#     model = Contracts
#     template_name = 'main/dop_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         objkey = self.kwargs.get('pk', None)
#         c_num = Contracts.objects.filter(work_contract=True, type_doc=2, id=objkey)
#         context['num_gk'] = c_num[:5]
#         d_today = datetime.date.today()
#         context['d_today'] = d_today
#         return context


class SearchResultsView(ListView):
    model = Contracts

    def get_queryset(self):
        query = self.request.GET.get('q')
        # if query:
        # Если q в GET запросе
        object_list = Contracts.objects.filter(
            Q(num_contract__icontains=query) | Q(name_object__icontains=query) | Q(uch_contract__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    template_name = 'main/search_results.html'
    paginate_by = 5


class ContractUpdateView(UpdateView):
    """Внесение изменений"""
    model = Contracts
    form_class = ContractForm
    success_url = reverse_lazy('contract-list')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Contracts.objects.all()
        else:
            return Contracts.objects.none()

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '{}'.format(form.instance))
        return result


class ContractCreateView(CreateView):
    """Заполнение аттрибутов контракта"""
    model = Contracts
    form_class = ContractCreatForm
    success_url = reverse_lazy('contract-list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '{}'.format(form.instance))
        return result

