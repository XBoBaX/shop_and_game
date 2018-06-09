from django.db import models
from videokarta.models import Connection
from proccesor.models import Soket


class Motherboard(models.Model):
    name = models.TextField(verbose_name="Название")
    dly_chego = models.TextField(null=True, verbose_name="По направлению")
    BIOS = models.TextField(null=True, )
    factor_OP = models.TextField(null=True, verbose_name="Форм-фактор ОЗУ")
    sound = models.TextField(null=True, verbose_name="Звук (каналов)")
    pins = models.TextField(null=True, verbose_name="Разъем питания")
    form_factor = models.TextField(null=True, verbose_name="Форм-фактор")
    chipset = models.TextField(null=True, verbose_name="Чипсет")
    OZU = models.TextField(null=True, verbose_name="слоты ОЗУ")
    taktovaya = models.TextField(null=True, verbose_name="Тактовая частота ОЗУ")
    otver = models.TextField(null=True, verbose_name="Разъемы")
    pin_proc = models.TextField(null=True, verbose_name="Питание процессора")
    min_price_ad = models.TextField(blank=True, null=True, verbose_name="мин адрес")

    min_price = models.IntegerField(null=True, default=0, verbose_name="минимальная цена")

    interf = models.ForeignKey(Connection, null=True, related_name="mother2", on_delete=models.CASCADE)
    sok = models.ForeignKey(Soket, null=True, related_name="mother", on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.name)

    @property
    def its(self):
        return "Motherboard"

    class Meta:
        verbose_name = u"Материнка"
        verbose_name_plural = u"Материнка"


class Price(models.Model):
    tovar = models.ForeignKey(Motherboard, related_name="tovar_id", on_delete=models.CASCADE)
    count = models.IntegerField(blank=True, null=True, verbose_name="Кол-во магазинов")
    price1 = models.IntegerField(null=True, verbose_name="Цена 1го магазина")
    adress1 = models.TextField(null=True, verbose_name="ссылка на 1ый магазин")
    price2 = models.IntegerField(null=True, verbose_name="Цена 2го магазина")
    adress2 = models.TextField(null=True, verbose_name="ссылка на 2ый магазин")
    price3 = models.IntegerField(null=True, verbose_name="Цена 3го магазина")
    adress3 = models.TextField(null=True, verbose_name="ссылка на 3ый магазин")
    price4 = models.IntegerField(null=True, verbose_name="Цена 4го магазина")
    adress4 = models.TextField(null=True, verbose_name="ссылка на 4ый магазин")
    price5 = models.IntegerField(null=True, verbose_name="Цена 5го магазина")
    adress5 = models.TextField(null=True, verbose_name="ссылка на 5ый магазин")
    price6 = models.IntegerField(null=True, verbose_name="Цена 6го магазина")
    adress6 = models.TextField(null=True, verbose_name="ссылка на 6ый магазин")
    price7 = models.IntegerField(null=True, verbose_name="Цена 7го магазина")
    adress7 = models.TextField(null=True, verbose_name="ссылка на 7ый магазин")
    price8 = models.IntegerField(null=True, verbose_name="Цена 8го магазина")
    adress8 = models.TextField(null=True, verbose_name="ссылка на 8ый магазин")
    price9 = models.IntegerField(null=True, verbose_name="Цена 9го магазина")
    adress9 = models.TextField(null=True, verbose_name="ссылка на 9ый магазин")
    price10 = models.IntegerField(null=True, verbose_name="Цена 10го магазина")
    adress10 = models.TextField(null=True, verbose_name="ссылка на 10ый магазин")

    def __str__(self):
        return "{0}_{1}".format(self.tovar.name, self.tovar.min_price)

    class Meta:
        verbose_name = u"Цена на материнку"
        verbose_name_plural = u"цена на материнку"
