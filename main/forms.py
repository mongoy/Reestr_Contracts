from django import forms
from .models import Reestr


class ContractForm(forms.ModelForm):
    """Форма"""
    class Meta:
        model = Reestr
        #fields = ['nregion', 'iroad', 'troad', 'innroad', 'inroad','proad']
        fields = '__all__' #все поля
        # exclude = ['n'] #должны быть исключены из формы
        # help_texts = {
        #     'nregion': (' - Название района.'),
        #     'lroad': (' км'),
        # }


class ContractCreatForm(forms.ModelForm):
    """Форма"""

    class Meta:
        model = Reestr
        # fields = ['nregion', 'iroad', 'troad', 'innroad', 'inroad','proad']
        fields = '__all__'  # все поля
        # fields = ['file_obj']
