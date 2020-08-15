from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentario(models.Model):
    nome_comentario = models.CharField(verbose_name="Nome", max_length=50)
    email_comentario = models.EmailField(verbose_name="E-mail")
    comentario = models.TextField(verbose_name="Comentário")
    post_comentario = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name="Post"
    )
    usuario_comentario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="Usuário", blank=True, null=True
    )
    data_comentario = models.DateTimeField(verbose_name="Data", default=timezone.now)
    publicado_comentario = models.BooleanField(verbose_name="Publicado", default=False)

    def __str__(self):
        return self.nome_comentario

