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
    """
        Сводная информация на главной странице
    """

    # def get(self, request, *args, **kwargs):
    @staticmethod
    def get(request):
        info = Reestr.objects.all().filter(work_contract=True).aggregate(Count('id', distinct=True), Sum('c_contract'))
        qs = Reestr.objects.all().filter(work_contract=True)
        d_today = datetime.date.today()
        summ_ost = 0
        for rw in qs:
            summ_ost += rw.c_contract
        info['oroad__sum'] = summ_ost
        info['date__today'] = d_today
        return render(request, 'index.html', context=info)


class ReestrListView(ListView):
    """
        Перечень дорог для просмотра
    """
    model = Reestr
    queryset = Reestr.objects.all().filter(work_contract=True)
    template_name = 'main/cotract_list.html'
    paginate_by = 10


class ReestrDetail(DetailView):
    """
        Информация о контракте
    """
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
        # context['elements'] = ElRoad.objects.filter(nroad=Road).filter(nregion=Road)
        # if self.request.user.is_authenticated:
        #     return context
        # else:
        #     return Reestr.objects.none()
        return context


class DisplayPDFView(View):
    """
        Вывод PDF файла сонтракта на экран
    """

    def get_context_data(self, **kwargs):  # Exec 1st
        context = {}
        # context logic here
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        base_path = os.path.join(os.path.join(settings.BASE_DIR, "files"), '2019')
        # base_path = os.path.join(os.path.join(os.path.dirname(settings.BASE_DIR), "files"), '2019')
        path = os.path.join(base_path, '2019.1.pdf')

        with open(path, 'rb') as pdf_f:
            response = HttpResponse(pdf_f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'filename="2019.1.pdf"'
        pdf_f.closed

        return response



