from django.db import models
from profiles.models import Profile
from videokarta.models import Videocard
from proccesor.models import Proc
from OP.models import Operative
from motherboard.models import Motherboard

class buyed(models.Model):
    profile = models.ForeignKey(Profile, related_name="tovar_id", on_delete=models.CASCADE)
    proc = models.ForeignKey(Proc, related_name="proc", on_delete=models.CASCADE)
    operative = models.ForeignKey(Operative, related_name="ram", on_delete=models.CASCADE)
    mother = models.ForeignKey(Motherboard, related_name="mother", on_delete=models.CASCADE)
    video = models.ForeignKey(Videocard, related_name="vid", on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    json = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
# Create your models here.
