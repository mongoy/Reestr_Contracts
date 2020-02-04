from django.db import models


class TypeDoc(models.Model):
    """ Тип документа: госконтракт или допсоглашение """
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Документ')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        ordering = ('name',)  # сортировка


class Initiator(models.Model):
    """ Инициаторы закупки"""
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Инициатор')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Инициатор"
        verbose_name_plural = "Инициаторы"
        ordering = ('name',)  # сортировка


class StatusContract(models.Model):
    """ Статус контракта """
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ('name',)  # сортировка


class Contracts(models.Model):
    """ Реестр контрактов """
    # num_izv = models.CharField(max_length=20, db_index=True, verbose_name='Номер извещения', default='-')
    # nc_contract = models.CharField(max_length=30, db_index=True, verbose_name='Номер карточки контракта', default='-')
    num_contract = models.CharField(max_length=20, db_index=True, verbose_name='Номер контракта', default='-')
    name_object = models.CharField(max_length=500, db_index=True, verbose_name='Наименование объекта закупки',
                                   default='-')
    type_doc = models.ForeignKey(TypeDoc, on_delete=models.DO_NOTHING, verbose_name='Документ', default='-')
    y_contract = models.CharField(max_length=4, verbose_name='Год', default='1970')
    # nmck = models.FloatField(max_length=50, verbose_name='НМЦ')
    c_contract = models.FloatField(max_length=50, verbose_name='Цена контракта')
    # econom = models.FloatField(max_length=50, verbose_name='Экономия')
    # proc_econom = models.FloatField(max_length=6, verbose_name='Процент экономии')
    ini_contract = models.ForeignKey(Initiator, on_delete=models.DO_NOTHING, verbose_name='Инициатор', default='-')
    uch_contract = models.CharField(max_length=200, db_index=True, verbose_name='Участник', default='-')
    in_contract = models.CharField(max_length=10, null=True, verbose_name='Дата подписания контракта')
    in_work = models.CharField(max_length=10, null=True, verbose_name='Дата начала работ')
    out_work = models.CharField(max_length=10, null=True, verbose_name='Дата окончания работ')
    stat_contract = models.ForeignKey(StatusContract, on_delete=models.DO_NOTHING, verbose_name='Статус', default='-')
    work_contract = models.BooleanField('В работе')
    failures = models.BooleanField('Срыв сроков')
    executed = models.BooleanField('Исполнен')
    file_obj = models.FileField(upload_to='files/')
    data_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.num_contract

    class Meta:
        verbose_name = "Госконтракт"
        verbose_name_plural = "Госконтракты"
        ordering = ('y_contract', 'num_contract',)  # сортировка

# class FileContract(models.Model):
#     #
#     file_obj = models.FileField(upload_to='files/')
