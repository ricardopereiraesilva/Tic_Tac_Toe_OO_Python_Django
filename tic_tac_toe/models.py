from django.db import models

class JVDjangoDBModel(models.Model):
    match_status = models.IntegerField(default=1)
    enabled_player = models.IntegerField(default=0)
    strategy = models.IntegerField(default=0)
    move_order = models.IntegerField(default=0)
    strategy_way = models.IntegerField(default=0)
    p11 = models.IntegerField(default=0)
    p12 = models.IntegerField(default=0)
    p13 = models.IntegerField(default=0)
    p21 = models.IntegerField(default=0)
    p22 = models.IntegerField(default=0)
    p23 = models.IntegerField(default=0)
    p31 = models.IntegerField(default=0)
    p32 = models.IntegerField(default=0)
    p33 = models.IntegerField(default=0)
