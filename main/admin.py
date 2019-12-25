from django.contrib import admin
from .models import *


@admin.register(Reestr)
class RoadAdmin(admin.ModelAdmin):
    """Перечень дорог"""
    list_display = [field.name for field in Reestr._meta.fields]  # все поля выводит в цикле
    search_fields = ["num_contract"]
    list_filter = ["num_contract", "y_contract"]


@admin.register(TypeDoc)
class RegionAdmin(admin.ModelAdmin):
    """ Тип документа: госконтракт или допсоглашение """
    list_display = ("id", "name",)


@admin.register(Initiator)
class TypeRoadAdmin(admin.ModelAdmin):
    """ Инициаторы закупки"""
    list_display = ("id", "name")


@admin.register(Status_Contract)
class TypeElRoadAdmin(admin.ModelAdmin):
    """ Статус контракта """
    list_display = ("id", "name")
