from django.db import models

class Operative(models.Model):
    name = models.TextField(null=True, verbose_name="Название")
    V_eto_obem = models.TextField(null=True, verbose_name="Объем ОП")
    count_comp = models.TextField(null=True, verbose_name="Планок в комплекте")
    DIMM = models.TextField(null=True, verbose_name="форм фактор")
    DDR = models.TextField(null=True, verbose_name="DDR")
    freq = models.TextField(null=True, verbose_name="частота")
    freq1 = models.TextField(null=True, verbose_name="пропускная")
    cooler = models.TextField(null=True, verbose_name="Тип охлаждения")
    min_price = models.IntegerField(null=True, default=0, verbose_name="минимальная цена")
    min_price_ad = models.TextField(blank=True, null=True, verbose_name="мин адрес")

    def __str__(self):
        return "{0}".format(self.name)

    @property
    def its(self):
        return "Operative"

    class Meta:
        verbose_name = u"Оперативная память"
        verbose_name_plural = u"Оперативная память"


class Price(models.Model):
    tovar = models.ForeignKey(Operative, related_name="oper", on_delete=models.CASCADE)
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
        verbose_name = u"Цена на оперативку"
        verbose_name_plural = u"цена на оперативку"
