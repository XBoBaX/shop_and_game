from django.db import models

class games(models.Model):
    name = models.TextField(null=True, verbose_name="Название")
    processor_min = models.TextField(null=True, verbose_name="процессор_мин")
    RAM_min = models.TextField(null=True, verbose_name="оператива_мин")
    videocard_min = models.TextField(null=True, verbose_name="видеокарта_мин")
    memory_min = models.TextField(null=True, verbose_name="ЖД_мин")
    json_min = models.TextField(null=True, verbose_name="json")

    processor_max = models.TextField(null=True, verbose_name="процессор_мин")
    RAM_max = models.TextField(null=True, verbose_name="оператива_мин")
    videocard_max = models.TextField(null=True, verbose_name="видеокарта_мин")
    memory_max = models.TextField(null=True, verbose_name="ЖД_мин")
    json_max = models.TextField(null=True, verbose_name="json")

    img = models.ImageField(upload_to='image/', verbose_name='Изображение')

    def __str__(self):
        return "{0}".format(self.name)
