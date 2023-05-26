from django.db import models

class Marca(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"