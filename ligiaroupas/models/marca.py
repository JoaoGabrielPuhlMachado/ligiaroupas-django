from django.db import models

class Marca(models.Model):
    nome_marca = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_marca
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"