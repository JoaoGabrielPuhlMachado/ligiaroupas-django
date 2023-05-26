from django.db import models
from ligiaroupas.models import Categoria, Marca, Cor, Tamanho

class Item(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    quantidade = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="itens")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="itens")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="itens")
    tamanho = models.ForeignKey(Tamanho, on_delete=models.PROTECT, related_name="itens")

    def __str__(self):
        return f"{self.nome} {self.marca} {self.cor} Tamanho {self.tamanho} ({self.quantidade})"
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"