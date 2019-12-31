import datetime

from django.contrib import messages
from django.db.models import Sum, Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.views.generic.base import View
from .models import Reestr


class ReestrInfoView(View):
    """Сводная информация на главной странице"""

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
    """Перечень дорог для просмотра"""
    model = Reestr
    queryset = Reestr.objects.all().filter(work_contract=True)
    template_name = 'main/cotract_list.html'
    paginate_by = 10


class ReestrDetail(DetailView):
    """Информация о контракте"""

    model = Reestr

    def get_queryset(self):
        if self.request.user.is_authenticated:
            @staticmethod
            def get(request):
                info = Reestr.objects.all()
                d_today = datetime.date.today()
                return render(request, 'main/reestr_detail.html', context=info)

            return Reestr.objects.all()
        else:
            return Reestr.objects.none()
