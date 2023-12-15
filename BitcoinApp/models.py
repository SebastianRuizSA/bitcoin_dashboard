from django.db import models

class Bitcoin(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    symbol = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

class ValorHistorico(models.Model):
    btc = models.ForeignKey(
        Bitcoin,
        on_delete=models.CASCADE
    )
    day_timestamp = models.CharField(max_length=50) # Los dias estan en formato UNIX timestamp.
    price = models.FloatField()
    marketcap = models.FloatField()

    class Meta:
        ordering = ("day_timestamp", )
