import datetime
import os

from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Sum, Count
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.views.generic.base import View
from django.views.generic.detail import BaseDetailView

from .models import Reestr
from django.http import FileResponse, Http404


class ReestrInfoView(View):
    """ Сводная информация на главной странице """

    # def get(self, request, *args, **kwargs):
    @staticmethod
    def get(request):
        # рабочие контракты без допов
        info = Reestr.objects.all().filter(work_contract=True, type_doc=1).aggregate(Count('id', distinct=True), Sum('c_contract'))
        qs = Reestr.objects.all().filter(work_contract=True, type_doc=1)
        d_today = datetime.date.today()
        summ_ost = 0
        for rw in qs:
            summ_ost += rw.c_contract
        info['oroad__sum'] = summ_ost
        info['date__today'] = d_today
        return render(request, 'index.html', context=info)


class ReestrListView(ListView):
    """ Перечень дорог для просмотра """
    model = Reestr
    # рабочие контракты без допов
    queryset = Reestr.objects.all().filter(work_contract=True, type_doc=1)
    template_name = 'main/cotract_list.html'
    paginate_by = 10


class ReestrDetail(DetailView):
    """ Информация о контракте """
    model = Reestr

    # template_name = 'main/contract_detail.html'

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
        c_num = Reestr.objects.filter(work_contract=True, type_doc=1, id=objkey)
        context['dops'] = Reestr.objects.filter(work_contract=True, type_doc=2, num_contract=c_num)
        # if self.request.user.is_authenticated:
        #     return context
        # else:
        #     return Reestr.objects.none()
        return context


class DisplayPdfView(BaseDetailView):
    """ Вывод на экран скана контракта в формате PDF"""
    def get(self, request, *args, **kwargs):
        objkey = self.kwargs.get('pk', None)  # обращение к именованному аргументу pk, переданному по URL-адресу, вызывающему представление
        pdf = get_object_or_404(Reestr, id=objkey)  # Эта строка получает фактический объект модели pdf
        fname = pdf.y_contract + '\\' + pdf.num_contract + '.pdf'  # Папка год + имя файла + расширение
        path = os.path.join(settings.MEDIA_ROOT, fname)  # полный путь к файлу
        response = FileResponse(open(path, 'rb'), content_type="application/pdf")
        response["Content-Disposition"] = "filename={}".format(fname)
        return response


class ContractDopListView(ListView):
    """ Перечень дополнительных соглашений к контрактам """
    model = Reestr

    queryset = Reestr.objects.all().filter(work_contract=True, type_doc=2)
    template_name = 'main/contract_dop_list.html'


