from django.db import models


class Categoria(models.Model):
    nome_cat = models.CharField(verbose_name="Nome", max_length=50)

    def __str__(self):
        return self.nome_cat
