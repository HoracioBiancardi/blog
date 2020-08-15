from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from categorias.models import Categoria
from PIL import Image
from django.conf import settings
import os


class Post(models.Model):
    titulo_post = models.CharField(verbose_name="Titulo", max_length=255)
    autor_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="Autor",
    )
    data_post = models.DateTimeField(verbose_name="Data", default=timezone.now)

    conteudo_post = models.TextField(verbose_name="Conteudo")

    excerto_post = models.TextField(verbose_name="Resuno")
    categoria_post = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        verbose_name="Categoria",
    )
    imagem_post = models.ImageField(
        verbose_name="Imagem", upload_to="imagens/%Y/%m/%d/", blank=True, null=True,
    )
    publicado_post = models.BooleanField(verbose_name="Publicado", default=False)

    def __str__(self):
        return self.titulo_post

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem_post:
            self.resize_image(self.imagem_post.name, 800)

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60
        )
        new_img.close()
