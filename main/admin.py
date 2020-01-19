from django.contrib import admin
from .models import *


@admin.register(Reestr)
class ReestrAdmin(admin.ModelAdmin):
    """Перечень дорог"""
    list_display = [field.name for field in Reestr._meta.fields]  # все поля выводит в цикле
    search_fields = ["num_contract"]
    list_filter = ["num_contract", "y_contract"]
    list_per_page = 5  # кол-во записей на странице

@admin.register(TypeDoc)
class TypeDocAdmin(admin.ModelAdmin):
    """ Тип документа: госконтракт или допсоглашение """
    list_display = ("id", "name",)


@admin.register(Initiator)
class InitiatorAdmin(admin.ModelAdmin):
    """ Инициаторы закупки"""
    list_display = ("id", "name")
    list_per_page = 10

@admin.register(Status_Contract)
class Status_ContractAdmin(admin.ModelAdmin):
    """ Статус контракта """
    list_display = ("id", "name")
