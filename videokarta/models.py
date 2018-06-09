from django.db import models


class Connection(models.Model):
    name = models.CharField(max_length=50, verbose_name="Подключение к матери")

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = u"Интерфейс видеокарты"
        verbose_name_plural = u"Интерфейс видеокарты"


class Videocard(models.Model):
    name = models.TextField(verbose_name="Название")
    GPU = models.CharField(null=True, max_length=200, verbose_name="Модель GPU")
    memory_vol = models.CharField(null=True, max_length=200, verbose_name="Объем памяти")
    type_memory = models.CharField(null=True, max_length=200, verbose_name="Тип памяти")
    bit_capacity = models.CharField(null=True, max_length=200, verbose_name="Разрядность шины")
    freq_of_work = models.CharField(null=True, max_length=200, verbose_name="Частота работы GPU")
    memory_frequency = models.CharField(null=True, max_length=200, verbose_name="Частота работы памяти")
    process_tech = models.CharField(null=True, max_length=200, verbose_name="Техпроцесс")
    max_resolution = models.CharField(null=True, max_length=200, verbose_name="Макс. разрешение")
    directX = models.CharField(null=True, max_length=20, verbose_name="DirectX")
    openGL = models.CharField(null=True, max_length=20, verbose_name="OpenGL")
    max_monitors = models.CharField(null=True, max_length=200, verbose_name="Макс. мониторов")
    cooling = models.CharField(null=True, max_length=200, verbose_name="Охлаждение")
    power = models.CharField(null=True, max_length=200, verbose_name="Потребляемая мощность")
    length = models.CharField(null=True, max_length=200, verbose_name="Длина видеокарты")
    min_price = models.IntegerField(null=True, default=0, verbose_name="минимальная цена")
    min_price_ad = models.TextField(blank=True, null=True, verbose_name="мин адрес")

    interf = models.ForeignKey(Connection, null=True, related_name="int_name", on_delete=models.CASCADE)

    @property
    def its(self):
        return "Videocard"

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = u"Видеокарты"
        verbose_name_plural = u"Видеокарты"


class Price(models.Model):
    tovar = models.ForeignKey(Videocard, related_name="tovar_id", on_delete=models.CASCADE)
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
        verbose_name = u"Цена на видеокарты"
        verbose_name_plural = u"цена на видеокарты"
