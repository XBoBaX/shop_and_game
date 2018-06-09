from django.db import models


class Soket(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название сокета")

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = u"Сокет для процессора"
        verbose_name_plural = u"Сокет для процессора"


class Proc(models.Model):
    name = models.TextField(verbose_name="Название")
    cooler = models.BooleanField(default=False, verbose_name="Есть ли куллер")
    series = models.CharField(blank=True, null=True, max_length=200, verbose_name="Серия")
    count_core = models.TextField(blank=True, null=True, verbose_name="Кол-во ядер")
    clock_freq = models.TextField(blank=True, null=True, verbose_name="Тактовая частота")
    freq = models.TextField(blank=True, null=True, verbose_name="Частота")
    proc_tech = models.CharField(blank=True, null=True, max_length=100, verbose_name="Техпроцесс")
    architecture = models.CharField(blank=True, null=True, max_length=100, verbose_name="Архитектура")
    integer_video = models.BooleanField(blank=True, default=False, verbose_name="Интегрированная графика")
    model_GPU = models.TextField(blank=True, null=True, verbose_name="модель интегр. графики")
    L1 = models.CharField(blank=True, null=True, max_length=50, verbose_name="кэш 1го")
    L2 = models.CharField(blank=True, null=True, max_length=50, verbose_name="кэш 2го")
    L3 = models.CharField(blank=True, null=True, max_length=50, verbose_name="кэш 3го")
    TDP = models.CharField(blank=True, null=True, max_length=50, verbose_name="Тепловыделение")
    sup_instr = models.TextField(blank=True, null=True, verbose_name="Поддержка инструкции")
    max_vol = models.CharField(blank=True, null=True, max_length=50, verbose_name="макс. объем")
    max_kanal = models.CharField(blank=True, null=True, max_length=50, verbose_name="макс. частота")
    min_price = models.IntegerField(blank=True, null=True, default=0, verbose_name="минимальная цена")
    min_price_ad = models.TextField(blank=True, null=True, verbose_name="мин адрес")

    sok = models.ForeignKey(Soket, null=True, related_name="soket_name", on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.name)

    @property
    def its(self):
        return "Proc"

    class Meta:
        verbose_name = u"Процессоры"
        verbose_name_plural = u"Процессоры"


class Price(models.Model):
    tovar = models.ForeignKey(Proc, related_name="tovar_id", on_delete=models.CASCADE)
    count = models.IntegerField(blank=True, null=True, verbose_name="Кол-во магазинов")
    price1 = models.IntegerField(blank=True, null=True, verbose_name="Цена 1го магазина")
    adress1 = models.TextField(blank=True, null=True, verbose_name="ссылка на 1ый магазин")
    price2 = models.IntegerField(blank=True, null=True, verbose_name="Цена 2го магазина")
    adress2 = models.TextField(blank=True, null=True, verbose_name="ссылка на 2ый магазин")
    price3 = models.IntegerField(blank=True, null=True, verbose_name="Цена 3го магазина")
    adress3 = models.TextField(blank=True, null=True, verbose_name="ссылка на 3ый магазин")
    price4 = models.IntegerField(blank=True, null=True, verbose_name="Цена 4го магазина")
    adress4 = models.TextField(blank=True, null=True, verbose_name="ссылка на 4ый магазин")
    price5 = models.IntegerField(blank=True, null=True, verbose_name="Цена 5го магазина")
    adress5 = models.TextField(blank=True, null=True, verbose_name="ссылка на 5ый магазин")
    price6 = models.IntegerField(blank=True, null=True, verbose_name="Цена 6го магазина")
    adress6 = models.TextField(blank=True, null=True, verbose_name="ссылка на 6ый магазин")
    price7 = models.IntegerField(blank=True, null=True, verbose_name="Цена 7го магазина")
    adress7 = models.TextField(blank=True, null=True, verbose_name="ссылка на 7ый магазин")
    price8 = models.IntegerField(blank=True, null=True, verbose_name="Цена 8го магазина")
    adress8 = models.TextField(blank=True, null=True, verbose_name="ссылка на 8ый магазин")
    price9 = models.IntegerField(blank=True, null=True, verbose_name="Цена 9го магазина")
    adress9 = models.TextField(blank=True, null=True, verbose_name="ссылка на 9ый магазин")
    price10 = models.IntegerField(blank=True, null=True, verbose_name="Цена 10го магазина")
    adress10 = models.TextField(blank=True, null=True, verbose_name="ссылка на 10ый магазин")

    def __str__(self):
        return "{0}_{1}".format(self.tovar.name, self.tovar.min_price)

    class Meta:
        verbose_name = u"Цена на процессоры"
        verbose_name_plural = u"цена на процессоры"
